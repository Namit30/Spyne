<template>
  <div class="auth-form">
    <h2>Sign Up and Start Your Journey</h2>
    <form @submit.prevent="handleSignup">
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
        <p v-if="passwordError" class="error-message">Password must be at least 6 characters long.</p>
      </div>

      <div>
        <label for="confirmPassword">Confirm Password</label>
        <input
          id="confirmPassword"
          type="password"
          v-model="confirmPassword"
          placeholder="Confirm Password"
          required
          :class="{ 'input-error': confirmPasswordError }"
        />
        <p v-if="confirmPasswordError" class="error-message">Passwords do not match.</p>
      </div>

      <button type="submit" :disabled="isLoading">Sign Up</button>

      <div v-if="isLoading" class="loading-spinner">Creating your account...</div>
    </form>

    <p>Already have an account? <router-link to="/">Login here</router-link></p>

    <p v-if="signupError" class="error-message">{{ signupError }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: '',
      confirmPassword: '',
      emailError: false,
      passwordError: false,
      confirmPasswordError: false,
      isLoading: false,
      signupError: '',
    };
  },
  methods: {
    async handleSignup() {
      this.emailError = false;
      this.passwordError = false;
      this.confirmPasswordError = false;
      this.signupError = '';

      if (!this.isValidEmail(this.email)) {
        this.emailError = true;
        return;
      }

      if (this.password.length < 6) {
        this.passwordError = true;
        return;
      }

      if (this.password !== this.confirmPassword) {
        this.confirmPasswordError = true;
        return;
      }

      this.isLoading = true;

      try {
        await this.$store.dispatch('signup', { email: this.email, password: this.password });
        this.$router.push('/');
      } catch (error) {
        this.signupError = 'Sign-up failed. Please try again.';
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

<style scoped>
/* Same as LoginPage */
</style>
