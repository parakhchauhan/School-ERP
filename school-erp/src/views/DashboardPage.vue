<script setup>
import { ref } from 'vue'
import Sidebar from '../components/appSidebar.vue'
import Navbar from '../components/appNavbar.vue'
import Card from '../components/Card.vue'

const sidebarOpen = ref(false)
</script>

<template>
  <div class="flex h-screen overflow-hidden bg-gray-100">
    <!-- Sidebar with mobile toggle -->
    <Sidebar :isOpen="sidebarOpen" @close="sidebarOpen = false" />

    <!-- Main content area adjusts if sidebar is visible (desktop) -->
    <div class="flex flex-col flex-1 w-0 md:ml-64">
      <!-- Sticky navbar with hamburger toggle on mobile -->
      <Navbar @toggleSidebar="sidebarOpen = !sidebarOpen" />

      <!-- Page content -->
      <main class="flex-1 overflow-y-auto p-6 pt-20">
        <h1 class="text-3xl font-bold mb-6 text-gray-800">Dashboard</h1>
        
        <!-- Stat Cards in a responsive grid -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
          <Card title="Total Students" value="450" />
          <Card title="Teachers" value="38" />
          <Card title="Monthly Revenue" value="₹1.2L" />
          <Card title="Upcoming Events" value="5" />
        </div>
        
        <!-- Chart/Cards Area with subtle hover effects -->
        <div class="bg-white shadow rounded-lg p-6 transition-all duration-300 hover:shadow-xl">
          <h2 class="text-xl font-semibold text-gray-700 mb-4">Enrollment Trends</h2>
          <div class="h-64 flex items-center justify-center text-gray-400">
            [ Chart Placeholder ]
          </div>
        </div>
      </main>
    </div>
  </div>
</template>