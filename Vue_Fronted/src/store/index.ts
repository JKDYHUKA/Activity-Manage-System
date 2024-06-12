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
    }
    // userId:null,
    // roomId:null
  },
  getters: {
    getUser(state){
      return state.user
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
    }
  },
  modules: {
  }
})
