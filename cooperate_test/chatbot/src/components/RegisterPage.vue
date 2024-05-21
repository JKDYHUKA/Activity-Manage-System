<template>
   <div class="container">
    <h2>Register</h2>
    <form v-on:submit.prevent="sendUserInfo">
      <div class="form-group">
        <label for="username">UserName：</label>
        <input v-model="userName" type="text" id="username" name="username" required>
      </div>
      <div class="form-group">
        <label for="email">Email：</label>
        <input v-model="email" type="email" id="email" name="email" required>
      </div>
      <div class="form-group">
        <label for="password">Password：</label>
        <input v-model="password" type="password" id="password" name="password" required>
      </div>
      <div class="form-group">
        <label for="confirm-password">Confirm Password：</label>
        <input v-model="confirmPassword" type="password" id="confirm-password" name="confirm-password" required>
      </div>
      <div class="form-group">
        <label for="captcha">Captcha：</label>
        <input v-model="captcha" type="text" id="captcha" name="captcha" required>
        <!-- 这里可以添加一个验证码图片或者其他验证码验证方式 -->
      </div>
      <button type="submit">Register</button>
      <button v-on:click="goToHome">Cancel</button>
    </form>
  </div> 
</template>

<script>
import { defineComponent, ref } from 'vue'

export default defineComponent({
    methods: {
        goToHome(){
            this.$router.push('/');
        },
    },
    setup() {
        var userName = ref('');
        var email = ref('');
        var password = ref('');
        var confirmPassword = ref('');
        var captcha = ref('');

        function sendUserInfo(){
            console.log(userName.value);
            console.log(email.value);
            console.log(password.value);
            console.log(confirmPassword.value);
            console.log(captcha.value);
        }

        return {
            userName,
            email,
            password,
            confirmPassword,
            captcha,
            sendUserInfo,
        }
    },
})
</script>

<style scoped>
body {
  font-family: Arial, sans-serif;
  background-color: #f2f2f2;
  margin: 0;
  padding: 0;
}

.container {
  max-width: 400px;
  margin: auto;
  margin-top: 2vh;
  background-color: #fff;
  padding: 1%;
  border-radius: 5px;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
}

h2 {
  text-align: center;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  font-weight: bold;
}

input {

  width: 95%;
  padding: 10px;
  font-size: 16px;
  border: 0;
  border-bottom: 2px solid #0c0c0c;
  /* border-radius: 5px; */
}

input:focus{outline: 0;}

button {
  width: 45%;
  padding: 10px;
  font-size: 16px;
  background-color: rgba(109,171,228, 0.7);
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-left: 3%;
}

button:hover {
  background-color: rgb(109,171,228);
}

#captcha{
    width: 40%;
    /* border: 1px solid #000000; */
}

</style>
