<template>
    <div class="card-header bg-primary text-white">
        <div class="optionals" id="a" v-on:click="goToHome">Chat</div>
        <div class="optionals" id="b" v-on:click="goToTravelChat">Travel</div>
        <div class="right">
            <div class="register" v-on:click="goToRegister">Register</div>
            <div class="login" v-on:click="goToLogin">LogIn</div>
        </div>
    </div>
</template> 

<script>
export default {
    name: 'PageHeader',
    methods: {
        goToLogin() {
            this.$router.push('/login');
        },
        goToHome(){
           this.$router.push('/');
        },
        goToRegister(){
            this.$router.push('/register');
        },
        goToTravelChat(){
            this.$router.push('/travelChat');
        },

    },
    // props: {
    //   router: Object, // 接收路由实例作为props
    // },
}
</script>

<style scoped src="../styles/head.css">

</style>