<template>
  <transition name="fade">
    <div v-if="isRetrieve">
      <register></register>
      <button class="upward" @click="changetype" v-if="isRetrieve">找回密码</button>
    </div>
    <div v-else>
      <resetpwd @updata-is-retrieve="changetype"></resetpwd>
      <button class="upward" 
      @click="changetype" 
      v-if="!isRetrieve">返回</button>
    </div>
  </transition>
</template>

<script>
import register from '../components/register.vue'
import resetpwd from '../components/reset_pwd.vue'

export default {
  name: 'login_register',
  components: {
    register,
    resetpwd
  },
  data(){
			return {
				isRetrieve: true,
			}
	},
  methods:{
    changetype(){
        console.log("change")
      this.isRetrieve=!this.isRetrieve;
    }

  }
}
</script>
