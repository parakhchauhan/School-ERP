<template>
  <header class="fixed top-0 left-0 w-full md:ml-64 md:w-[calc(100%-16rem)] h-16 bg-white border-b border-gray-200 flex items-center justify-between px-4 shadow z-40">
    <div class="flex items-center space-x-4">
      <!-- Hamburger Menu (visible on mobile) -->
      <button class="md:hidden" @click="$emit('toggleSidebar')">
        <svg class="w-6 h-6 text-gray-700 transition-transform transform hover:rotate-90" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"/>
        </svg>
      </button>
      <span class="text-lg font-semibold text-gray-800">School ERP</span>
    </div>
    <button
  @click="handleLogout"
  class="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600 transition duration-200"
>
  Logout
</button>
  </header>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

defineEmits(['toggleSidebar'])

const username = ref('')
const router = useRouter()

onMounted(() => {
  username.value = localStorage.getItem('username') || 'User'
})

function handleLogout() {
  localStorage.removeItem('token')
  localStorage.removeItem('username')
  router.push('/')
}
</script>