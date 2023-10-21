<template>
    <div v-if="cart.length" class="cart-dropdown" v-on:click="isOpen = !isOpen">
        <span> Cart has ({{ quantity }} items) </span>
        <div v-if="isOpen" class="cart-content">
            <ul>
                <li v-for="item in cart" :key="item.id" class="flex justify-content-between flex-wrap">
                    <span> {{ truncateMealName(item.plate_name) }} </span> 
                    <span> {{ item.price }} CHF x{{ item.quantity }} </span>
                </li>
            </ul>
            <hr />
            <div> Total: {{ total }} CHF </div>
            <hr />

            <Button label="Submit Order" @click="showConfirm" />
            <Dialog v-model:visible="displayConfirm" :modal="true" :closable="false">
                <template #header> Confirm Order </template>
                <p> Are you sure you want to submit your order? </p>
                <template #footer>
                    <Button label="No" @click="hideConfirm" />
                    <Button label="Yes!🍕" @click="submitOrder"  />
                </template>
            </Dialog>
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useCartStore } from '@/stores/cartStore';
import Button from 'primevue/button';
import Dialog from 'primevue/dialog';

let isOpen = ref(false);
let displayConfirm = ref(false);

const cartStore = useCartStore();
const cart = ref(cartStore.cart);
const total = computed(() => cartStore.cartTotal);
const quantity = computed(() => cartStore.cartQuantity);


const truncateMealName = (name) => {
    return name.split(' ').slice(0, 3).join(' ');
}

const showConfirm = () => {
    displayConfirm.value = true;
};
const hideConfirm = () => {
    displayConfirm.value = false;
};

const submitOrder = async () => {
    console.log('🌟', cartStore.cart)
    try {
        const response = await fetch('/api/orders', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(cartStore.cart)
        });

        if (response.ok) {
            alert('Order submitted successfully!');
            cartStore.clearCart();
        } else {
            alert('Failed to submit the order. Please try again.');
        }
    } catch (error) {
        console.error('There was an error submitting the order:', error);
    }
    hideConfirm();
};


</script>

<style scoped>
.cart-dropdown {
    color: var(--indigo-600);
    position: fixed;
    bottom: 10px;
    left: 10px;
    cursor: pointer;
    background-color: white;
    border: 1px solid #ddd;
    border-radius: full;
    padding: 10px;
    z-index: 1000;
}

.cart-content {
    color: black;
    position: absolute;
    bottom: 50px;
    left: 0;
    background-color: white;
    border: 1px solid #ddd;
    border-radius: full;
    width: 350px;
    padding: 10px 10px;
    z-index: 999;
}
</style>
