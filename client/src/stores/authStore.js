import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
    state: () => ({
        isAuthenticated: false
    }),
    actions: {
        setAuthenticated(authStatus) {
            this.isAuthenticated = authStatus;
        }
    }
});