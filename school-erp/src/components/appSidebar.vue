<template>
  <!-- Mobile Backdrop -->
  <div
    v-if="isOpen"
    class="fixed inset-0 bg-black bg-opacity-30 z-40 md:hidden"
    @click="$emit('close')"
  />

  <!-- Sidebar -->
  <aside
    class="fixed top-0 left-0 z-50 w-64 h-full bg-white shadow transform transition-transform duration-300 ease-in-out"
    :class="isOpen ? 'translate-x-0' : '-translate-x-full md:translate-x-0'"
  >
    <div class="p-6 font-bold text-xl border-b border-gray-100">
      School ERP
    </div>
    <nav class="flex flex-col px-6 py-4 space-y-3">
      <RouterLink to="/dashboard" class="hover:text-blue-600" @click="$emit('close')">Dashboard</RouterLink>
      <RouterLink to="/students" class="hover:text-blue-600" @click="$emit('close')">Students</RouterLink>
      <RouterLink to="/teachers" class="hover:text-blue-600" @click="$emit('close')">Teachers</RouterLink>
      <RouterLink to="/finance" class="hover:text-blue-600" @click="$emit('close')">Finances</RouterLink>
      <RouterLink to="/events" class="hover:text-blue-600" @click="$emit('close')">Events</RouterLink>
      <RouterLink to="/users" class="hover:text-blue-600" @click="$emit('close')">Users</RouterLink>
    </nav>
  </aside>
</template>

<script setup>
defineProps({
  isOpen: Boolean
})
</script>