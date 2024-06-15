import { createStore } from 'vuex'


export default createStore({
  state: {
    user: {
      userId: "",
      username: "",
      nickname: "",
      email: "",
      phone_number: "",
    },
    chatroom:{
      userId:null,
      roomId:null
    },
    act_upload:{
      act_name:"",//用于在文件上传时的数据共享
    },
    
    // userId:null,
    // roomId:null
  },
  getters: {
    getUser(state){
      return state.user
    },
    getUsername(state) {
      return state.user.username;
    },
    getUserId(state){
      return state.user.userId;
    },
    getActLoad(state){
      return state.act_upload.act_name;
    }
  },
  mutations: {
    setUser(state, userData){
      state.user = userData;
    },
    setRoom(state,data){
      state.chatroom.userId=data.userid;
      state.chatroom.roomId=data.roomid;
    },
    setActUpload(state, actData){
      state.act_upload = actData;
    },
    // serUserId(state,data){
    //   state.userId=data;
    // },
    // setRoomId(state,data){
    //   state.roomId=data;
    // }
  },
  actions: {
    updateUser({ commit }, userData){
      commit('setUser', userData);
    },
    updateChat({ commit }, chatData){
      commit('setRoom', chatData);
    },
    updateActUpload({ commit }, actData){
      commit('setActUpload', actData);
    }
  },
  modules: {
  }
})
