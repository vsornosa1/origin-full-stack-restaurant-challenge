<template>
    <div v-if="cart.length" class="cart-dropdown" v-on:click="isOpen = !isOpen">
        <span> Cart has ({{ quantity }} items) </span>
        <div v-if="isOpen" class="cart-content">
            <ul>
                <li v-for="item in cart" :key="item.id">
                    {{ item.plate_name }} - {{ item.price }} CHF x{{ item.quantity }}
                </li>
            </ul>
            <hr>
            <div> Total: {{ total }} CHF </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useCartStore } from '@/stores/cartStore';

const cartStore = useCartStore();
const cart = ref(cartStore.cart);
const total = computed(() => cartStore.cartTotal);
const quantity = computed(() => cartStore.cartQuantity);

let isOpen = ref(false);
</script>

<style scoped>
.cart-dropdown {
    color: blue;
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
    width: 200px;
    z-index: 999;
}
</style>
