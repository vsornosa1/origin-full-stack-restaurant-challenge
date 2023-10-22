<script setup>
import { ref } from 'vue';
import TabMenu from 'primevue/tabmenu';

const items = ref([
  {label: 'Menu', to: '/menu'},
  {label: 'My Orders', to: '/orders'},
]);


</script>

<template>
  <div class="top-0">
    <div class="flex align-items-center">
      <h1 class="text-700"> CERN's  Restaurant 🍜 </h1>
    </div>
    <TabMenu :model="items" />
    <router-view />
  </div>
</template>

