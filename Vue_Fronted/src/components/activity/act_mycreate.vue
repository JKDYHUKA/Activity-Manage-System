<template>
  <el-calendar>
    <template #date-cell="{ data }">
      <div :class="{ 'has-event': getActs(data.day).length }" @click="selectDate(data)">
        <p :class="data.isSelected ? 'is-selected' : ''">
          {{ data.day.split('-').pop() }}
        </p>
        <p v-if="getActs(data.day).length" class="event-name">
          {{ getActs(data.day)[0].act_name }}
        </p>
      </div>
    </template>
  </el-calendar>
  <div class="details-div" v-if="selectedDate && getActs(selectedDate.day).length">
    <p v-for="act in getActs(selectedDate.day)" :key="act.act_name" class="event-item">
      • 您创建的活动:{{ act.act_name }}在今天的{{ act.act_start }}点到{{ act.act_end }}
    </p>
  </div>
</template>

<script>
import { set_no_csrf_header } from '@/utils/httpUtils'

export default {
  data() {
    return {
      notice_Array: [
        { act_date: "", act_name: "",act_start:"",act_end:"" },
      ],
      selectedDate: null
    }
  },
  methods: {
    getActs(date) {
      return this.notice_Array.filter(act => act.act_date === date);
    },
    selectDate(data) {
      this.selectedDate = data;
    },
    fetchActivities() {
      fetch('http://127.0.0.1:8000/api/get_activities_by_personal_number/', {
        method: 'GET',
        headers:set_no_csrf_header(),
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('网络响应错误');
        }
        return response.json();
      })
      .then(data => {
        this.notice_Array = data.act_details;
      })
      .catch(error => {
        console.error('获取数据失败:', error);
      });
    }
  },
  created(){
    this.fetchActivities()
  }
}
</script>

<style>
.details-div {
  width: 80%; /* 宽度设置为父元素的80% */
  max-width: 300px; /* 最大宽度保持300px，以免过宽 */
  min-height: 200px; /* 最小高度保持200px */
  background-color: #f2f2f2;
  border: 1px solid #dcdcdc;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column; /* 使内容垂直排列 */
  justify-content: flex-start; /* 内容靠顶部对齐 */
  align-items: flex-start; /* 内容靠左对齐 */
  font-family: 'Arial', sans-serif;
  color: #333;
  padding: 20px; /* 添加内边距，让文字与边框有合理的距离 */
  margin: 20px auto; /* 上下保持20px的外边距，左右自动调整以居中 */
  transition: transform 0.3s ease;
}

.has-event {
  border-left: 3px solid #1989fa;
  padding-left: 4px;
}

.is-selected {
  color: #1989fa;
}

.event-name {
  margin-top: 4px;
  font-size: 0.75em;
  color: #606266;
}
</style>
