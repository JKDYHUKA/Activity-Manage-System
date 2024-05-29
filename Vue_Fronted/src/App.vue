<template>
  <router-view></router-view>
</template>

<script>

export default {
name: 'App',
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

<style scoped="scoped">
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
