<template>
    <div>
      <el-card>
        <el-descriptions class="margin-top" title="简介" :column="2" border>
          <template #extra>
            <!-- <el-button v-if="$route.params.id === $store.state.id" type="primary" size="small">操作</el-button> -->
            <el-button type="primary" size="small">操作</el-button>
          </template>
          <el-descriptions-item label="头像">
            <img class="img" :src="avatar" alt="Failed" />
          </el-descriptions-item>
          <el-descriptions-item label="账户名">{{ username }}</el-descriptions-item>
          <el-descriptions-item label="昵称">{{ nickname }}</el-descriptions-item>
          <el-descriptions-item label="年龄">{{ age }}</el-descriptions-item>
          <el-descriptions-item label="性别">
            <el-tag size="small">{{ sex }}</el-tag>
          </el-descriptions-item>
          <el-descriptions-item label="邮箱Email">{{ email }}</el-descriptions-item>
          <el-descriptions-item label="手机号码">{{ mobilePhoneNumber }}</el-descriptions-item>
          <el-descriptions-item label="地区">{{ area }}</el-descriptions-item>
          <el-descriptions-item label="职业">{{ work }}</el-descriptions-item>
          <el-descriptions-item label="兴趣爱好">{{ hobby }}</el-descriptions-item>
          <el-descriptions-item label="个性签名">{{ design }}</el-descriptions-item>
          <el-descriptions-item label="注册日期">{{ createDate  }}</el-descriptions-item>
        </el-descriptions>
      </el-card>
    </div>
  </template>
  
  <script>
  import { set_post_header } from "../utils/httpUtils.js"
  export default {
    data(){
        return {
            userId:this.$route.params.id,
            username:"",
            nickname:"",
            age:"",
            sex:"",
            email:"",
            mobilePhoneNumber:"",
            area:"",
            work:"",
            hobby:"",
            design:"",
            createDate:"",
        }
    },
    created(){
        fetch('http://127.0.0.1:8000/api/get_user_detail/', {
                method: 'GET',
                headers: set_post_header(),    
            })
            .then(res => {
                return res.json()
            })
            .then(data => {
                this.username = data.username;
                this.nickname = data.nickname;
                this.email = data.email;
                this.mobilePhoneNumber = data.phone_number;
            })
    },

  }
  </script>