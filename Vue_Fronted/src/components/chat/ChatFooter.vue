<template>
  <div class="chat-footer">
    <el-row>
      <el-col :span="20">
        <el-input v-model="content" placeholder="请输入发送内容" @keyup.enter.native="sendMsg" class="send-input"></el-input>
      </el-col>
      <el-col :span="4">
         <span>
        <!-- <el-popover
            ref="popover5"
            placement="top-start"
            width="370"
            v-model="chatPopover"
            trigger="manual"
        >
      <p>
        <chat-emoji @selectEmoji="selectEmoji"></chat-emoji>
      </p>
       <el-button type="primary" icon="el-icon-lightning" circle slot="reference" @click="chatPopover = !chatPopover"></el-button>
      </el-popover> -->

      <el-button type="primary" icon="el-icon-position" circle @click="sendMsg">发送</el-button>
    </span>
      </el-col>
    </el-row>
  </div>
</template>

<script>
// import ChatEmoji from "@/compoents/emoji/ChatEmoji";

export default {
  name: "ChatFooter",
  // components: {
  //   ChatEmoji
  // },
  data() {
    return {
      content: '',
      // chatPopover: false
    }
  },
  methods: {
    sendMsg() {
      if (this.content) {
        let obj = {
          user_id: this.$store.state.chatroom.userId,
          chat_id: this.$store.state.chatroom.roomId,
          sysMsgType: 'text',
          data: this.content
        }
        this.$emit('sendMsg', obj);
      }
    },
    /**
     * 清除会话框
     */
    clearContent() {
      this.content = ''
    }
    // selectEmoji(emoji) {
    //   this.content += emoji;
    //   this.chatPopover = false;
    // }
  }
}
</script>

<style scoped>

span .el-button {
  margin-left: 10px;
}

.send-input {
  width: 100%;
}

.el-popover {
  bottom: 80px;
}
</style>
