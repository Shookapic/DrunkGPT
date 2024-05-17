<template>
    <div class="private-messages">
      <div class="header">Private Messages</div>
      <ul class="message-list">
        <li v-for="(message, index) in messages" :key="index">
          {{ message }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        messages: ["Private Message 1", "Private Message 2", "Private Message 3"] // Example data
      };
    }
  };
  </script>
  
  <style>
  .private-messages {
    width: 20%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.8);
    display: flex;
    flex-direction: column;
  }
  
  .header {
    padding: 20px;
    font-size: 24px;
    text-align: center;
  }
  
  .message-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .message-list li {
    padding: 10px 20px;
    border-bottom: 1px solid #444;
    cursor: pointer;
  }
  
  .message-list li:hover {
    background-color: rgba(255, 255, 255, 0.1);
  }
  </style>
  