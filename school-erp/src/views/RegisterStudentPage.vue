<template>
  <div class="flex h-screen overflow-hidden bg-gray-100">
    <!-- Sidebar -->
    <Sidebar :isOpen="sidebarOpen" @close="sidebarOpen = false" />

    <!-- Main Content -->
    <div class="flex flex-col flex-1 w-0 md:ml-64">
      <Navbar @toggleSidebar="sidebarOpen = !sidebarOpen" />

      <main class="flex-1 overflow-y-auto p-6 pt-20">
        <h1 class="text-3xl font-bold text-gray-800 mb-6">Add New Student</h1>

<router-link
  to="/students"
  class="inline-flex items-center text-blue-600 hover:text-blue-800 font-medium mb-4"
>
  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-1" fill="none" viewBox="0 0 24 24" stroke="currentColor">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
  </svg>
  Back to Student List
</router-link>


        <form class="space-y-10" @submit.prevent="submitForm">
          <!-- 🧍 Personal Information -->
<section class="form-section">
  <h2 class="form-section-title">🧍 Personal Information</h2>
  <div class="form-grid-3">
    <div class="flex flex-col">
      <label class="form-label">First Name *</label>
      <input type="text" class="form-input" v-model="form.first_name" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Middle Name * (optional)</label>
      <input type="text" class="form-input" v-model="form.middle_name" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Last Name *</label>
      <input type="text" class="form-input" v-model="form.last_name" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Date of Birth *</label>
      <input type="date" class="form-input" v-model="form.dob" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Gender *</label>
      <select class="form-input" v-model="form.gender">
        <option>Select</option>
        <option>Male</option>
        <option>Female</option>
        <option>Other</option>
      </select>
    </div>
    <div class="flex flex-col">
      <label class="form-label">Blood Group * (optional)</label>
      <input type="text" class="form-input" v-model="form.blood_group" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Nationality *</label>
      <input type="text" class="form-input" v-model="form.nationality" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Aadhar Number / Student ID * (optional)</label>
      <input type="text" class="form-input" v-model="form.aadhar_no" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Profile Photo Upload * (optional)</label>
      <input type="file" class="form-input-file" />
    </div>
  </div>
</section>

<!-- 🏠 Contact & Address -->
<section class="form-section">
  <h2 class="form-section-title">🏠 Contact & Address</h2>
  <div class="form-grid-2">
    <div class="flex flex-col">
      <label class="form-label">Mobile Number *</label>
      <input type="text" class="form-input" v-model="form.mobile" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Email Address *</label>
      <input type="email" class="form-input" v-model="form.email" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Present Address *</label>
      <input type="text" class="form-input" v-model="form.present_address" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Permanent Address *</label>
      <input type="text" class="form-input" v-model="form.permanent_address" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">City / State / Country *</label>
      <input type="text" class="form-input" v-model="form.city_state_country" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">ZIP / Postal Code *</label>
      <input type="text" class="form-input" v-model="form.zip_code" />
    </div>
  </div>
</section>

<!-- 👪 Guardian Details -->
<section class="form-section">
  <h2 class="form-section-title">👪 Guardian Details</h2>
  <div class="form-grid-3">
    <div class="flex flex-col">
      <label class="form-label">Father’s Name *</label>
      <input type="text" class="form-input" v-model="form.guardian.father_name" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Father’s Occupation *</label>
      <input type="text" class="form-input" v-model="form.guardian.father_occupation" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Father’s Phone *</label>
      <input type="text" class="form-input" v-model="form.guardian.father_phone" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Mother’s Name *</label>
      <input type="text" class="form-input" v-model="form.guardian.mother_name" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Mother’s Occupation *</label>
      <input type="text" class="form-input" v-model="form.guardian.mother_occupation" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Mother’s Phone *</label>
      <input type="text" class="form-input" v-model="form.guardian.mother_phone" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Emergency Contact Person *</label>
      <input type="text" class="form-input" v-model="form.guardian.emergency_contact_person" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Emergency Contact Number *</label>
      <input type="text" class="form-input" v-model="form.guardian.emergency_contact_number" />
    </div>
  </div>
</section>

<!-- 🎓 Academic Details -->
<section class="form-section">
  <h2 class="form-section-title">🎓 Academic Details</h2>
  <div class="form-grid-3">
    <div class="flex flex-col">
      <label class="form-label">Admission Number *</label>
      <input type="text" class="form-input" v-model="form.academic.admission_number" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Admission Date *</label>
      <input type="date" class="form-input" v-model="form.academic.admission_date" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Roll Number *</label>
      <input type="text" class="form-input" v-model="form.academic.roll_number" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Class / Grade *</label>
      <input type="text" class="form-input" v-model="form.academic.class_name" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Section *</label>
      <input type="text" class="form-input" v-model="form.academic.section" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Previous School</label>
      <input type="text" class="form-input" v-model="form.academic.previous_school" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Transfer Certificate Number (optional)</label>
      <input type="text" class="form-input" v-model="form.academic.transfer_certificate" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">House (if applicable)</label>
      <input type="text" class="form-input" v-model="form.academic.house" />
    </div>
  </div>
</section>

