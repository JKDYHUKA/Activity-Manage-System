<template>
    <div class="person_body_right" v-for="item in activity_Array">
        <div class="everyone">
          <p class="p-title">{{item.act_name}}</p>
          <p class="p-txt">{{item.act_describe}}</p>
          <div class="picture_box">
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
        activity_Array: [{act_name:"",act_describe:"",act_create_user:"",act_time:""}]
      }
      
    },
    methods:{
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

.everyone {
  width: 100%;
  height:220px;
  margin-top: 0px;
  margin-bottom: 20px;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1),
              0 0 5px rgba(0, 0, 0, 0.1),
              0 0 5px rgba(0, 0, 0, 0.1),
              0 0 5px rgba(0, 0, 0, 0.1);
}
.p-title{
  margin-left: 10px;
  margin-bottom:15px;
  padding-top:10px;
  padding-left:15px;
  font-size: 20px;
}
.p-txt{
  margin-left: 10px;
  margin-top:5px;
  margin-bottom:5px;
  padding-left:10px;
  font-size: 15px;
}
.picture_box{
  margin-top:5px;
  margin-bottom:5px;
  height:100px;
  width:100%;
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
