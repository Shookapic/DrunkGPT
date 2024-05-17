from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import bcrypt

database = Flask(__name__)
CORS(database)

def initialize_db():
    conn = sqlite3.connect('./database.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        chat_attempts INTEGER NOT NULL,
        state BOOL FALSE
    )
    ''')
    conn.commit()
    conn.close()

@database.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    username = data['username']
    password = data['password']

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    conn = sqlite3.connect('./database.db')
    cursor = conn.cursor()

    try:
        cursor.execute('''
        INSERT INTO users (username, password, chat_attempts, state) VALUES (?, ?, ?, ?)
        ''', (username, hashed_password.decode('utf-8'), 10, False))
        conn.commit()
        return jsonify({"message": f"User '{username}' added successfully."}), 201
    except sqlite3.IntegrityError as e:
        return jsonify({"error": str(e), "message": f"User '{username}' already exists."}), 400
    finally:
        conn.close()

@database.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    conn = sqlite3.connect('./database.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT * FROM users WHERE username = ?
    ''', (username,))
    user = cursor.fetchone()

    conn.close()

    if user:
        stored_password = user[2]
        if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
            return jsonify({"message": f"User '{username}' logged in successfully."}), 200
    return jsonify({"message": "Invalid credentials."}), 401

@database.route('/is_logged_in', methods=['POST'])
def is_logged_in():
    data = request.json
    username = data['username']

    conn = sqlite3.connect('./database.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT state FROM users WHERE username = ?
    ''', (username,))
    state = cursor.fetchone()

    conn.close()

    if state:
        return jsonify({"state": state[0]}), 200
    return jsonify({"message": "User not found."}), 404

@database.route('/set_state', methods=['POST'])
def set_state():
    data = request.json
    username = data['username']
    state = data['state']

    conn = sqlite3.connect('./database.db')
    cursor = conn.cursor()

    cursor.execute('''
    UPDATE users SET state = ? WHERE username = ?
    ''', (state, username))
    conn.commit()

    conn.close()

    return jsonify({"message": f"State set to {state}."}), 200

@database.route('/decrease_attempts', methods=['POST'])
def decrease_attempts():
    print("[[[[[[[[[[[[[[[[[[[[[[[[[DECREASING]]]]]]]]]]]]]]]]]]]]]]]]]]")
    data = request.json
    username = data['username']

    conn = sqlite3.connect('./database.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT chat_attempts FROM users WHERE username = ?
    ''', (username,))
    chat_attempts = cursor.fetchone()

    if chat_attempts is None:
        conn.close()
        return jsonify({"message": "User not found"}), 404

    if chat_attempts[0] > 0:
        cursor.execute('''
        UPDATE users SET chat_attempts = chat_attempts - 1 WHERE username = ?
        ''', (username,))
        conn.commit()

        cursor.execute('''
        SELECT chat_attempts FROM users WHERE username = ?
        ''', (username,))
        chat_attempts = cursor.fetchone()

    conn.close()

    return jsonify({"message": "Chat attempts decreased.", "remaining_attempts": chat_attempts[0]}), 200


if __name__ == '__main__':
    initialize_db()
    database.run(host='0.0.0.0', port=5001)
