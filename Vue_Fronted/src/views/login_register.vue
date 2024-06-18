<template>
    <transition name="fade">
      <div v-if="isRetrieve">
        <register></register>
        <p class="upward-1" @click="changetype" v-if="isRetrieve">忘记密码?</p>
      </div>
      <div v-else>
        <resetpwd @updata-is-retrieve="changetype"></resetpwd>
        <p class="upward-2" 
        @click="changetype" 
        v-if="!isRetrieve">返回</p>
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
  
    },
    
  }
</script>

<style scoped="scoped">
  .upward-1 {
    position: relative;
    margin-top: -285px;
    margin-left: 735px;
}
.upward-2 {
    position: relative;
    margin-top: -298px;
    margin-left: 781px;
}
</style>
  