
<template>
    <div class="card">
        <DataView :value="meals" :layout="layout">
            <template #header>
                <div class="flex justify-content-end">
                    <DataViewLayoutOptions v-model="layout" />
                </div>
            </template>

            <template #list="slotProps">
                <div class="col-12">
                    <MealList :meal="slotProps.data" :addToCart="addMealToCart" />
                </div>
            </template>

            <template #grid="slotProps">
                <div class="col-12 sm:col-6 lg:col-12 xl:col-4 p-2">
                    <MealGrid :meal="slotProps.data" :addToCart="addMealToCart" />
                </div>
            </template>
        </DataView>
    </div>
    <CartDropup />
</template>

<script setup>
import { ref, onMounted } from 'vue';
import DataView from 'primevue/dataview';
import DataViewLayoutOptions from 'primevue/dataviewlayoutoptions';
import MealList from '@/components/common/MealList.vue';
import MealGrid from '@/components/common/MealGrid.vue';
import CartDropup from "@/components/common/CartDropup.vue";
import { useCartStore } from '@/stores/cartStore.js';

const cartStore = useCartStore();

const meals = ref([]);
const layout = ref('grid');

const addMealToCart = (meal) => {
    console.log('Adding meal to cart:', meal);
    cartStore.addToCart(meal);
};

const fetchMeals = async () => {
    const response = await fetch('https://localhost:8443/api/plates');
    meals.value = await response.json();
};

onMounted(fetchMeals);

</script>

