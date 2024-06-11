<template>
  <div class="chat-container">
    <el-row :gutter="10">
      <el-col :span="8" class="col-container">
   
        <div class="left-msg">
          <el-button type="primary" @click="initServer(this.$route.params.chatid,this.$route.params.id)">test</el-button>
        </div>
      </el-col>
      <el-col :span="8">
        <el-container>
          <el-main class="main">
            <chat-main ChatMain ref="ChatMain" @initServer="test()"></chat-main>
          </el-main>
          <el-footer class="footer">
            <chat-footer ref="ChatFooter" @sendMsg="sendMsg"></chat-footer>
          </el-footer>
        </el-container>
      </el-col>
      <el-col :span="8" class="col-container">
        <!--右侧用户列表-->
        <!-- <div class="right-msg">
          <user-list ref="userList"></user-list>
        </div> -->
      </el-col>
    </el-row>
  </div>
</template>

  
<script>
  // import { } from "@/components/axios_api/api.js"; // @符号指的是src路径
//   import MChat from "@maybecode/m-chat";
import ChatMain from "../components/chat/ChatMain.vue";
import ChatFooter from "../components/chat/ChatFooter.vue";
// import SysMeg from "../components/SysMsg.vue";
import UserList from "../components/chat/UserList.vue";
import {socket} from "@/utils/socket"
import { ElMessage } from "element-plus";
import {ref} from 'vue';
import { createRouter, createWebHistory } from 'vue-router';

export default {
  name: "chatIndex",
  components: {
    ChatMain,
    ChatFooter,
    UserList
  },
  data() {
    return {
      globalData:{
        user_id: this.$route.params.id,
      },
      ws: null,  
      send_data: "",
      chat_id: null,
      send_chat: false,
      add_chat: true,
      messages: [],
      open_extends: ["image"],
    }
  },
  methods: {
    /**
     * 连接服务器
     */
    test(){
      console.log(this.$route.params.chatid)
    },


    initServer(roomId, userId) {
      const data={
        userid:this.$route.params.id,
        roomid:this.$route.params.chatid
      }
      var user_id=this.$route.params.id;

      let that=this;
      console.log("init-start")
      const wsuri = "ws://127.0.0.1:8000";
      const ws_on_line = `${wsuri}/ws/chat/${roomId}/`;
       socket.ws_url =  ws_on_line;
       socket.chat_id=data.roomid;
       socket.user_id=data.userid;
       console.log(socket.user_id);
      // 设置连接成功时回调
      socket.successCallBack = () => {
        this.$message.success('连接成功')
        this.$store.commit('setRoom',data)
        // 获取 房间所有人
        // setTimeout(() => {
        //   this.getRoomList()
        // }, 1000);
      }
      // 重写Socket中的消息接收方法
      socket.receive = (msg) => {
        msg = JSON.parse(msg.data);
        // if (msg.sysMsgType === 'join') {
        //   this.$refs.sysMsg.pushSysMsg(msg);
        //   this.$refs.userList.pushUserList(msg.data)
        // }
        // if (msg.sysMsgType === 'leave') {
        //   this.$refs.sysMsg.pushSysMsg(msg);
        //   this.$refs.userList.removeUserList(msg.data)
        // }
        // if (msg.sysMsgType === 'roomList') {
        //   this.$refs.userList.loadUserList(msg.data)
        // }
        if (msg.sysMsgType === 'join') {
          console.log("add room")
        }
        if (msg.sysMsgType === 'text') {
          let data = {
            type: 'other',
            content: msg.data,
            user_id : msg.user_id,
            isMy:''
          }
          this.$refs.ChatMain.pushMsg(data,this.$route.params.id);
        }
      };
      // 开始建立连接
      socket.init();
    },
    /**
     * 发送消息 会将消息展示在页面上
     */
    sendMsg(obj) {
      socket.send(obj, () => {
        let msgObj = {content: obj.data, type: 'my',user_id:this.$route.params.id,isMy:''}
        this.$refs.ChatMain.pushMsg(msgObj,this.$route.params.id);
        this.$refs.ChatFooter.clearContent();
      }, error => {
        console.log(error);
        this.$message.error('socket 出现未知异常,请查看控制台')
      });
    },
    /**
     * 获取房间人列表
     */
    // getRoomList() {
    //   var msgObj = {
    //     sysMsgType: 'roomList',
    //     sender: this.$store.state.chatroom.userId,
    //     roomId: this.$store.state.chatroom.roomId
    //   }
    //   socket.send(msgObj);
    // }
  },
  mounted(){
    this.initServer(this.$route.params.chatid,this.$route.params.id)
  }
}
</script>

<style scoped>
.el-container {
  width: 100%;
  margin: 0 auto;
}

.chat-container {
  width: 100%;
  background-color: #a8c3ee;
  border-radius: 10px;
  opacity: 0.8;
}

.left-msg, .right-msg {
  margin-top: 5px;
}

.right-msg {
  padding-right: 20px !important;
}

.col-container {
  padding-top: 5px;
  padding-left: 20px !important;
}

.main {
  margin-top: 5px;
  padding: 5px;
}

.footer {
  padding: 5px;
}
</style>
