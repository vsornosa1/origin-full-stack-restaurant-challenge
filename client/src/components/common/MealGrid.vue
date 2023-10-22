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
                <Button icon="pi pi-info-circle" @click="openReviewsDialog(meal)" rounded />
                <Button icon="pi pi-shopping-cart" @click="addToCart(meal)" rounded />
            </div>
        </div>
    </div>
    <Dialog :visible="showModal" :modal="true" :closable="false" class="w-24rem">
        <template #header>
            <div class="flex flex-column align-items-center">
                <h3> ⭐ Reviews for {{ truncateMealName(meal.plate_name, 2) }} ⭐</h3>
                <img class="w-9 shadow-2 border-round" :src="meal.picture" :alt="meal.plate_name" />
            </div>
        </template>

        <div v-for="review in reviews" :key="review.user_id" class="flex justify-content-between">
            <p><strong>{{ review.user_id }}</strong>: {{ review.comment }}</p>
            <Rating v-model="review.rating" readonly :cancel="false" />
        </div>
      </Dialog>
</template>

<script setup>
import { ref } from 'vue';
import Button from 'primevue/button';
import Rating from 'primevue/rating';
import Dialog from 'primevue/dialog';
import { makeApiCallWithToken } from '@/services/apiService';
import { truncateMealName } from '@/services/stringManipulationService';


const reviews = ref(null);
const showModal = ref(false);

const { meal, addToCart } = defineProps({
    meal: Object,
    addToCart: Function
});

const openReviewsDialog = async (meal) => {
    await fetchPlateReviews(meal.plate_id);
}

const fetchPlateReviews = async () => {
    console.log(meal)
    try {
        const response_reviews = await makeApiCallWithToken(`/api/reviews/plates/${meal.plate_id}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        console.log("🌟🌟Reviews:", response_reviews);
        if (response_reviews.length > 0) {
            reviews.value = response_reviews;
            showModal.value = true;
        } else {
            alert('Failed to fetch reviews.');
        }
    } catch (error) {
        console.error('There was an error fetching the reviews:', error);
    }
}

</script>