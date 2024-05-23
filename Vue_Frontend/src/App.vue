<template>
    <login_register></login_register>
</template>

<script>
import login_register from './views/login_register.vue';

export default {
  name: 'App',
  components: {
    login_register,
  },
  data(){
			return {
				isRetrieve:true,
			}
	},
  methods:{
    changetype(){
      this.isRetrieve=!this.isRetrieve;
    }

  }
}
</script>

<style>
.fade-enter-active, .fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.upward {
  position: relative;
  top: -28px;
  left:261px;
  transform: translate(0, -100px);
}

</style>
