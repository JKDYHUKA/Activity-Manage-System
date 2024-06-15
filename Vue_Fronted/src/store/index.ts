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
    messages: []
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
    }
  },
  actions: {
    updateUser({ commit }, userData) {
      commit('setUser', userData);
    },
    updateChat({ commit }, chatData) {
      commit('setRoom', chatData);
    }
  },
  modules: {
  }
});
