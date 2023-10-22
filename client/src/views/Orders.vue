
<template>
    <div v-if="orders && orders.length" v-for="order in orders">
        <div class="card xl:flex xl:justify-content-center">
            <OrderList v-model="order.plates" listStyle="height:auto" dataKey="i">
                <template #header>
                    <div class="flex justify-content-between gap-4">
                        <span># {{ order.order_id }}</span>
                        <span>{{ parseTimeToString(order.order_time) }}</span>
                        <span>💸 Total: {{ getOrderTotal(order.order_id) }} CHF </span>
                    </div>
                    
                </template>
                <template #item="slotProps">
                    <div class="flex flex-wrap p-2 align-items-center gap-3">
                        <img class="w-4rem shadow-2 flex-shrink-0 border-round" :src="plateInfo(slotProps.item.plate_id).picture" :alt="slotProps.item.name" />
                        <div class="flex-1 flex flex-column gap-2">
                            <span class="font-bold w-10rem">{{ slotProps.item.quantity }} x {{ slotProps.item.plate_name }}</span>
                        </div>
                        <span class="font-bold text-900">{{ plateInfo(slotProps.item.plate_id).price * slotProps.item.quantity }} CHF</span>
                        <Button @click="openReviewModal(slotProps.item.plate_id)" label="Review" />
                    </div>
                </template>
            </OrderList>
        </div>
    </div>
    <div v-else>
        <p class="text-gray-700"> No orders so far! </p>
        <p class="text-gray-700"> Maybe you could <router-link to="/menu" class="cursor-pointer"> order something... </router-link></p>
    </div>
    <Dialog
        :modal="true" 
        :closable="false" 
        :visible="showReviewModal" 
        :header="'🍜 Tell us about your ' + truncateMealName(currentPlateInfo.plate_name, 1) + '!'"
        @hide="closeModal" 
        class="w-24rem">
        <div class="bg-white px-6 rounded shadow-lg w-1/2">
            <div class="flex flex-column align-items-center gap-4">
                <img class="w-12rem shadow-2 flex-shrink-0 border-round" :src="currentPlateInfo.picture" :alt="plateInfo(currentPlateId).plate_name" />
                <Rating v-model="currentRating" :cancel="false" />
            </div>
            <Textarea v-model="currentComment" autoResize rows="5" cols="30" placeholder="Leave a comment..." class="w-full mt-4 p-2 border" />
            <div class="mt-4 text-right flex gap-2 justify-content-center">
                <Button @click="cancelReview" class="negative-state" label="Cancel" />
                <Button @click="submitReview" label="Submit" :disabled="!currentRating || !currentComment" />
            </div>
        </div>
    </Dialog>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import Button from 'primevue/button';
import Rating from 'primevue/rating';
import Dialog from 'primevue/dialog';
import Textarea from 'primevue/textarea';
import OrderList from 'primevue/orderlist';
import { makeApiCallWithToken } from '@/services/apiService';
import { truncateMealName, parseTimeToString } from '../services/stringManipulationService';


const orders = ref(null);
const plates = ref();
const router = useRouter();

const showReviewModal = ref(false);
const currentPlateId = ref(null);
const currentPlateInfo = ref('');
const currentRating = ref(null);
const currentComment = ref('');

 // REVIEWS
const openReviewModal = (plateId) => {
    showReviewModal.value = true;
    currentPlateId.value = plateId;
    currentPlateInfo.value = plateInfo(plateId);
}

const cancelReview = () => {
    showReviewModal.value = false;
    currentRating.value = null;
    currentComment.value = '';
}


 // PRICING + PLATES
const plateInfo = (itemId) => {
    return plates.value.find(plate => plate.plate_id === itemId)
}

const getOrderTotal = (orderId) => {
    let total = 0;
    orders.value.find(order => order.order_id === orderId).plates.forEach(plate => {
        total += plateInfo(plate.plate_id).price * plate.quantity;
    });
    return total.toFixed(2);
}


 // API interaction functions
const fetchPlates = async () => {
    const URL = "https://localhost:8443/api/plates"
    const response = await fetch(URL);
    const data = await response.json();
    plates.value = data;
}

const fetchUserOrders = async () => {
    try {
        const response_orders = await makeApiCallWithToken('/api/orders', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        console.log("🌟🌟Orders:", response_orders);
        if (response_orders) {
            orders.value = response_orders;
        } else {
            alert('Failed to submit the order. Please try again.');
        }
    } catch (error) {
        console.error('There was an error submitting the order:', error);
    }
}

const submitReview = async () => {
    const reviewData = {
        plate_id: currentPlateId.value,
        rating: currentRating.value,
        comment: currentComment.value
    };
    try {
        const response = await makeApiCallWithToken('/api/reviews', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(reviewData)
        });

        if (response) {
            alert('Review submitted successfully!');
            showReviewModal.value = false;
        } else {
            alert('Review already done for this meal!');
        }
    } catch (error) {
        console.error('There was an error submitting the review:', error);
    }
}


onMounted(async () => {
    fetchPlates();
    fetchUserOrders();
});

</script>