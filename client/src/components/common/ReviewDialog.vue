<template>
    <Dialog 
        :visible="showModal" 
        :modal="true" 
        :closable="false" 
        class="w-26rem">
        <template #header>
            <div class="flex flex-column align-items-center">
                <h3> ⭐ Reviews for {{ truncateMealName(meal.plate_name, 2) }} ⭐ </h3>
                <img class="w-9 shadow-2 border-round" :src="meal.picture" :alt="meal.plate_name" />
            </div>
        </template>

        <div v-for="review in reviews" :key="review.user_id" class="flex justify-content-between">
            <p><strong> {{ review.user_id }} </strong>: {{ review.comment }} </p>
            <Rating v-model="review.rating" readonly :cancel="false" />
        </div>
        <Button @click="cancelReviewDialog" class="text-sm negative-state" > Close </Button>
    </Dialog>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';
import Rating from 'primevue/rating';
import Dialog from 'primevue/dialog';
import { truncateMealName } from '@/services/stringManipulationService';


const { meal, showModal, reviews } = defineProps({
    meal: Object,
    reviews: Array,
    showModal: Boolean
});

const emit = defineEmits();
const cancelReviewDialog = () => {
    emit('update:showModal', false);
};

</script>
