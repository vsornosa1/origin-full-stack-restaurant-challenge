<template>
  <Dialog
    :modal="true" 
    :closable="true" 
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
import { ref, computed, onMounted } from 'vue';
import { useAuthStore } from '@/stores/authStore';
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';

export default {
  components: {
    Dialog,
    Button,
    InputText
  },
  props: {
    display: Boolean
  },
  setup(props) {
    const authStore = useAuthStore();

    const login = ref({
      username: '',
      password: ''
    });

    const isButtonDisabled = computed(() =>
      !login.value.username.trim() || !login.value.password.trim()
    );

    async function handleLogin() {
      console.log('Logging in with: ', login.value.username);
      const response = await fetch('https://localhost:8443/token', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(login.value)
      });

      if (response.ok) {
        console.log('Hit');
        const data = await response.json();
        const token = data.access_token;
        localStorage.setItem('token', token);
      } else {
        console.error("Error logging in:", await response.text());
      }
    }

    async function makeApiCallWithToken(url, options = {}) {
      options.headers = options.headers || {};
      options.headers['Authorization'] = 'Bearer ' + localStorage.getItem('token');
      const response = await fetch(url, options);
      return response.json();
    }

    function checkAuth() {
      const token = localStorage.getItem("token");
      if (token) {
        authStore.setAuthenticated(true);
      }
    }

    onMounted(checkAuth);

    return {
      login,
      isButtonDisabled,
      handleLogin
    };
  }
}
</script>
