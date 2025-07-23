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
        <div class="ag-theme-alpine bg-white rounded-lg shadow p-2" style="height: 600px;">
          <AgGridVue
              :rowData="adminList"
              :columnDefs="columnDefs"
              :gridOptions="gridOptions"
              :domLayout="'autoHeight'"
              :theme="'legacy'"
            >
            </AgGridVue>
        </div>
      </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from '../utils/axios.js'
import Sidebar from '../components/appSidebar.vue'
import Navbar from '../components/appNavbar.vue'

import { AgGridVue } from "ag-grid-vue3"; // Vue Data Grid Component

const columnDefs = [
  { headerName: 'ID', field: 'id', sortable: true, filter: true },
  { headerName: 'Name', field: 'name', sortable: true, filter: true },
  { headerName: 'Email', field: 'email', sortable: true, filter: true },
  { headerName: 'Contact', field: 'contact', sortable: true, filter: true },
  {
    headerName: 'Actions',
    field: 'actions',
    cellRenderer: params => {
      return `
        <button class='text-green-600 mr-2 hover:text-green-800'>Edit</button>
        <button class='text-red-600 hover:text-red-800'>Delete</button>
      `
    },
  },
]

const gridOptions = {
  defaultColDef: {
    flex: 1,
    minWidth: 100,
    resizable: true,
  },
}

const components = { AgGridVue }


const sidebarOpen = ref(false)
const adminList = ref([])



onMounted(async () => {
  try {
    const response = await axios.get('/admins')
    adminList.value = response.data
  } catch (error) {
    console.error('Failed to fetch admins:', error)
  }
})
</script>

<style>
/* Add optional animations or transitions if you like */
</style>