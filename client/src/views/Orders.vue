
<template>
    <div v-if="orders && orders.length" v-for="order in orders">
        <div class="card xl:flex xl:justify-content-center">
            <OrderList v-model="order.plates" listStyle="height:auto" dataKey="i">
                <template #header>
                    <div class="flex gap-5">
                        <span># {{ order.order_id }}</span>
                        <span>{{ parseTimeToString(order.order_time) }}</span>
                        <span>Total: {{ getOrderTotal(order.order_id) }} €</span>
                    </div>
                    
                </template>
                <template #item="slotProps">
                    <div class="flex flex-wrap p-2 align-items-center gap-3">
                        <img class="w-4rem shadow-2 flex-shrink-0 border-round" :src="plateImage(slotProps.item.plate_id)" :alt="slotProps.item.name" />
                        <div class="flex-1 flex flex-column gap-2">
                            <span class="font-bold w-10rem">{{ slotProps.item.quantity }} x {{ slotProps.item.plate_name }}</span>
                        </div>
                        <span class="font-bold text-900">{{ platePrice(slotProps.item.plate_id) * slotProps.item.quantity }} €</span>
                    </div>
                </template>
            </OrderList>
        </div>
    </div>
    <div v-else>
        <p class="text-gray-700"> No orders so far! </p>
        <p class="text-gray-700"> Maybe you could <router-link to="/menu" class="cursor-pointer"> order something... </router-link></p>
    </div>
</template>

<script setup>
import OrderList from 'primevue/orderlist';
import { ref, onMounted, computed } from 'vue';
import { useRouter } from 'vue-router';
import { makeApiCallWithToken } from '@/services/apiService';


const orders = ref(null);
const plates = ref();
const router = useRouter();

const reversedListOfOrders = computed(() => {
    return [...orders.value].reverse(); // copyOf
});


onMounted(async () => {
    // fetch plates from server
    const URL = "https://localhost:8443/api/plates"
    const response = await fetch(URL);
    const data = await response.json();
    plates.value = data;

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
});


function platePrice(itemId) {
    return plates.value.find(plate => plate.plate_id === itemId).price
}

function plateImage(itemId) {
    return plates.value.find(plate => plate.plate_id === itemId).picture
}

function parseTimeToString(timestamp) {
    if (!timestamp) return "";
    const regex = /(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2})/;
    let matches = timestamp.match(regex);
    if (matches) {
        return matches[1] + " " + matches[2];
    }
}

function getOrderTotal(orderId) {
    let total = 0;
    orders.value.find(order => order.order_id === orderId).plates.forEach(plate => {
        total += platePrice(plate.plate_id) * plate.quantity;
    });
    return total.toFixed(2);
}

</script>