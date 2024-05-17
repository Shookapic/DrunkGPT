<template>
    <div class="chat-sidebar">
      <div class="header">Conversations</div>
      <ul class="conversation-list">
        <li v-for="(conversation, index) in conversations" :key="index">
          {{ conversation }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        conversations: ["Conversation 1", "Conversation 2", "Conversation 3"] // Example data
      };
    }
  };
  </script>
  
  <style>
  .chat-sidebar {
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
  
  .conversation-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .conversation-list li {
    padding: 10px 20px;
    border-bottom: 1px solid #444;
    cursor: pointer;
  }
  
  .conversation-list li:hover {
    background-color: rgba(255, 255, 255, 0.1);
  }
  </style>
  