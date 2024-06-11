<template>
    <el-tabs type="border-card">
      <el-tab-pane label="大型会议"><meeting></meeting></el-tab-pane>
      <el-tab-pane label="答辩面试"><interview/></el-tab-pane>
      <el-tab-pane label="研讨会"><seminar/></el-tab-pane>
      <el-tab-pane label="社交活动"><contact/></el-tab-pane>
      <el-tab-pane label="自定义"><customize/></el-tab-pane>
    </el-tabs>
</template>
  
<script>
import meeting from "../components/creation/meeting.vue"
import interview from "../components/creation/interview.vue"
import seminar from "../components/creation/seminar.vue"
import contact from "../components/creation/contact.vue"
import customize from "../components/creation/customize.vue"
export default{
  components: {
    meeting,
    interview,
    seminar,
    contact,
    customize
  },
}
</script>

<style scoped="scoped">
    
</style>