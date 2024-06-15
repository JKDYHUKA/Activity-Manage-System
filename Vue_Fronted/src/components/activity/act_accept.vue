<template>
  <div class="person_body_right" v-for="item in notice_Array">
    <div class="everyone" v-if="item.act_name && isVisible" @click="hideDivs(item)">
      <div class="div-inline-block-left">{{ item.act_name }}</div>
      <div class="div-inline-block-right">{{ item.notice_title }}</div>
    </div>
  </div>
  <div v-if="!isVisible">
    <el-container>
      <el-header style="border: 1px solid black;height: 33px;">
        <el-button @click="isVisible=true">back</el-button>
        {{ clickedItem.act_name }}
      </el-header>
      <el-main style="border: 1px solid black;padding: 10px">
          <div>
            <span>活动描述:</span>
            {{ clickedItem.notice_content }}
          </div>
          <div v-if="clickedItem.notice_title==='Invitation'">
            <span>邀请你参加</span>
            <span class="p-name">{{clickedItem.act_name}}</span>
            <span>是否接受  </span>
            <el-button @click="actAccept(clickedItem)" size="small">
              <el-icon size="20px"><Check /></el-icon>
            </el-button>
            <el-button @click="actRefuse(clickedItem)" size="small">
              <el-icon size="20px"><Close /></el-icon>
            </el-button>
          </div>
      </el-main>
    </el-container>
  </div>
</template>
  
  <script>
  import { mapGetters } from 'vuex';
  import { set_no_csrf_header } from '@/utils/httpUtils'
  export default{
    data(){
      return {
        isVisible: true,
        clickedItem : null,
        notice_Array: [
          { act_name: "11", notice_content: "22",notice_type:"",notice_title:"Invitation", notice_id: "", act_accept: null, is_choose:false }
        ]
      }
      
    },
    computed: {
    ...mapGetters([
      'getUsername',
      'getUserId',
    ])
    },
    methods:{
      hideDivs(item) {
        this.isVisible = false;
        this.clickedItem = item;
      },
      actAccept(item){
        item.is_choose=true;
        item.act_accept=true;
        fetch('http://127.0.0.1:8000/api/accept_invitation/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id: this.clickedItem.notice_id,
                userid: this.getUserId,
                content: this.clickedItem.notice_content,
            })
        })
        
        .then(response => {
            return response.json()
        })
        .catch(error => {
            console.error(error)
        })
      },
      actRefuse(item){
        item.is_choose=true;
        item.act_accept=false;
        fetch('http://127.0.0.1:8000/api/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                act_username:this.getUsername,
                act_name: clickedItem.act_name,
                act_accept: clickedItem.act_accept,
            })
        })
        
        .then(response => {
            return response.json()
        })
        .catch(error => {
            console.error(error)
        })
      },
      fetchNotices() {
      fetch('http://127.0.0.1:8000/api/get_notices/', {
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
        this.notice_Array = data.notice_details;
      })
      .catch(error => {
        console.error('获取数据失败:', error);
      });
    }
    },
    created(){
      this.fetchNotices()
  
    }
  }
  
  </script>
  
  <style scoped="scoped">
.div-inline-block-left {
  display: inline-block;
  width: 80%; /* 或者你需要的宽度 */
  justify-content: center;
  align-items: center;
  text-align: left; /* 左对齐 */
  padding: 10px; /* 设置内边距，你可以根据需要调整这个值 */
  border-right: 2px solid black;
}

.div-inline-block-right {
  display: inline-block;
  width: 20%; /* 或者你需要的宽度 */
  justify-content: center;
  align-items: center;
  text-align: right; /* 右对齐 */
  padding: 10px; /* 设置内边距，你可以根据需要调整这个值 */
}

  .everyone {
  width: 100%;
  height:60px;
  margin-top: 0px;
  margin-bottom: 20px;
  border-radius: 5px;
  display: flex;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1),
              0 0 5px rgba(0, 0, 0, 0.1),
              0 0 5px rgba(0, 0, 0, 0.1),
              0 0 5px rgba(0, 0, 0, 0.1);
  }

  </style>
  