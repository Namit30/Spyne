<template>
  <div class="auth-container">
    <div class="auth-background">
      <transition name="fade">
        <Loginpage v-if="isLoginpage" @login="handleLogin" />
        <Signuppage v-else @signup="handleSignup" />
      </transition>
    </div>
    <p class="toggle-link">
      <a @click="toggleForm">
        {{ isLoginpage ? "Don't have an account? Sign up" : "Already have an account? Login" }}
      </a>
    </p>
  </div>
</template>

<script>
import Loginpage from '../components/LoginPage.vue';
import Signuppage from '../components/SignupPage.vue';

export default {
  components: {
    Loginpage,
    Signuppage,
  },
  data() {
    return {
      isLoginpage: true,
    };
  },
  methods: {
    handleLogin() {
      this.$router.push('/cars');
    },
    handleSignup() {
      this.$router.push('/cars');
    },
    toggleForm() {
      this.isLoginpage = !this.isLoginpage;
    },
  },
};
</script>

<style scoped>
.auth-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background: url('@/assets/car-background.jpg') center/cover no-repeat;
}

.auth-background {
  background: rgba(255, 255, 255, 0.8);
  padding: 20px;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
  max-width: 450px;
  width: 100%;
  text-align: center;
}

.toggle-link a {
  color: #1a73e8;
  text-decoration: none;
  font-size: 14px;
  font-weight: bold;
}

.toggle-link a:hover {
  text-decoration: underline;
}
</style>
