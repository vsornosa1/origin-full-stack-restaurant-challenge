<template>
    <div class="p-4 border-1 surface-border surface-card border-round">
        <!-- Additional header details can be added here. -->
        <div class="flex flex-column align-items-center gap-3 py-5">
            <img class="w-9 shadow-2 border-round" :src="meal.picture" :alt="meal.plate_name" />
            <div class="text-2xl font-bold"> {{ meal.plate_name }} </div>
        </div>
        <div class="flex align-items-center justify-content-between">
            <span class="text-2xl font-semibold"> {{ meal.price }} CHF </span>
            <Button icon="pi pi-shopping-cart" @click="addToCart(meal)" rounded></Button>
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue';
import Button from 'primevue/button';

export default defineComponent({
    components: {
        Button
    },
    props: {
        meal: Object,
        addToCart: Function
    }
});
</script>