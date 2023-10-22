<template>
    <div class="p-4 border-1 surface-border surface-card border-round">
        <div class="flex flex-column align-items-center gap-3 py-5">
            <img class="w-9 shadow-2 border-round" :src="meal.picture" :alt="meal.plate_name" />
            <div class="text-2xl font-bold"> {{ meal.plate_name }} </div>
        </div>
        <div class="flex align-items-center justify-content-between">
            <div class="flex flex-column align-items-start">
                <span class="text-xl font-semibold"> {{ meal.price }} CHF </span>
                <Rating v-model="value" :cancel="false" />
            </div>
            <div class="flex gap-1">
                <Button icon="pi pi-info-circle" @click="openReviewsDialog" rounded />
                <Button icon="pi pi-shopping-cart" @click="addToCart(meal)" rounded />
            </div>
        </div>
    </div>
    <ReviewDialog :meal="meal" :reviews="reviews" :showModal="showModal" />
</template>

<script setup>
import { ref, defineProps } from 'vue';
import Button from 'primevue/button';
import Rating from 'primevue/rating';
import ReviewDialog from './ReviewDialog.vue';
import { makeApiCallWithToken } from '@/services/apiService';

const showModal = ref(false);
const reviews = ref(null);

const { meal, addToCart } = defineProps({
    meal: Object,
    addToCart: Function
});

const openReviewsDialog = async () => {
    showModal.value = true;
    fetchPlateReviews();
}

const fetchPlateReviews = async () => {
    try {
        const response_reviews = await makeApiCallWithToken(`/api/reviews/plates/${meal.plate_id}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        console.log(response_reviews)
        if (response_reviews.length > 0) {
            reviews.value = response_reviews;
        }
    } catch (error) {
        console.error('There was an error fetching the reviews:', error);
    }
}

</script>