import Vue from 'vue';
import Router from 'vue-router';
import LoginPage from '../components/LoginPage.vue';
import SignupPage from '../components/SignupPage.vue';
import CarManagement from '../views/CarManagement.vue';

Vue.use(Router);

export default new Router({
  mode: 'history', // Enables clean URLs without the hash #
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: LoginPage,
    },
    {
      path: '/signup',
      name: 'Signup',
      component: SignupPage,
    },
    {
      path: '/cars',
      name: 'CarManagement',
      component: CarManagement,
    },
    {
      path: '*',
      redirect: '/login', // Redirects any undefined route to login
    },
  ],
});
