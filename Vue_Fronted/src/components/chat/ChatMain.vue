<template>
  <div class="chat-main scroller" id="scrollbar">
    <div class="main-top">
      <span>
          <!-- <el-avatar :src="require('@/assets/wx.png')"></el-avatar> -->
          <span>房间号</span>
      </span>
      <span style="float: right;line-height: 50px">
        <!-- <el-dropdown trigger="click" @command="handleCommand">
          <span class="el-dropdown-link">
            <i class="el-icon-more" style="font-size: 25px;cursor: pointer;margin-right: 5px"></i>
          </span>
          <template #dropdown>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item icon="el-icon-s-promotion" command="join">加入房间</el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown> -->
        <!-- <el-button type="primary" @click="initServer()">加入房间</el-button> -->
      </span>
    </div>
    <!--消息列表-->
    <div>
      <div class="msg-list" v-for="(item,value) in msgList" :key="value">
        <div v-show="item.type === 'other' && item.isMy === 'false'" class="other chat-box">
          <!-- <el-avatar size="medium" :src="require('@/assets/wx.png')" class="left-head-img"></el-avatar> -->
          <!--文本消息-->
          <div class="other-msg">
            <!--文本消息-->
            <div>{{ item.content }}</div>
          </div>
        </div>
        <div v-show="item.type === 'my'" class="my chat-box">
          <div class="my-msg">
            <!--文本消息-->
            <div>{{ item.content }}</div>
          </div>
          <!-- <el-avatar size="medium" :src="require('@/assets/head.png')" class="right-head-img"></el-avatar> -->
        </div>
      </div>
    </div>
    <!-- 加入房间弹窗-->
    <!-- <join-room-dialog ref="joinRoomDialog" @initServer="initServer"></join-room-dialog> -->
  </div>
</template>


<script>
  export default {
    name: "ChatMain",
    // components: {JoinRoomDialog},
    data() {
      return {
        msgList: [],
      }
    },
    methods: {
      /**
       * 新增消息
       * @param item
       */
      pushMsg(item,myId) {
        if(item.user_id==myId){
          item.isMy='true'
        }
        else{
          item.isMy='false'
        }
        this.msgList.push(item);
        this.keepInBottom();
        console.log(item.user_id)
        console.log(item.isMy)
      },
      /**
       * 内容永远保持在底部
       */
      keepInBottom() {
        this.$nextTick(() => {
          var div = document.getElementById('scrollbar');
          div.scrollTop = div.scrollHeight - div.clientHeight;
        })
      },
      /**
       * 建立连接
       * @param roomId
       * @param userId
       */
      initServer() {
        console.log("init")
      },
      /**
       * 对应事件
       * @param command
       */
      // handleCommand(command) {
      //   if (command === 'join') {
      //     this.$refs.joinRoomDialog.dialogVisible = true;
      //   }
        // if (command === 'create') {
        //   this.$refs.createRoomDialog.dialogVisible = true;
        // }
      // }
    }
  }
  </script>

<style scoped>

  .chat-main {
    overflow: auto;
    height: calc(100vh - 95px);
    background-color: white;
    border-radius: 5px;
  }

  .right-head-img {
    position: relative;
    top: 5px;
    float: right;
  }

  .left-head-img {
    position: relative;
    top: 42px;
  }

  .other {
    padding: 0px 5px;
    margin: 0 10px;
    text-align: left;
  }

  .other-msg, .my-msg {
    font-size: 12px;
    margin-left: 40px;
    vertical-align: middle;
    background-color: #eff3f6;
    max-width: 80%;
    /*宽度内容自适应*/
    width: -webkit-fit-content;
    padding: 15px 15px;
    border-radius: 5px;
    /*文本自动换行*/
    word-break: break-all;
    display: inline-block;
    box-shadow: 0 2px 4px 0 rgb(207 209 211);
  }

  .msg-img {
    height: 100px;
    width: 100px;
  }

  .msg-video {
    width: 300px;
    height: 200px;
  }

  .my-msg {
    background-color: #6CA1FA;
    color: white;
    text-align: left;
    margin-right: 5px;
  }

  .my {
    text-align: right;
    padding: 10px 5px;
    margin: 0 10px;
  }

  .chat-box {
    position: relative;
  }

  .el-avatar {
    display: block;
    background: #ffffff;
  }

  .main-top {
    padding: 5px;
    height: 50px;
    border-bottom: 1px solid #eff3f6;
  }

  .main-top span {
    float: left;
    line-height: 40px;
    margin-left: 5px;
  }


  .scroller::-webkit-scrollbar {
    width: 8px;
    height: 8px;
  }

  .scroller::-webkit-scrollbar-track {
    background-color: transparent;
    -webkit-border-radius: 2em;
    -moz-border-radius: 2em;
    border-radius: 2em;
  }

  .scroller::-webkit-scrollbar-thumb {
    background-color: rgb(147, 147, 153, 0.5);
    -webkit-border-radius: 2em;
    -moz-border-radius: 2em;
    border-radius: 2em;
  }

</style>
