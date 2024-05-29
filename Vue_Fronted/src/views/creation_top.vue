<template>
    <el-tabs type="border-card">
      <el-tab-pane label="大型会议"><meeting></meeting></el-tab-pane>
      <el-tab-pane label="答辩面试"><interview/></el-tab-pane>
      <el-tab-pane label="研讨会">Role</el-tab-pane>
      <el-tab-pane label="社交活动">Task</el-tab-pane>
      <el-tab-pane label="自定义">Task</el-tab-pane>
    </el-tabs>
</template>
  
<script>
import meeting from "../components/meeting.vue"
import interview from "../components/interview.vue"

export default{
  components: {
    meeting,
    interview
  },
}
</script>

<style scoped="scoped">
    
</style>