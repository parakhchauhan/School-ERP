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
            class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition duration-200"
          >
            + Add New Student
          </RouterLink>
        </div>

        <!-- Students Table -->
        <div class="overflow-x-auto">
          <table class="min-w-full bg-white border border-gray-200 rounded-lg shadow text-sm">
  <thead class="bg-gray-100 text-left">
    <tr>
      <th class="py-2 px-3">ID</th>
      <th class="py-2 px-3">Name</th>
      <th class="py-2 px-3">DOB</th>
      <th class="py-2 px-3">Gender</th>
      <th class="py-2 px-3">Nationality</th>
      <th class="py-2 px-3">Aadhar</th>
      <th class="py-2 px-3">Blood Group</th>
      <th class="py-2 px-3">Father</th>
      <th class="py-2 px-3">Mother</th>
      <th class="py-2 px-3">Father Phone</th>
      <th class="py-2 px-3">Roll No</th>
      <th class="py-2 px-3">Class</th>
      <th class="py-2 px-3">Section</th>
      <th class="py-2 px-3">Status</th>
      <th class="py-2 px-3 text-center">Actions</th>
    </tr>
  </thead>
  <tbody>
    <tr
      v-for="student in students"
      :key="student.id"
      class="hover:bg-gray-50 border-t border-gray-200"
    >
      <td class="py-2 px-3">{{ student.id }}</td>
      <td class="py-2 px-3">{{ student.first_name }} {{ student.last_name }}</td>
      <td class="py-2 px-3">{{ student.dob }}</td>
      <td class="py-2 px-3">{{ student.gender }}</td>
      <td class="py-2 px-3">{{ student.nationality }}</td>
      <td class="py-2 px-3">{{ student.aadhar_no }}</td>
      <td class="py-2 px-3">{{ student.blood_group }}</td>
      <td class="py-2 px-3">{{ student.guardian?.father_name }}</td>
      <td class="py-2 px-3">{{ student.guardian?.mother_name }}</td>
      <td class="py-2 px-3">{{ student.guardian?.father_phone }}</td>
      <td class="py-2 px-3">{{ student.academic?.roll_number }}</td>
      <td class="py-2 px-3">{{ student.academic?.class_name }}</td>
      <td class="py-2 px-3">{{ student.academic?.section }}</td>
      <td class="py-2 px-3">{{ student.status }}</td>
      <td class="py-2 px-3 text-center whitespace-nowrap">
        <button class="text-green-600 hover:text-green-800 mr-2">Edit</button>
        <button class="text-red-600 hover:text-red-800">Delete</button>
      </td>
    </tr>
    <tr v-if="students.length === 0">
      <td colspan="15" class="text-center py-4">No Students Found</td>
    </tr>
  </tbody>
</table>
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