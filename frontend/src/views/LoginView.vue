<template>
  <div class="screen-1">
    <div class="email">
      <label for="email">Username</label>
      <div class="sec-2">
        <ion-icon name="mail-outline"></ion-icon>
        <input type="email" name="email" placeholder="Username"/>
      </div>
    </div>
    <div class="password">
      <label for="password">Password</label>
      <div class="sec-2">
        <ion-icon name="lock-closed-outline"></ion-icon>
        <input class="pas" type="password" name="password" placeholder="*********"/>
        <ion-icon class="show-hide" name="eye-outline"></ion-icon>
      </div>
    </div>
    <button class="login" @click="login">Login</button>
    <button class="footer" @click="signup">Create & Connect</button>
  </div>
</template>

<script>
export default {
  name: 'LoginScreen',
  methods: {
    async login() {
      const response = await fetch('http://10.106.1.161:5001/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          username: document.querySelector('input[name="email"]').value,
          password: document.querySelector('input[name="password"]').value
        })
      });
      if (response.ok) {
        localStorage.setItem('username', document.querySelector('input[name="email"]').value);
        await fetch('http://10.106.1.161:5001/set_state', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            username: document.querySelector('input[name="email"]').value,
            state: 1
          })
        });
        this.$router.push('/chat');
      } else {
        alert('Invalid username or password');
      }
    },
    async signup() {
      const response = await fetch('http://10.106.1.161:5001/add_user', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          username: document.querySelector('input[name="email"]').value,
          password: document.querySelector('input[name="password"]').value
        })
      });
      if (response.ok) {
        const username = document.querySelector('input[name="email"]').value;
        localStorage.setItem('username', username);
        await fetch('http://10.106.1.161:5001/set_state', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            username: document.querySelector('input[name="email"]').value,
            state: 1
          })
        });
        alert('Signup successful');
        this.$router.push('/chat');
      } else {
        alert('Username taken. Please try another.');
      }
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@100;200;300;400;500;600;700;800;900&display=swap');

* {
  font-family: "Poppins";
}

.screen-1 {
  width: 30em;
  background: #f1f7fe;
  padding: 2em;
  display: flex;
  flex-direction: column;
  border-radius: 30px;
  box-shadow: 0 0 2em #e6e9f9;
  margin-left: 120%;
}

.screen-1 .logo {
  margin-top: -3em;
}

.screen-1 .email {
  background: white;
  box-shadow: 0 0 2em #e6e9f9;
  padding: 1em;
  display: flex;
  flex-direction: column;
  gap: 0.5em;
  border-radius: 20px;
  color: #4d4d4d;
  margin-top: 6vh;
}

.screen-1 .email input {
  outline: none;
  border: none;
}

.screen-1 .email input::-moz-placeholder {
  color: black;
  font-size: 0.9em;
}

.screen-1 .email input:-ms-input-placeholder {
  color: black;
  font-size: 0.9em;
}

.screen-1 .email input::placeholder {
  color: black;
  font-size: 0.9em;
}

.screen-1 .email ion-icon {
  color: #4d4d4d;
  margin-bottom: -0.2em;
}

.screen-1 .password {
  background: white;
  box-shadow: 0 0 2em #e6e9f9;
  padding: 1em;
  display: flex;
  flex-direction: column;
  gap: 0.5em;
  border-radius: 20px;
  color: #4d4d4d;
}

.screen-1 .password input {
  outline: none;
  border: none;
}

.screen-1 .password input::-moz-placeholder {
  color: black;
  font-size: 0.9em;
}

.screen-1 .password input:-ms-input-placeholder {
  color: black;
  font-size: 0.9em;
}

.screen-1 .password input::placeholder {
  color: black;
  font-size: 0.9em;
}

.screen-1 .password ion-icon {
  color: #4d4d4d;
  margin-bottom: -0.2em;
}

.screen-1 .password .show-hide {
  margin-right: -5em;
}

.screen-1 .login {
  padding: 1em;
  background: #3e4684;
  color: white;
  border: none;
  border-radius: 30px;
  font-weight: 600;
  cursor: pointer;
}

.screen-1 .footer {
  padding: 1em;
  background: linear-gradient(135deg, #34e89e, #0f3443);
  color: white;
  border: none;
  border-radius: 30px;
  font-weight: 600;
  text-align: center;
  cursor: pointer;
}

button {
  cursor: pointer;
  width: 100%;
  text-align: center;
}
</style>
