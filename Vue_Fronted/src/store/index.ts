import { createStore } from 'vuex'

// 定义Message接口
interface Message {
  id: string;
  content: string;
  timestamp: string;
}

// 定义State接口
interface State {
  user: {
    userId: string;
    username: string;
    nickname: string;
    email: string;
    phone_number: string;
  };
  chatroom: {
    userId: string | null;
    roomId: string | null;
  };
  messages: Message[];
  act_upload: {
    act_name: string
  };
}

export default createStore<State>({
  state: {
    user: {
      userId: "",
      username: "",
      nickname: "",
      email: "",
      phone_number: "",
    },
    chatroom: {
      userId: null,
      roomId: null
    },
    messages: [],
    act_upload: {
      act_name: ""
    },
  },
  getters: {
    getUser(state) {
      return state.user;
    },
    getUsername(state) {
      return state.user.username;
    },
    getUserId(state) {
      return state.user.userId;
    },
    getActLoad(state){
      return state.act_upload.act_name;
    }
  },
  mutations: {
    setUser(state, userData) {
      state.user = userData;
    },
    setRoom(state, data) {
      state.chatroom.userId = data.userid;
      state.chatroom.roomId = data.roomid;
    },
    addMessage(state, mes: Message) { // 指定 mes 的类型
      state.messages.push(mes);
    },
    setActName(state, act_name) {
      state.act_upload.act_name = act_name
    },
    clearUser(state) {
      state.user = {
        userId: "",
        username: "",
        nickname: "",
        email: "",
        phone_number: "",
      }
    },
    clearMsg(state) {
      state.messages = []
    },
  },
  actions: {
    updateUser({ commit }, userData) {
      commit('setUser', userData);
      console.log("update user")
    },
    updateChat({ commit }, chatData) {
      commit('setRoom', chatData);
    },
    updateActUpload({ commit }, actData){
      commit('setActName', actData);
    },
    clearUserData({ commit }) {
      commit('clearUser');
      console.log("clear user")
    },
    clearMsgList({ commit }) {
      commit('clearMsg')
    }
  },
  modules: {
  }
});
