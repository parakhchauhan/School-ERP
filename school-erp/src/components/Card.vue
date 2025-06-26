<template>
  <div class="bg-white p-5 rounded-lg shadow hover:shadow-xl transform hover:scale-105 transition duration-200 ease-in-out">
    <h2 class="text-gray-600 text-sm mb-1">{{ title }}</h2>
    <p class="text-2xl font-bold text-gray-800">{{ value }}</p>
  </div>
</template>

<script setup>
defineProps({
  title: String,
  value: [String, Number]
})
</script>