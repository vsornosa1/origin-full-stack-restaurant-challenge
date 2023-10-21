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
import { ref, computed } from 'vue';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';
import { useRouter } from 'vue-router';

export default {
  components: {
    Dialog,
    Button,
    InputText
  },
  setup(_, { emit }) {
    const router = useRouter();

    const register = ref({
      username: '',
      password: ''
    });

    const isButtonDisabled = computed(() =>
      !register.value.username.trim() || !register.value.password.trim()
    );

    function closeModal() {
      emit('update:display', false);
    }

    async function handleRegister() {
      console.log('Registering with', register.value.username);

      try {
        const response = await fetch("https://localhost:8443/api/users", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(register.value)
        });

        if (!response.ok) {
          const data = await response.json();
          throw new Error(data.detail);
        }

        router.push("/");
      } catch (err) {
        console.error("An error occurred:", err.message);
      }
      closeModal();
    }

    return {
      register,
      isButtonDisabled,
      closeModal,
      handleRegister
    };
  }
}
</script>
