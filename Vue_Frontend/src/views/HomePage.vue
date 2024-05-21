<template>
  <div class="home">
    <Top />
    <input v-model="currentTime" disabled />
    <button @click="fetchTime">获取当前时间</button>
  </div>
</template>
  
<script>
import Top from '../components/Top.vue';
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
        const response = await fetch('http://127.0.0.1:8000/api/get_current_time');
        const data = await response.json();
        console.log(data)
        const year = data.year
        const month = data.month
        const day = data.day
        this.currentTime = year + "-" + month + "-" + day; // 修改此处
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
  