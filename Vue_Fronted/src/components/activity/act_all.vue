<template>
  <div class="person_body_right" v-for="item in activity_Array">
    <div class="everyone" v-if="item.act_name && isVisible" @click="hideDivs(item)">
      <p class="p-title">{{item.act_name}}</p>
      <div class="p-txt">
        {{item.act_describe}}
      </div>
      <div class="div-bottom">
        <div class="div-bottom-left">{{item.act_create_user}}</div>
        <div class="div-bottom-right">{{item.act_time}}</div>
      </div>
    </div>
  </div>
  <div class="common-layout" v-if="!isVisible">
    <el-container>
      <el-header style="border: 1px solid black;height: 33px;">
        <el-button @click="isVisible=true">back</el-button>
      </el-header>
      <el-container>
        <el-aside style="border: 1px solid black;width: 50%;padding: 10px">
          <p>活动名称:{{ this.clickedItem.act_name }}</p>
          <p>活动描述:{{ this.clickedItem.act_describe }}</p>
          <p>活动时间:{{ this.clickedItem.act_time }}</p>
          <el-button type="primary" @click="toChat(this.chat_id)">加入活动聊天室</el-button>
        </el-aside>
        <el-main style="border: 1px solid black;width: 50%;padding: 10px">
          <el-table :data="tableData" style="width: 100%" max-height="250">
            <el-table-column prop="username" label="人员列表" width="120" />
            <el-table-column prop="usertype" label="人员类型" width="120" />
            <el-table-column fixed="right" label="Operations" width="120">
              <template #default="scope">
                <el-button
                  link
                  type="primary"
                  size="small"
                  v-if="this.getUsername===clickedItem.act_create_user"
                  @click.prevent="handleDelete(scope.$index)"
                >
                  Remove
                </el-button>
              </template>
            </el-table-column>
          </el-table>
          <div v-if="this.getUsername===clickedItem.act_create_user">
            <el-input v-model="act_userid"/>
            <el-form-item label="活动人员类型" prop="act_usertype">
              <el-segmented :options="UserOptions" v-model="this.act_usertype" />
            </el-form-item>
            <el-button @click="handleAdd">添加</el-button>
            <el-button @click="handleSubmit">确定修改</el-button>
          </div>
          <el-steps style="max-width: 600px;" :active="clickedItem.act_step" finish-status="success" simple>
            <el-step title="审核中" />
            <el-step title="通过" />
          </el-steps>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>
  
<script>
  import { set_no_csrf_header } from '@/utils/httpUtils'
  import { mapGetters } from 'vuex';
  export default{
    data(){
      return{
        act_usertype:"",
        act_userid:"",
        isVisible: true,
        activity_Array: [{act_id:"12",act_name:"12",act_type:"",act_describe:"12",act_create_user:"12",act_time:"12",act_step:"1"}],
        //act_step为1:审核中，2：通过
        clickedItem : null,
        tableData : [],
        UserOptions : ['参会人员', '嘉宾'],
        userid_str:[],
        usertype_str:[],
        chat_id:"f6e1ec10cd9f4be38edee9c7d4de1e92"
      }
    },
    computed: {
    ...mapGetters([
      'getUsername'
    ])
    },
    methods: {
      handleAdd(){
        const personal_number = this.act_userid
        fetch('http://127.0.0.1:8000/api/get_user_by_personal_number/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            userId: personal_number
          })
        })
        .then(res => {
          return res.json()
        })
        .then(data => {
          if (data.code === '0'){
            this.tableData.push({
              username: data.username,
              userid: this.act_userid,
              usertype:this.act_usertype,
            })
          }
          else{
            alert(data.message)
          }
        })
      },
      handleSubmit(){
        this.tableData.forEach((item)=>{
          this.userid_str.push(item.userid);
          this.usertype_str.push(item.usertype);
        })
        console.log(this.userid_str)
        fetch('http://127.0.0.1:8000/api/activity_member_modify/', {
          method: 'POST',
          headers: set_no_csrf_header(),
          body: JSON.stringify({
            act_id:this.clickedItem.act_id,
            userid_str:this.userid_str,
            usertype_str:this.usertype_str,
          })
        })
        .then(response => {
            return response.json()
        })
        .catch(error => {
            console.error(error)
        })
      },
      handleDelete(index) {
        this.tableData.splice(index, 1);
      },
      fetchTableData(){
        fetch('http://127.0.0.1:8000/api/get_all_members/', {
          method: 'POST',
          headers:set_no_csrf_header(),
          body: JSON.stringify({
          act_id:this.clickedItem.act_id,
        })
        })
        .then(response => {
          if (!response.ok) {
            throw new Error('网络响应错误');
          }
          return response.json();
        })
        .then(data => {
          this.tableData = data.tableData;
        })
        .catch(error => {
          console.error('获取数据失败:', error);
        });
      },
      hideDivs(item) {
        this.isVisible = false; // 点击后设置为false，所有div将不显示
        this.clickedItem = item; // 记录被点击的div的整个对象
        this.fetchTableData();
        console.log('Clicked item:', this.clickedItem); // 可以在控制台查看被点击的对象
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
      },
      toChat(chatID){
        const userId = this.$route.params.id;
            // const chatID = 8888;
            this.$router.push({
                path: `/chat/${userId}/${chatID}`
            })
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
  height:160px;
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
  
  </style>