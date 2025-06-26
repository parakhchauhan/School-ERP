<template>
  <div class="flex min-h-screen items-center justify-center bg-gradient-to-br from-blue-100 to-indigo-200 p-4">
    <div class="w-full max-w-md bg-white rounded-2xl shadow-lg p-8">
      <h2 class="text-2xl font-bold text-center text-indigo-700 mb-6">Create Admin Account</h2>

      <form @submit.prevent="handleRegister" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700">Name</label>
          <input
            type="text"
            v-model="name"
            required
            placeholder="Full Name"
            class="w-full mt-1 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
          />
        </div>

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
          <label class="block text-sm font-medium text-gray-700">Contact Number</label>
          <input
            type="tel"
            v-model="contact"
            placeholder="+91XXXXXXXXXX"
            class="w-full mt-1 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
          />
        </div>

        <!-- Password Field -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Password</label>
          <input
            :type="showPassword ? 'text' : 'password'"
            v-model="password"
            required
            placeholder="Choose a secure password"
            class="w-full mt-1 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
          />
        </div>

        <!-- Confirm Password Field -->
        <div>
          <label class="block text-sm font-medium text-gray-700">Confirm Password</label>
          <input
            :type="showPassword ? 'text' : 'password'"
            v-model="confirmPassword"
            required
            placeholder="Re-enter password"
            class="w-full mt-1 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500"
          />
        </div>

        <!-- Show/Hide Toggle -->
        <div class="flex items-center mt-2">
          <input type="checkbox" id="showPassword" v-model="showPassword" class="mr-2" />
          <label for="showPassword" class="text-sm text-gray-600">Show password</label>
        </div>
        

        <button
          type="submit"
          class="w-full bg-indigo-600 hover:bg-indigo-700 text-white font-semibold py-2 rounded-lg transition"
        >
          Register Admin
        </button>
      </form>

      <p class="text-center text-sm text-gray-500 mt-6">
        Already have an account?
        <router-link to="/" class="text-indigo-600 hover:underline font-medium">Login</router-link>
      </p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'RegisterAdminPage',
  data() {
    return {
      name: '',
      email: '',
      contact: '',
      password: '',
      confirmPassword: '',
      showPassword: false,
    }

  },
  methods: {
    async handleRegister() {
      if (this.password !== this.confirmPassword) {
        alert("❌ Passwords do not match.");
        return;
      }

      const payload = {
        name: this.name,
        email: this.email,
        password: this.password,
        contact: this.contact,
      };

      try {
        await axios.post("http://localhost:8000/api/register", payload);
        alert("✅ Admin registered successfully!");
        this.$router.push("/"); // Or wherever your login page lives
      } catch (error) {
        console.error("Registration error:", error.response?.data || error.message);
        alert("❌ Failed to register admin. Please check console.");
      }
    },
  },
}
</script>