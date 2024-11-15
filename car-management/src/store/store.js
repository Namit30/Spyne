import { createStore } from 'vue';

const store = createStore({
  state() {
    return {
      token: localStorage.getItem('token') || null, // Stores token from localStorage
      user: JSON.parse(localStorage.getItem('user')) || {}, // Stores user info from localStorage
    };
  },
  mutations: {
    setToken(state, token) {
      state.token = token;
      localStorage.setItem('token', token); // Persist token in localStorage
    },
    removeToken(state) {
      state.token = null;
      state.user = {}; // Clear user data on logout
      localStorage.removeItem('token'); // Remove token from localStorage
      localStorage.removeItem('user'); // Remove user data from localStorage
    },
    setUser(state, user) {
      state.user = user;
      localStorage.setItem('user', JSON.stringify(user)); // Persist user info
    },
  },
  actions: {
    login({ commit }, { token, user }) {
      commit('setToken', token);
      commit('setUser', user); // Store user info on successful login
    },
    logout({ commit }) {
      commit('removeToken');
    },
  },
});

export default store;
