<template>
    <div class="leave-container">
      <button class="leave-button" @click="leave">Disconnect</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'LeaveScreen',
    methods: {
      async leave() {
        this.$router.push('/login');
        alert("leaving");
        localStorage.removeItem('username');
        await fetch('http://10.106.1.161:5001/set_state', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            username: document.querySelector('input[name="email"]').value,
            state: 0
          })
        });
      }
    }
  }
  </script>
  
  <style scoped>
  .leave-container {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .leave-button {
    padding: 12px 24px;
    font-size: 16px;
    font-weight: bold;
    color: #ffffff;
    background: linear-gradient(135deg, #ff416c, #ff4b2b);
    border: none;
    border-radius: 50px;
    box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
    cursor: pointer;
    transition: all 0.3s ease;
  }
  
  .leave-button:hover {
    box-shadow: 0 15px 20px rgba(0, 0, 0, 0.2);
    transform: translateY(-2px);
  }
  
  .leave-button:active {
    box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
    transform: translateY(2px);
  }
  </style>
  