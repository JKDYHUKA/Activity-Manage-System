<template>
  <head>
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="QiangSang">
    <meta name="twitter:title" content="{{ activity.act_name }}">
    <meta name="twitter:description" content="{{ activity.act_description }}">
    <meta name="twitter:image" content="https://www.gamersky.com/showimage/id_gamersky.shtml?https://img1.gamersky.com/upimg/pic/2024/06/14/origin_202406141711163447.png">
  </head>
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
          <p>已发送通知:{{ this.send_number }}</p>
          <p>已接受通知:{{ this.accept_number }}</p>
          <el-button type="primary" @click="toChat(this.clickedItem.act_id)">加入活动聊天室</el-button>
          <el-button type="primary" @click="shareOnTwitter(this.clickedItem)">Share on Twitter</el-button>

          <el-popover placement="right" :width="400" trigger="click" :visible="visible">
            <template #reference>
              <el-button type="primary" style="margin-right: 16px" @click="visible = true">创建通知</el-button>
            </template>
            <el-input v-model="this.notice_title" placeholder="通知标题"></el-input>
            <el-input v-model="this.notice_content" placeholder="通知内容"></el-input>
            <el-button size="small" text @click="visible = false">cancel</el-button>
            <el-button @click="submitNotice()">提交</el-button>
          </el-popover>

          <div>
            <br/>
            <div>
              <!-- 上传 /尝试-->
              <upload_file></upload_file>
            </div>
          </div>
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
                  v-if="this.getUsername===clickedItem.act_create_user&&this.clickedItem.step==='1'"
                  @click.prevent="handleDelete(scope.$index)"
                >
                  Remove
                </el-button>
              </template>
            </el-table-column>
          </el-table>
          <div v-if="this.getUsername===clickedItem.act_create_user&&this.clickedItem.step==='1'">
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
            <el-step title="活动完成" @click="finishACT(clickedItem)" />
          </el-steps>
          <div>
            <!-- 下载 -->
            <download_file></download_file>
          </div>
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>
  
<script>
  import { set_no_csrf_header } from '@/utils/httpUtils'
//  import { tr } from 'element-plus/es/locale';
  import { mapGetters } from 'vuex'
  import { mapActions } from "vuex"
  import upload_file from '@/components/activity/upload.vue'
  import download_file from '@/components/activity/download.vue'
  export default{
    components:{
      upload_file,
      download_file
    },
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
        chat_id:"",
        visible: false,
        notice_content:"",
        notice_title:"",
        accept_number:"",
        send_number: "",
      }
    },
    computed: {
    ...mapGetters([
      'getUsername',
      'getActLoad',
      'getUserId',
    ])
    },
    methods: {
      shareOnTwitter(item) {
        const tweetText = `活动名字: ${item.act_name}\n\n活动描述: ${item.act_describe}\n\n想要参加我们活动的话, 请私信我哦`;
        const tweetUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(tweetText)}`;
        window.open(tweetUrl, '_blank');
      },
      submitNotice(){
        this.visible = false,
        fetch('http://127.0.0.1:8000/api/create_notice/', {
            method: 'POST',
            headers: set_no_csrf_header(),
            body: JSON.stringify({
              act_id:this.clickedItem.act_id,
              notice_content:this.notice_content,
              notice_title:this.notice_title,
            })
          })
          .then(response => {
              return response.json()
          })
          .catch(error => {
              console.error(error)
          })
      },
      createNotice(){
        this.newNotice = true;
      },
      finishACT(Item){
        if (Item.act_step===2){
          Item.act_step=3;
          fetch('http://127.0.0.1:8000/api/activity_member_modify/', {
            method: 'POST',
            headers: set_no_csrf_header(),
            body: JSON.stringify({
              act_step:Item.act_step,
              act_id:Item.act_id
            })
          })
          .then(response => {
              return response.json()
          })
          .catch(error => {
              console.error(error)
          })
        }
        
      },
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
          console.log(data.tableData.act_id);
        })
        .catch(error => {
          console.error('获取数据失败:', error);
        });
      },
      hideDivs(item) {
        this.isVisible = false; // 点击后设置为false，所有div将不显示
        this.clickedItem = item; // 记录被点击的div的整个对象
        this.fetchTableData();
        this.updateActUpload({ act_name: this.clickedItem.act_name });
        fetch('http://127.0.0.1:8000/api/get_notice_number/', {
          method: 'POST',
          body: JSON.stringify({
            act_id: this.clickedItem.act_id,
            act_condition: this.clickedItem.act_time,
          })
        })
        .then(res => {
          return res.json()
        })
        .then(data => {
          console.log("notice structure: ", data)
          this.accept_number = data.number.accept_number
          this.send_number = data.number.send_number
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
      },
      toChat(chatID){
        const userId = this.$route.params.id;
        const processed_chatID = chatID.replace(/-/g, '');
        const chatData = {
          userid: userId,
          roomid: processed_chatID,
        };
        this.updateChat(chatData);
            // const chatID = 8888;
        this.$router.push({
            path: `/chat/${userId}/${processed_chatID}`
        })
      },
      ...mapActions(['updateChat', 'updateActUpload']),
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
  .div-bottom-left {
  display: inline-block;
  width: 30%;
  }
  .div-bottom-right {
  display: inline-block;
  width: 70%;
  }
  </style>