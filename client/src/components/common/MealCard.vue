<template>
    <div class="flex flex-column xl:flex-row xl:align-items-start p-4 gap-4">
        <img class="w-9 sm:w-16rem xl:w-10rem shadow-2 block xl:block mx-auto border-round" :src="meal.picture"
            :alt="meal.plate_name" />
        <div
            class="flex flex-column sm:flex-row justify-content-between align-items-center xl:align-items-start flex-1 gap-4">
            <div class="flex flex-column align-items-center sm:align-items-start gap-3">
                <div class="text-2xl font-bold text-900">{{ meal.plate_name }}</div>
            </div>
            <div class="flex sm:flex-column align-items-center sm:align-items-end gap-3 sm:gap-2">
                <span class="text-2xl font-semibold">{{ meal.price }} € </span>
                <Button icon="pi pi-shopping-cart" rounded />
            </div>
        </div>
    </div>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
    props: {
        meal: Array
    },
    setup() {
        const addToCart = () => {
            // Logic to add meal to cart goes here
        }

        return {
            addToCart
        };
    }
});
</script>
