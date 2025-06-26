<template>
  <div class="flex min-h-screen items-center justify-center bg-gradient-to-br from-blue-100 to-indigo-200 p-4">
    <div class="w-full max-w-md bg-white rounded-2xl shadow-lg p-8">
      <h2 class="text-2xl font-bold text-center text-indigo-700 mb-6">Login to Your Account</h2>

      <form @submit.prevent="handleLogin" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700">Email</label>
          <input
            type="email"
            v-model="email"
            required
            placeholder="you@example.com"
            class="w-full mt-1 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
          />
        </div>

        <div>
          <label class="block text-sm font-medium text-gray-700">Password</label>
          <input
            :type="showPassword ? 'text' : 'password'"
            v-model="password"
            required
            placeholder="Enter your password"
            class="w-full mt-1 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
          />
          <div class="flex items-center mt-2">
            <input type="checkbox" id="showPassword" v-model="showPassword" class="mr-2" />
            <label for="showPassword" class="text-sm text-gray-600">Show password</label>
          </div>
        </div>

        <div class="text-right">
          <router-link to="/ForgetPassword" class="text-sm text-indigo-600 hover:underline">Forgot password?</router-link>
        </div>

        <button
          type="submit"
          class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-2 rounded-lg transition"
        >
          Login
        </button>
      </form>

      <p class="text-center text-sm text-gray-500 mt-6">
        Don’t have an account?
        <router-link to="/RegisterAdminPage" class="text-indigo-600 hover:underline font-medium">Register</router-link>
      </p>
    </div>
  </div>
</template>

<script>
import axios from '../utils/axios.js'  // we'll create this

export default {
  name: 'LoginPage',
  data() {
    return {
      email: '',
      password: '',
      showPassword: false,
    }
  },
  methods: {
    async handleLogin() {
      try {
        const response = await axios.post('/login', {
          email: this.email,
          password: this.password,
        })
        const token = response.data.access_token
        localStorage.setItem('token', token)

        const user = await axios.get('/me') // ✅ Ensure /me works with token
        localStorage.setItem('username', user.data.name)
        console.log('👋 Username from localStorage:', localStorage.getItem('username'))

        this.$router.push('/dashboard') // ✅ Now redirect!
      } catch (error) {
        console.error('Login error:', error)
        alert('❌ Invalid credentials.')
      }
    },
  },
}
</script>
