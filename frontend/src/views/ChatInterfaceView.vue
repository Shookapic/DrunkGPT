<template>
  <div class="chat-interface">
    <div class="header">
      Drunk GPT
      <LeaveButton />
    </div>
    <div class="chat-box">
      <div 
        v-for="message in messages" 
        :key="message.id" 
        :class="['message', message.sender]"
      >
        {{ message.text }}
      </div>
    </div>
    <div class="input-container">
      <input 
        v-model="input"
        @keyup.enter="() => { decreaseAttempts(); sendMessage(); }"
        placeholder="Type a message..."
      />
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import LeaveButton from '../components/Leave.vue';

export default {
  components: {
    LeaveButton
  },
  data() {
    return {
      input: '',
      messages: []
    };
  },
  methods: {
    async decreaseAttempts() {
      try {
        alert('decreasing attempts');
        const response = await fetch('http://10.106.1.161:5001/decrease_attempts', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            username: localStorage.getItem('username')
          })
        });
        const data = await response.json();
        if (response.status === 200) {
          if (data.remaining_attempts === 0) {
            alert('You have no more attempts left. Please try again later.');
            this.$router.push('/login');
            localStorage.removeItem('username');
          }
        } else {
          alert(data.message);
        }
      } catch (error) {
        console.error('Error decreasing attempts:', error);
      }
    },
    async sendMessage() {
      if (this.input.trim() === '') return;
      this.messages.push({ id: this.messages.length, text: this.input, sender: 'user' });
      try {
        const response = await axios.post('http://10.106.1.161:5000/generate', { prompt: this.input });
        this.messages.push({ id: this.messages.length, text: response.data.response, sender: 'bot' });
      } catch (error) {
        console.error('Error sending message:', error);
      }
      this.input = '';
    }
  }
};
</script>

<style>
body {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 0;
  height: 100vh;
  background: linear-gradient(180deg, #000000, #5A5A5A);
  font-family: Exo2, Arial, sans-serif;
  color: white;
}

.chat-interface {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 100vh;
  width: 100vw;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 20px;
  font-size: 24px;
}

.chat-box {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}

.input-container {
  display: flex;
  justify-content: center;
  padding: 20px;
}

input {
  width: 80%;
  padding: 15px;
  border-radius: 50px;
  border: none;
  outline: none;
  font-size: 18px;
  background-color: #F0F0F0;
}

input:focus {
  background-color: #E0E0E0;
}

.message {
  margin: 10px 0;
  padding: 10px 20px;
  border-radius: 20px;
  max-width: 60%;
  word-wrap: break-word;
}

.user {
  align-self: flex-end;
  background-color: #007BFF;
  color: white;
}

.bot {
  align-self: flex-start;
  background-color: #E0E0E0;
  color: black;
}
</style>
