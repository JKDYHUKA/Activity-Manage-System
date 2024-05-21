<template>
  <PageHeader></PageHeader>
  <router-view></router-view>
</template>

<script>
import PageHeader from './components/PageHeader.vue'

export default {
  name: 'TestApp',
  components: {
    PageHeader,
  }
}
</script>

<style src="./styles/head.css">

</style>
