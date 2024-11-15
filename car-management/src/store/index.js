import Vue from 'vue';
import Vuex from 'vuex';
import api from '../api';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    token: localStorage.getItem('token') || '',
    user: {},
    cars: [],
  },
  mutations: {
    SET_TOKEN(state, token) {
      state.token = token;
      localStorage.setItem('token', token);
    },
    SET_USER(state, user) {
      state.user = user;
    },
    SET_CARS(state, cars) {
      state.cars = cars;
    },
    CLEAR_TOKEN(state) {
      state.token = '';
      localStorage.removeItem('token');
    },
  },
  actions: {
    async login({ commit }, credentials) {
      try {
        const response = await api.post('/login', credentials);
        commit('SET_TOKEN', response.data.access_token);
        commit('SET_USER', response.data.user);  // Assuming the user data is returned
      } catch (error) {
        console.error('Login error:', error);
        throw new Error('Login failed');
      }
    },
    async signup(_, credentials) {
      try {
        await api.post('/signup', credentials);
      } catch (error) {
        console.error('Signup error:', error);
        throw new Error('Signup failed');
      }
    },
    async fetchCars({ commit }) {
      try {
        const response = await api.get('/cars');
        commit('SET_CARS', response.data);
      } catch (error) {
        console.error('Error fetching cars:', error);
      }
    },
    async addCar({ dispatch }, carData) {
      try {
        await api.post('/cars', carData);
        dispatch('fetchCars');
      } catch (error) {
        console.error('Error adding car:', error);
      }
    },
    async updateCar({ dispatch }, { id, carData }) {
      try {
        await api.put(`/cars/${id}`, carData);
        dispatch('fetchCars');
      } catch (error) {
        console.error('Error updating car:', error);
      }
    },
    async deleteCar({ dispatch }, id) {
      try {
        await api.delete(`/cars/${id}`);
        dispatch('fetchCars');
      } catch (error) {
        console.error('Error deleting car:', error);
      }
    },
    logout({ commit }) {
      commit('CLEAR_TOKEN');
      commit('SET_USER', {});  // Clear user data
    },
  },
});
