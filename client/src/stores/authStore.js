import { defineStore } from '@pinia/store';

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