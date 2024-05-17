<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script>
import ChatInterface from './views/ChatInterfaceView.vue';
import LeaveButton from './components/Leave.vue';
export default {
  components: {
    ChatInterface,
    LeaveButton,
  }
};
</script>

<style>
html, body {
  display: flex;;
  padding-left: -900vh;
}

</style>