<script setup>
import { Form, Field } from 'vee-validate';
import * as Yup from 'yup';

import { useUsersStore, useAlertStore } from '@/stores';
import { router } from '@/router';

const schema = Yup.object().shape({
    firstName: Yup.string()
        .required('First Name is required'),
    lastName: Yup.string()
        .required('Last Name is required'),
    username: Yup.string()
        .required('Username is required'),
    password: Yup.string()
        .required('Password is required')
        .min(6, 'Password must be at least 6 characters')
});

async function getVerificationCode() {
  try {
    const response = await axios.post('http://127.0.0.1:8000/api/get_captcha', {
        username: values.username,
        phone_number:values.phonenumber,
    });

    // 处理响应
    console.log('Verification code sent:', response.data);
  } catch (error) {
    console.error('Error sending verification code:', error);
  }
}   

async function register(values) {
    const usersStore = useUsersStore();
    const alertStore = useAlertStore();
    try {
        // Send a POST request to the backend API
        await axios.post('http://127.0.0.1:8000/api/register', {
            username: values.username,
            password: values.password,
            nickname: values.firstName + ' ' + values.lastName,
            phone_number:values.phonenumber,
        });

        // Redirect to the login page
        await router.push('/account/login');
        alertStore.success('Registration successful');
    } catch (error) {
        alertStore.error(error.message);
    }
}

async function onSubmit(values) {
    const usersStore = useUsersStore();
    const alertStore = useAlertStore();
    try {
        await usersStore.register(values);
        await router.push('/account/login');
        alertStore.success('Registration successful');
    } catch (error) { 
        alertStore.error(error);
    }
}
</script>

<template>
    <div class="card m-3">
        <h4 class="card-header">Register</h4>
        <div class="card-body">
            <Form @submit="onSubmit" :validation-schema="schema" v-slot="{ errors, isSubmitting }">
                <div class="form-group">
                    <label>First Name</label>
                    <Field name="firstName" type="text" class="form-control" :class="{ 'is-invalid': errors.firstName }" />
                    <div class="invalid-feedback">{{ errors.firstName }}</div>
                </div>
                <div class="form-group">
                    <label>Last Name</label>
                    <Field name="lastName" type="text" class="form-control" :class="{ 'is-invalid': errors.lastName }" />
                    <div class="invalid-feedback">{{ errors.lastName }}</div>
                </div>
                <div class="form-group">
                    <label>Username</label>
                    <Field name="username" type="text" class="form-control" :class="{ 'is-invalid': errors.username }" />
                    <div class="invalid-feedback">{{ errors.username }}</div>
                </div>
                <div class="form-group">
                    <label>Password</label>
                    <Field name="password" type="password" class="form-control" :class="{ 'is-invalid': errors.password }" />
                    <div class="invalid-feedback">{{ errors.password }}</div>
                </div>
                <div class="form-group">
                    <label>Phonenumber</label>
                    <Field name="phonenumber" type="phonenumber" class="form-control" :class="{ 'is-invalid': errors.phonenumber }" />
                    <div class="invalid-feedback">{{ errors.phonenumber }}</div>
                </div>

                <button  id="yzm" @click="getVerificationCode">点击获取验证码</button>
                <input type="text" name="yzm" id="yzms" placeholder="验证码" style="margin-top: 7.5px;margin-bottom: 7.5px;">
                <br>

                <div class="form-group">
                    <button @click="register" class="btn btn-primary" :disabled="isSubmitting">
                        <span v-show="isSubmitting" class="spinner-border spinner-border-sm mr-1"></span>
                        Register
                    </button>
                    <router-link to="login" class="btn btn-link">Cancel</router-link>
                </div>
            </Form>
        </div>
    </div>
</template>


<style scoped>

</style>