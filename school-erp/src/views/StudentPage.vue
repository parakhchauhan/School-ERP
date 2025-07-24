<template>
  <div class="flex h-screen overflow-hidden bg-gray-100">
    <!-- Sidebar Component -->
    <Sidebar :isOpen="sidebarOpen" @close="sidebarOpen = false" />

    <!-- Main Content Area (adjusts for sidebar on desktop) -->
    <div class="flex flex-col flex-1 w-0 md:ml-64">
      <!-- Navbar with mobile sidebar toggle -->
      <Navbar @toggleSidebar="sidebarOpen = !sidebarOpen" />

      <!-- Page Content -->
      <main class="flex-1 overflow-y-auto p-6 pt-20">
        <!-- Header & Add New Student Button -->
        <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-6">
          <h1 class="text-3xl font-bold text-gray-800 mb-4 md:mb-0">Students</h1>
          <RouterLink
            to="/RegisterStudentPage"
            class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition duration-200" >
            + Add New Student
          </RouterLink>
        </div>

        <!-- Students Table -->
        <div class="overflow-x-auto">
          <div class="ag-theme-alpine bg-white rounded-lg shadow p-2" style="height: 50%; width: 100%;">
          <AgGridVue
              :rowData="students"
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
import axios from 'axios'
import Sidebar from '../components/appSidebar.vue'
import Navbar from '../components/appNavbar.vue'
import { AgGridVue } from 'ag-grid-vue3'


const columnDefs = [
  { headerName: 'ID', field: 'id', sortable: true, filter: true },
  {
    headerName: 'Name',
    valueGetter: params => `${params.data.first_name} ${params.data.last_name}`,
    sortable: true,
    filter: true
  },
  { headerName: 'DOB', field: 'dob', sortable: true, filter: true },
  { headerName: 'Gender', field: 'gender', sortable: true, filter: true },
  { headerName: 'Nationality', field: 'nationality', sortable: true, filter: true },
  { headerName: 'Aadhar', field: 'aadhar_no', sortable: true, filter: true },
  { headerName: 'Blood Group', field: 'blood_group', sortable: true, filter: true },
  { headerName: 'Father', field: 'guardian.father_name', sortable: true, filter: true },
  { headerName: 'Mother', field: 'guardian.mother_name', sortable: true, filter: true },
  { headerName: 'Father Phone', field: 'guardian.father_phone', sortable: true, filter: true },
  { headerName: 'Roll No', field: 'academic.roll_number', sortable: true, filter: true },
  { headerName: 'Class', field: 'academic.class_name', sortable: true, filter: true },
  { headerName: 'Section', field: 'academic.section', sortable: true, filter: true },
  { headerName: 'Status', field: 'status', sortable: true, filter: true },

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



const sidebarOpen = ref(false)
const students = ref([])

onMounted(async () => {
  try {
    const res = await axios.get('http://localhost:8000/api/students')
    students.value = res.data.students
  } catch (err) {
    console.error('Failed to fetch students:', err)
  }
})
</script>

<style scoped>
/* Optional custom styles can be added here */
</style>