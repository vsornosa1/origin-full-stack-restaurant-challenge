import { defineStore } from 'pinia';

export const useCartStore = defineStore("cart", {
    state: () => ({
        cart: [],
    }),
    getters: {
        cartTotal() {
            return this.cart.reduce(
              (totalBill, item) => totalBill + item.price * item.quantity,
              0
            );
        },
        cartQuantity() {
            return this.cart.reduce(
              (quantity, item) => quantity + item.quantity,
              0
            );
        }
    },
    actions: {
        addToCart(meal) {
            const existingMeal = this.cart.find(
              (item) => item.plate_id === meal.plate_id
            );
            console.log('🎨',existingMeal)
            existingMeal ?
                existingMeal.quantity += 1
            :   this.cart.push({ ...meal, quantity: 1 });
        },
        removeFromCart(mealId) {
            const index = this.cart.findIndex((item) => item.plate_id === mealId);
            if (index !== -1) {
                this.cart[index].quantity > 1 ?
                    this.cart[index].quantity -= 1
                :   this.cart.splice(index, 1);
            }
        }
    },
    clearCart() {
        this.cart = [];
    },
});