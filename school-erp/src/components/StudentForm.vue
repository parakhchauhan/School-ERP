<template>
  <form @submit.prevent="submitForm">
    <input type="text" v-model="student.name" placeholder="Student Name" class="border p-2 w-full mb-3">
    <select v-model="student.grade" class="border p-2 w-full mb-3">
      <option value="Grade 1">Grade 1</option>
      <option value="Grade 2">Grade 2</option>
    </select>
    <button type="submit" class="bg-green-500 text-white py-2 px-4">Register</button>
  </form>
</template>

<script>
export default {
  data() { return { student: { name: "", grade: "" } }; },
  methods: { submitForm() { console.log("Student Registered:", this.student); } }
};
</script>