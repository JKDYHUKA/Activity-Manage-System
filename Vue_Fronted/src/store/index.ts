import { createStore } from 'vuex'


export default createStore({
  state: {
    user: {
      userId: "",
      username: "",
      nickname: "",
      email: "",
      phone_number: "",
    }
  },
  getters: {
    getUser(state){
      return state.user
    }
  },
  mutations: {
    setUser(state, userData){
      state.user = userData;
    }
  },
  actions: {
    updateUser({ commit }, userData){
      commit('setUser', userData);
    }
  },
  modules: {
  }
})
