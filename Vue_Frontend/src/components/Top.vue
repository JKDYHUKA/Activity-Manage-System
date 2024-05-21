<template>
    <div class="top-bar">
      <button @click="login">登录</button>
      <button @click="register">注册</button>
    </div>
</template>
  
  <script>
  export default {
    methods: {
      login() {
        // 处理登录逻辑
      },
      register() {
        // 处理注册逻辑
      }
    }
  }
  </script>
  
  <style scoped>
  /* 样式定义 */
  .top-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
    background-color: #f0f0f0;
  }
  button {
    margin: 0 10px;
  }
  </style>
  