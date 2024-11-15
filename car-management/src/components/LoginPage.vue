<template>
  <div class="page-container">
    <div class="auth-form">
      <h2>Login to Drive</h2>
      <form @submit.prevent="handleLogin">
        <div>
          <label for="email">Email</label>
          <input
            id="email"
            type="email"
            v-model="email"
            placeholder="Email"
            required
            :class="{ 'input-error': emailError }"
          />
          <p v-if="emailError" class="error-message">Please enter a valid email.</p>
        </div>
        
        <div>
          <label for="password">Password</label>
          <input
            id="password"
            type="password"
            v-model="password"
            placeholder="Password"
            required
            :class="{ 'input-error': passwordError }"
          />
          <p v-if="passwordError" class="error-message">Password is required.</p>
        </div>

        <button type="submit" :disabled="isLoading">Login</button>
        
        <div v-if="isLoading" class="loading-spinner">Starting your engine...</div>
      </form>

      <p>Don't have an account? <router-link to="/signup">Sign up now!</router-link></p>

      <p v-if="loginError" class="error-message">{{ loginError }}</p>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: '',
      emailError: false,
      passwordError: false,
      isLoading: false,
      loginError: '',
    };
  },
  methods: {
    async handleLogin() {
      this.emailError = !this.isValidEmail(this.email);
      this.passwordError = !this.password;

      if (this.emailError || this.passwordError) {
        return;
      }

      this.isLoading = true;
      try {
        await this.$store.dispatch('login', { email: this.email, password: this.password });
        this.$router.push('/cars');
      } catch (error) {
        this.loginError = 'Login failed. Please try again.';
      } finally {
        this.isLoading = false;
      }
    },
    isValidEmail(email) {
      const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
      return emailPattern.test(email);
    },
  },
};
</script>

<style>
body {
  background: url('@/assets/car-background.jpg') no-repeat center center fixed;
  background-size: cover;
  height: 100vh;
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

.auth-form {
  max-width: 400px;
  background: rgba(255, 255, 255, 0.9);
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
  text-align: left;
}

h2 {
  text-align: center;
  color: #1a73e8;
  margin-bottom: 20px;
}

label {
  font-weight: bold;
  color: #333;
}

input {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  margin-bottom: 15px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  width: 100%;
  padding: 10px;
  color: #fff;
  background: #1a73e8;
  border: none;
  border-radius: 4px;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background: #1558b1;
}

.input-error {
  border-color: red;
}

.error-message {
  color: red;
  font-size: 12px;
}

.loading-spinner {
  margin-top: 10px;
  font-size: 14px;
  color: #666;
}
</style>
