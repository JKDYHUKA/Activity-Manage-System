<template>
    <div class="home">
      <input v-model="currentTime" disabled />
      <button @click="fetchTime">获取当前时间</button>
    </div>
</template>
  
<script>
import Top from '../components/Top.vue'
export default {
    components: {
        Top,
    },
    data() {
      return {
        currentTime: ''
      };
    },
    methods: {
      async fetchTime() {
        try {
          // 从后端获取当前时间
          const response = await fetch('/api/getTime');
          const data = await response.json();
          this.currentTime = data.time;
        } catch (error) {
          console.error('获取时间失败：', error);
        }
      }
    }
  }
  </script>
  
  <style scoped>
  /* 样式定义 */
  .home {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
  }
  input {
    width: 200px;
    padding: 5px;
    margin-bottom: 10px;
  }
  button {
    padding: 8px 16px;
    background-color: #007bff;
    color: #fff;
    border: none;
    cursor: pointer;
  }
  </style>
  