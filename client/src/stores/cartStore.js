import { defineStore } from '@pinia/store';

export const useCartStore = defineStore('cart', {
    state: () => ({
        meals: []
    }),
    actions: {
        addMeal(meal) {
            this.meals.push(meal);
        },
        removeMeal(index) {
            this.meals.splice(index, 1);
        }
    },
});