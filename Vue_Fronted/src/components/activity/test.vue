<template>
  <div class="person_body_right" v-for="item in activity_Array" :key="item.act_name">
    <p></p>
    <div class="everyone" v-if="item.is_choose === false&&item.act_name">
      <div class="p-title">
        <span>邀请你参加</span>
        <span class="p-name">{{item.act_name}}</span>
        <span>是否接受  </span>
        <el-button @click="actAccept(item)" size="small">
          <el-icon size="20px"><Check /></el-icon>
        </el-button>
        <el-button @click="actRefuse(item)" size="small">
          <el-icon size="20px"><Close /></el-icon>
        </el-button>
      </div>
      <div class="p-txt">
        {{item.act_describe}}
      </div>
      <div class="div-bottom">
        <div class="div-bottom-left">{{item.act_create_user}}</div>
        <div class="div-bottom-right">{{item.act_time}}</div>
      </div>
    </div>
  </div>

</template>

<script>
import { set_no_csrf_header } from '@/utils/httpUtils'
export default{
  data(){
    return {
      activity_Array: [
        { act_name: "活动1", act_describe: "描述1", act_create_user: "创建者1", act_time: "时间1", act_accept: true,is_choose:false },
        { act_name: "活动2", act_describe: "描述2", act_create_user: "创建者2", act_time: "时间2", act_accept: null,is_choose:false },
      ]
    }
    
  },
  methods:{
    actAccept(item){
      item.is_choose=true;
      item.act_accept=true;
      fetch('http://127.0.0.1:8000/api/', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json'
          },
          body: JSON.stringify({
              act_name: item.act_name,
              act_accept: item.act_accept,
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
              act_name: item.act_name,
              act_accept: item.act_accept,
          })
      })
      
      .then(response => {
          return response.json()
      })
      .catch(error => {
          console.error(error)
      })
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
      this.activity_Array = data.act_details;
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

<style scoped="scoped">

.p-title{
margin-left: 10px;
margin-bottom:15px;
padding-top:10px;
padding-left:15px;
}
.everyone {
width: 100%;
height:160px;
margin-top: 0px;
margin-bottom: 20px;
border-radius: 5px;
box-shadow: 0 0 5px rgba(0, 0, 0, 0.1),
            0 0 5px rgba(0, 0, 0, 0.1),
            0 0 5px rgba(0, 0, 0, 0.1),
            0 0 5px rgba(0, 0, 0, 0.1);
}
.p-name{
font-size: 20px;
}
.p-txt{
margin-top:5px;
margin-bottom:5px;
padding-left: 15px;
padding-right: 15px;
height:70px;
width:95%;
overflow: auto;
}
.div-buttom{
margin:0px;
padding:0px;
height: 30px;
width:100%;
}
.div-bottom {
margin: 0;
padding: 0;
height: 30px;
width: 100%;
}

.div-bottom-left {
margin: 0;
padding: 0;
height: 30px;
width: 48%;
padding-left:15px;
font-size:20px;
display: inline-block;
}
.div-bottom-right{
margin: 0;
padding: 0;
height: 30px;
width: 48%;
padding-right:10px;
font-size:20px;
display: inline-block;
text-align: right;
}
</style>
