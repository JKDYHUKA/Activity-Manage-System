<template>
    <el-upload
      ref="uploadRef"
      class="upload-demo"
      action="http://127.0.0.1:8000/api/upload/"
      :auto-upload="false"
      :data="uploadData"
    >
      <template #trigger>
        <el-button type="primary">选择文件</el-button>
      </template>
  
      <el-button class="ml-3" type="success" @click="submitUpload">
        上传到服务器
      </el-button>
  
      <template #tip>
        <div class="el-upload__tip">
          jpg/png 文件大小不超过 500kb
        </div>
      </template>
    </el-upload>
  </template>
  
  <script lang="ts" setup>
  import { ref,computed } from 'vue'
  import { useStore } from 'vuex'
  import type { UploadInstance } from 'element-plus'
  
  const uploadRef = ref<UploadInstance>()
  
  const store = useStore()
  const user = computed(() => store.getters.getUser)
  const act_upload = computed(() => store.getters.getActLoad)
  const uploadData = () => {
    return {
      username: user.value.username,
      userId: user.value.userId,
      act_id:act_upload.value.act_id,
      // 添加其他需要上传的用户信息
    }
  }
  
  const submitUpload = () => {
    uploadRef.value!.submit()
  }
  </script>
  