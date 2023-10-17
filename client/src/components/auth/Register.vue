<template>
  <Dialog
    :modal="true" 
    :closable="true" 
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
import Dialog from 'primevue/dialog';
import Button from 'primevue/button';
import InputText from 'primevue/inputtext';

export default {
  components: {
    Dialog,
    Button,
    InputText
  },
  data() {
    return {
      register: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    closeModal() {
      this.$emit('update:display', false);
    },
    async handleRegister() {
      console.log('Registering with', this.register.username);

      try {
        const response = await fetch("https://localhost:8443/api/users", {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(this.register)
        });

        if (!response.ok) {
          const data = await response.json();
          throw new Error(data.detail);
        }

        this.$router.push("/");
      } catch (err) {
        console.error("An error occurred:", err.message);
      }

      //this.closeModal();
    }
  },
	computed: {
    isButtonDisabled() {
      return !this.register.username.trim() || !this.register.password.trim();
    }
},
}
</script>