<!-- 💳 Fee & Transport -->
<section class="form-section">
  <h2 class="form-section-title">💳 Fee & Transport</h2>
  <div class="form-grid-3">
    <div class="flex flex-col">
      <label class="form-label">Fee Plan / Category</label>
      <input type="text" class="form-input" v-model="studentData.fee_transport.fee_plan" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Transport Route / Bus Number</label>
      <input type="text" class="form-input" v-model="studentData.fee_transport.transport_route" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Hostel Room (if applicable)</label>
      <input type="text" class="form-input" v-model="studentData.fee_transport.hostel_room" />
    </div>
  </div>
</section>

<!-- 📎 Documents Upload -->
<section class="form-section">
  <h2 class="form-section-title">📎 Documents Upload</h2>
  <div class="form-grid-2">
    <div class="flex flex-col">
      <label class="form-label">Birth Certificate</label>
      <input type="file" class="form-input-file" v-model="studentData.documents.birth_certificate" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Passport Size Photo</label>
      <input type="file" class="form-input-file" v-model="studentData.documents.passport_photo" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Transfer Certificate</label>
      <input type="file" class="form-input-file" v-model="studentData.documents.transfer_certificate_doc" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Aadhar / ID Proof</label>
      <input type="file" class="form-input-file" v-model="studentData.documents.aadhar_proof" />
    </div>
    <div class="flex flex-col">
      <label class="form-label">Signature (Digital)</label>
      <input type="file" class="form-input-file" v-model="studentData.documents.signature" />
    </div>
  </div>
</section>

          <button type="submit" class="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700">
            Register Student
          </button>
        </form>
      </main>
    </div>
  </div>
</template>

<script setup>
import Sidebar from '../components/appSidebar.vue'
import Navbar from '../components/appNavbar.vue'
import { useRouter } from 'vue-router'
import { reactive } from 'vue'
import { ref } from 'vue'
import axios from 'axios'


export default {
  name: 'RegisterStudentPage',
  data() {
    return {
      studentData: {
        // Personal Information
        first_name: '',
        middle_name: '',
        last_name: '',
        dob: '',
        gender: '',
        blood_group: '',
        nationality: '',
        aadhar_no: '',
        profile_photo_url: '',
        
        // Contact & Address
        mobile: '',
        email: '',
        present_address: '',
        permanent_address: '',
        city_state_country: '',
        zip_code: '',
        
        // Guardian Details
        guardian: {
          father_name: '',
          father_occupation: '',
          father_phone: '',
          mother_name: '',
          mother_occupation: '',
          mother_phone: '',
          emergency_contact_person: '',
          emergency_contact_number: ''
        },
        
        // Academic Details
        academic: {
          admission_number: '',
          admission_date: '',
          roll_number: '',
          class_name: '',
          section: '',
          previous_school: '',
          transfer_certificate: '',
          house: ''
        },
        
        // Fee & Transport
        fee_transport: {
          fee_plan: '',
          transport_route: '',
          hostel_room: ''
        },
        
        // Documents
        documents: {
          birth_certificate: '',
          passport_photo: '',
          transfer_certificate_doc: '',
          aadhar_proof: '',
          signature: ''
        }
      }
    }
  },
  methods: {
    async submitForm() {
      try {
        const response = await fetch('http://localhost:8000/api/students', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(this.studentData)
        });
        
        if (response.ok) {
          const result = await response.json();
          alert(result.message);
          this.resetForm();
        } else {
          throw new Error('Failed to submit form');
        }
      } catch (error) {
        console.error('Error:', error);
        alert('Error submitting form');
      }
    },
    
    resetForm() {
      // Reset all form fields
      this.studentData = {
        first_name: '',
        middle_name: '',
        last_name: '',
        dob: '',
        gender: '',
        blood_group: '',
        nationality: '',
        aadhar_no: '',
        profile_photo_url: '',
        mobile: '',
        email: '',
        present_address: '',
        permanent_address: '',
        city_state_country: '',
        zip_code: '',
        guardian: {
          father_name: '',
          father_occupation: '',
          father_phone: '',
          mother_name: '',
          mother_occupation: '',
          mother_phone: '',
          emergency_contact_person: '',
          emergency_contact_number: ''
        },
        academic: {
          admission_number: '',
          admission_date: '',
          roll_number: '',
          class_name: '',
          section: '',
          previous_school: '',
          transfer_certificate: '',
          house: ''
        },
        fee_transport: {
          fee_plan: '',
          transport_route: '',
          hostel_room: ''
        },
        documents: {
          birth_certificate: '',
          passport_photo: '',
          transfer_certificate_doc: '',
          aadhar_proof: '',
          signature: ''
        }
      };
    }
  }
}

</script>

<style scoped>
.form-input {
  @apply block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 bg-white text-gray-700;
}

.form-input-file {
  @apply block w-full text-sm text-gray-600 bg-white border border-gray-300 rounded-md cursor-pointer focus:outline-none focus:ring-2 focus:ring-blue-500;
}

.form-section {
  @apply bg-white p-6 rounded-lg shadow-md;
}

.form-section-title {
  @apply text-lg font-semibold mb-4;
}

.form-grid-2 {
  @apply grid grid-cols-1 md:grid-cols-2 gap-4;
}

.form-grid-3 {
  @apply grid grid-cols-1 md:grid-cols-3 gap-4;
}
</style>
