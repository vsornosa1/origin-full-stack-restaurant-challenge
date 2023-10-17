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
  data() {
    return {
      login: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    closeModal() {
      this.$emit('update:display', false);
    },
    handleLogin() {
      console.log('Logging in with', this.login.username);
      this.closeModal();
    }
  },
	computed: {
    isButtonDisabled() {
      return !this.login.username.trim() || !this.login.password.trim();
    }
},
}
</script>
