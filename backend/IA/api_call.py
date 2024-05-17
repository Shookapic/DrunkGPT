from openai import OpenAI
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = OpenAI()

@app.route('/generate', methods=['POST'])
def generate():
    user_message = request.json['prompt']
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a very drunk assistant. Sometimes do not understand what you are saying."},
            {"role": "user", "content": user_message}
        ],
        max_tokens=100,
        temperature=1
    )
    response_message = completion.choices[0].message.content
    return jsonify({'response': response_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
