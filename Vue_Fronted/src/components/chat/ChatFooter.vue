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
      <div style="display: flex; align-items: center;">
        <el-button type="primary" icon="el-icon-position" style="text-align: center;display: flex;justify-content:center;"  @click="sendMsg">发送 </el-button>
        <div style="margin-left: auto;">
          <div v-show="this.ask==='false'">
            <el-button type="primary" icon="el-icon-position"  @click="Questions">提问</el-button>
          </div>
          <div v-show="this.ask==='true' &&(this.ask_id==this.$store.state.chatroom.userId || this.my.isGuests==='true')">
            <el-button type="primary" icon="el-icon-position"  @click="EndQuestions">结束提问</el-button>
          </div>
        </div>
      </div>
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
      ask:'false',
      ask_id:'',
      my:{
        Name:'',
        isGuests:''
      }
      // chatPopover: false
    }
  },
  methods: {
    MyGuest(){
      fetch('http://127.0.0.1:8000/api/GetGuests/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            userId: this.$store.state.chatroom.userId,
            activityId:this.$store.state.chatroom.roomId
          })
        })
        .then(res => {
          return res.json()
        })
        .then(data => {
          if (data.code === '0'){
            this.my.isGuests='true'
            // console.log("chatfooter:",item.isGuests)
            // this.$emit('sendMsg', item);
            }
            else{
            this.my.isGuests='false'
            // if(this.ask==='true' && this.ask_id!= this.$store.state.chatroom.userId){
            //   alert(item.user_name+"提问中,请稍后")
            // }
          //   else{
          //     this.$emit('sendMsg', item);
          //   }
          }
          })
    },
    MyName(){
      fetch('http://127.0.0.1:8000/api/GetName/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            userId: this.$store.state.chatroom.userId
          })
        })
        .then(res => {
          return res.json()
        })
        .then(data => {
          if (data.code === '0'){
            this.my.Name=data.username
            // console.log("name:",item.user_name)
            // this.$emit('sendMsg', item);
            // this.GetGuests(item)
          }
        })
    },
    MyChat(){
      fetch('http://127.0.0.1:8000/api/GetLeader/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            activityId: this.$store.state.chatroom.roomId
          })
        })
        .then(res => {
          return res.json()
        })
        .then(data => {
          if (data.userid === this.$store.state.chatroom.userId){
            this.my.isGuests='true'
          }
        })
    },
    askrecive(obj){
      console.log("askrecive arrive")
      if(obj.type==='ask'){
        this.ask='true'
        this.ask_id=obj.user_id
      }
      else if(obj.type==='endask'){
        this.ask='false'
        this.ask_id=''
      }
    },
    sendMsg() {
      if (this.content) {
        console.log("ask:",this.ask)
        console.log("askid:",this.ask_id)
        if(this.ask==='true' && this.ask_id!= this.$store.state.chatroom.userId && this.my.isGuests==='false'){
            alert(this.my.Name+"提问中,请稍后")
            this.content = ''
        }
        else{
            let obj = {
              user_id: this.$store.state.chatroom.userId,
              chat_id: this.$store.state.chatroom.roomId,
              sysMsgType: 'text',
              data: this.content,
              user_name:this.my.Name,
              isGuests:this.my.isGuests
            }
            this.$emit('sendMsg', obj);
        }
        // this.GetName(obj)
        // console.log("coming back??")
        // this.GetGuests(obj)
      }
    },
    /**
     * 清除会话框
     */
    clearContent() {
      this.content = ''
    },
    // GetName(item){
    //     fetch('http://127.0.0.1:8000/api/GetName/', {
    //       method: 'POST',
    //       headers: {
    //         'Content-Type': 'application/json'
    //       },
    //       body: JSON.stringify({
    //         userId: item.user_id
    //       })
    //     })
    //     .then(res => {
    //       return res.json()
    //     })
    //     .then(data => {
    //       if (data.code === '0'){
    //         item.user_name=data.username
    //         console.log("name:",item.user_name)
    //         // this.$emit('sendMsg', item);
    //         this.GetGuests(item)
    //       }
    //     })
    // },
    // GetGuests(item){
    //   fetch('http://127.0.0.1:8000/api/GetGuests/', {
    //       method: 'POST',
    //       headers: {
    //         'Content-Type': 'application/json'
    //       },
    //       body: JSON.stringify({
    //         userId: item.user_id,
    //         activityId:item.chat_id
    //       })
    //     })
    //     .then(res => {
    //       return res.json()
    //     })
    //     .then(data => {
    //       if (data.code === '0'){
    //         item.isGuests='true'
    //         console.log("chatfooter:",item.isGuests)
    //         this.$emit('sendMsg', item);
    //       }
    //       else{
    //         item.isGuests='false'
    //         if(this.ask==='true' && this.ask_id!= this.$store.state.chatroom.userId){
    //           alert(item.user_name+"提问中,请稍后")
    //         }
    //         else{
    //           this.$emit('sendMsg', item);
    //         }
    //       }
    //     })
    //     console.log("arrive")
    // },
    Questions(){
      console.log("is?",this.my.isGuests)
      this.ask='true'
      this.ask_id=this.$store.state.chatroom.userId
      let obj = {
          user_id: this.$store.state.chatroom.userId,
          chat_id: this.$store.state.chatroom.roomId,
          sysMsgType: 'ask',
          data: '',
          user_name:''
        }
        this.$emit('sendMsg',obj);
    },
    EndQuestions(){
      this.ask='false'
      this.ask_id=''
      let obj = {
          user_id: this.$store.state.chatroom.userId,
          chat_id: this.$store.state.chatroom.roomId,
          sysMsgType: 'endask',
          data: '',
          user_name:''
        }
        this.$emit('sendMsg',obj);
    }

    // selectEmoji(emoji) {
    //   this.content += emoji;
    //   this.chatPopover = false;
    // }
  },
  mounted(){
    this.MyGuest()
    this.MyName()
    this.MyChat()
  }
}
</script>

<style scoped>

span .el-button {
  margin-left: 10px;
}

el-button  .el-button {
  margin-left: 8px;
}


.send-input {
  width: 100%;
}

.el-popover {
  bottom: 80px;
}
</style>
