<template>
  <Dialog
    :modal="true" 
    :closable="false" 
    :visible="true" 
    header="🍕 CERN's Restaurant"
    @hide="closeModal" 
		class="w-24rem">

    <h3> Welcome back colleague! </h3>

		<div class="flex flex-column">
			<InputText class="flex-1 " v-model="login.username" placeholder="Enter username" />
			<InputText class="flex-1 my-3" v-model="login.password" type="password" placeholder="Your password" />
		</div>

		<div class="flex flex-row-reverse">
      <Button :disabled="isButtonDisabled" class="block mt-2" label="Login" @click="handleLogin" />
		</div>
    <p> Don't have an account? <router-link to="/register" class="cursor-pointer"> Register </router-link></p>
  </Dialog>
</template>

<script>
import { reactive, computed, onMounted } from 'vue';
import { useAuthStore } from '@/stores/authStore';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import { useRouter } from 'vue-router';
import { getToken } from '@/services/apiService';

export default {
  components: {
    Dialog,
    Button,
    InputText
  },
  props: {
    display: Boolean
  },
  setup(_, context) {
    const router = useRouter();
    const authStore = useAuthStore();

    const state = reactive({
      login: {
        username: '',
        password: ''
      },
    });

    const isButtonDisabled = computed(() =>
      !state.login.username.trim() || !state.login.password.trim()
    );

    function closeModal() {
      context.emit('update:display', false);
    }

    function navigateToMenuIfAuthenticated() {
      if (authStore.isAuthenticated) {
        router.push('/menu');
      }
    }

    async function attemptLogin() {
      try {
        const data = await getToken(state.login);
        localStorage.setItem('token', data.access_token);
        authStore.setAuthenticated(true);
        navigateToMenuIfAuthenticated();
      } catch (error) {
        console.error("Error logging in:", error.message);
      }
      closeModal();
    }

    onMounted(navigateToMenuIfAuthenticated);

    return {
      ...state,
      isButtonDisabled,
      handleLogin: attemptLogin,
    };
  }
}
</script>