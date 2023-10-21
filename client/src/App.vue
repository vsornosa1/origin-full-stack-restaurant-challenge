<script setup>
import TabMenu from 'primevue/tabmenu';
import { ref } from 'vue';

const items = ref([
  {label: 'Menu', to: '/menu'},
  {label: 'Orders', to: '/orders'},
]);

</script>

<template>
  <div class="top-0">
    <TabMenu :model="items" />
    <router-view />
  </div>
</template>

