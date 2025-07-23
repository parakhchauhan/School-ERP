<template>
  <div class="ag-theme-alpine" style="height: 400px; width: 100%;">
    <AgGridVue
      :rowData="rowData"
      :columnDefs="columnDefs"
    ></AgGridVue>
  </div>
</template>

<script setup>
import { AgGridVue } from 'ag-grid-vue3'
import 'ag-grid-community/styles/ag-grid.css'
import 'ag-grid-community/styles/ag-theme-alpine.css'

const columnDefs = [
  { headerName: 'ID', field: 'id' },
  { headerName: 'Name', field: 'name' },
  { headerName: 'Email', field: 'email' }
]

const rowData = [
  { id: 1, name: 'Parakh Chauhan', email: 'parakh@example.com' },
  { id: 2, name: 'Aarav Nanda', email: 'aarav@example.com' }
]
</script>