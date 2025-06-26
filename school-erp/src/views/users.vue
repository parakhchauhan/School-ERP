<template>
  <div class="flex h-screen overflow-hidden bg-gray-100">
    <!-- Sidebar -->
    <Sidebar :isOpen="sidebarOpen" @close="sidebarOpen = false" />

    <!-- Main Content -->
    <div class="flex flex-col flex-1 w-0 md:ml-64">
      <!-- Navbar -->
      <Navbar @toggleSidebar="sidebarOpen = !sidebarOpen" />

      <!-- Page Content -->
      <main class="flex-1 overflow-y-auto p-6 pt-20">
        <!-- Header -->
        <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-6">
          <h1 class="text-3xl font-bold text-gray-800 mb-4 md:mb-0">Admins</h1>
          <button class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition duration-200">
            + Add New Admin
          </button>
        </div>

        <!-- Admins Table -->
        <div class="overflow-x-auto">
          <table class="min-w-full bg-white border border-gray-200 rounded-lg shadow">
            <thead class="bg-gray-100">
              <tr>
                <th class="py-2 px-4 text-left">ID</th>
                <th class="py-2 px-4 text-left">Name</th>
                <th class="py-2 px-4 text-left hidden md:table-cell">Email</th>
                <th class="py-2 px-4 text-left hidden md:table-cell">Contact</th>
                <th class="py-2 px-4 text-center">Actions</th>
              </tr>
            </thead>
            <tbody>
              <!-- Dummy Admin Row 1 -->
              <tr class="hover:bg-gray-50 border-t border-gray-200">
                <td class="py-2 px-4">1</td>
                <td class="py-2 px-4">Parakh Chauhan</td>
                <td class="py-2 px-4 hidden md:table-cell">parakh@example.com</td>
                <td class="py-2 px-4 hidden md:table-cell">+91 9876543210</td>
                <td class="py-2 px-4 text-center">
                  <button class="text-green-600 hover:text-green-800 mr-2">Edit</button>
                  <button class="text-red-600 hover:text-red-800">Delete</button>
                </td>
              </tr>
              <!-- Dummy Admin Row 2 -->
              <tr class="hover:bg-gray-50 border-t border-gray-200">
                <td class="py-2 px-4">2</td>
                <td class="py-2 px-4">Aarav Nanda</td>
                <td class="py-2 px-4 hidden md:table-cell">aarav.n@example.com</td>
                <td class="py-2 px-4 hidden md:table-cell">+91 9123456789</td>
                <td class="py-2 px-4 text-center">
                  <button class="text-green-600 hover:text-green-800 mr-2">Edit</button>
                  <button class="text-red-600 hover:text-red-800">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Sidebar from '../components/appSidebar.vue'
import Navbar from '../components/appNavbar.vue'

const sidebarOpen = ref(false)
</script>

<style scoped>
/* Add optional animations or transitions if you like */
</style>