<template>
  <Dialog
    :modal="true" 
    :closable="false" 
		:visible="true"
    header="🍕 CERN's Restaurant"
    @hide="closeModal"
		class="w-24rem">

    <h3> Official registering form </h3>

		<div class="flex flex-column">
			<InputText class="flex-1 " v-model="register.username" placeholder="Enter username" />
			<InputText class="flex-1 my-3" v-model="register.password" type="password" placeholder="Your password" />
		</div>

		<div class="flex flex-row-reverse">
			<Button :disabled="isButtonDisabled" class="block mt-2" label="Register" @click="handleRegister" />
		</div>
    <p> Already have an account? <router-link to="/" class="cursor-pointer"> Login </router-link></p>
  </Dialog>
</template>

<script>
import { reactive, computed, onMounted } from 'vue';
import { useAuthStore } from '@/stores/authStore';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import { useRouter } from 'vue-router';
import { registerUser } from '@/services/apiService'; 

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
      register: {
        username: '',
        password: ''
      },
   });

   const isButtonDisabled = computed(() =>
      !state.login.username.trim() || !state.login.password.trim()
    );

    const closeModal = () => {
      context.emit('update:display', false);
    }

    const navigateToMenuIfAuthenticated = () => {
      if (authStore.isAuthenticated) {
        router.push('/menu');
      }
    }

    const attemptRegister = async () => {
      try {
        await registerUser(state.register);
        authStore.setAuthenticated(true);
        alert('Successfully created a new account! Now, log in to continue.')
        navigateToMenuIfAuthenticated();
      } catch (error) {
        console.error("Error registering:", error.message);
      }
      closeModal();
    }

    onMounted(navigateToMenuIfAuthenticated);

    return {
      ...state,
      handleRegister: attemptRegister
    };
  }
}
</script>