<template>
  <div class="flex min-h-screen items-center justify-center bg-gradient-to-br from-blue-100 to-indigo-200 p-4">
    <div class="w-full max-w-md bg-white rounded-2xl shadow-lg p-8">
      <h2 class="text-2xl font-bold text-center text-indigo-700 mb-6">Reset Your Password</h2>

      <form @submit.prevent="handleReset" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700">Email Address</label>
          <input
            type="email"
            v-model="email"
            required
            placeholder="you@example.com"
            class="w-full mt-1 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
          />
        </div>

        <p class="text-sm text-gray-500">
          We'll send a password reset link to your email if it's linked to an account.
        </p>

        <button
          type="submit"
          class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-2 rounded-lg transition"
        >
          Send Reset Link
        </button>
      </form>

      <p class="text-center text-sm text-gray-500 mt-6">
        Back to
        <router-link to="/" class="text-indigo-600 hover:underline font-medium">Login</router-link>
      </p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ForgetPasswordPage',
  data() {
    return {
      email: ''
    }
  },
  methods: {
    async handleReset() {
      try {
        // Replace this endpoint with your actual FastAPI forgot-password route
        await axios.post('http://localhost:8000/api/forgot-password', { email: this.email })
        alert('📩 If an account exists, a reset link has been sent.')
      } catch (error) {
        console.error('Reset error:', error)
        alert('Something went wrong. Please try again later.')
      }
    }
  }
}
</script>