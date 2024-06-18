<template>
  <router-view></router-view>
</template>


<script setup lang="ts">
import { ref } from "vue";
import { onMounted } from "vue";
import { useRoute } from "vue-router";

// Initialize the isRetrieve state
const isRetrieve = ref(true);

// Method to change the state of isRetrieve
const changetype = () => {
  isRetrieve.value = !isRetrieve.value;
};

// Debounce function
const debounce = (fn: any, delay: any) => {
  let timer: any;
  return (...args: any) => {
    if (timer) {
      clearTimeout(timer);
    }
    timer = setTimeout(() => {
      fn(...args);
    }, delay);
  };
};

// Override the ResizeObserver with debounce
const resizeObserver = window.ResizeObserver;
window.ResizeObserver = class ResizeObserver extends resizeObserver {
  constructor(callback: any) {
    callback = debounce(callback, 200);
    super(callback);
  }
};

onMounted(() => {
  const route = useRoute();
  // Add any logic needed on mounted, like listening to route changes or other setup
});
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
