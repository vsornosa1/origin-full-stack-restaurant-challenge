<template>
    <div class="flex flex-column xl:flex-row xl:align-items-start p-4 gap-4">
        <img class="w-9 sm:w-16rem xl:w-10rem shadow-2 block xl:block mx-auto border-round" :src="meal.picture"
            :alt="meal.plate_name" />
        <div class="flex flex-column sm:flex-row justify-content-between align-items-center xl:align-items-start flex-1 gap-4">
            <div class="flex flex-column align-items-center sm:align-items-start gap-3">
                <div class="text-2xl font-bold text-900"> {{ meal.plate_name }} </div>
                <div v-if="mealRatings > 0">
                    <Rating v-model="mealRatings" readonly :cancel="false" />
                </div>
                <div v-else>
                    <i> Buy the {{ meal.plate_name }} to be the first coleague in CERN to review this meal! </i>
                </div>
            </div>
            <div class="flex sm:flex-column align-items-center sm:align-items-end gap-3 sm:gap-2">
                <span class="text-2xl font-semibold"> {{ meal.price }} CHF </span>
                <div class="flex gap-1">
                    <Button icon="pi pi-info-circle" @click="openReviewsDialog" rounded />
                    <Button icon="pi pi-shopping-cart" rounded @click="addToCart(meal)" />
                </div>
            </div>
        </div>
    </div>
    <ReviewDialog :meal="meal" :reviews="reviews" :showModal="showModal" @update:showModal="val => showModal = val" />
</template>

<script setup>
import { ref, defineProps, onMounted } from 'vue';
import Button from 'primevue/button';
import Rating from 'primevue/rating';
import ReviewDialog from './ReviewDialog.vue';
import { makeApiCallWithToken } from '@/services/apiService';


const showModal = ref(false);

const reviews = ref(null);
const mealRatings = ref({});


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
        if (response_reviews.length > 0) {
            reviews.value = response_reviews;
        }
    } catch (error) {
        console.error('There was an error fetching the reviews:', error);
    }
}

const fetchAverageRatings = async () => {
    const response_rating = await makeApiCallWithToken(`/api/plates/average/${meal.plate_id}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    });
    mealRatings.value = response_rating;
}


onMounted(async () => {
    fetchAverageRatings();
});

</script>