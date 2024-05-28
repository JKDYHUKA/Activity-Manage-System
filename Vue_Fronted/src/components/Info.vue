<template>
    <div>
      <el-card>
        <el-descriptions class="margin-top" title="简介" :column="2" border>
          <template #extra>
            <el-button v-if="$route.params.id === $store.state.id" type="primary" size="small">操作</el-button>
          </template>
          <el-descriptions-item label="头像">
            <img class="img" :src="avatar" alt="" />
          </el-descriptions-item>
          <el-descriptions-item label="账户名">{{ account }}</el-descriptions-item>
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
  import { ref, onMounted } from "vue";
  
  export default {
    name: "Info",
    setup() {
      const avatar = ref("");
      const account = ref("");
      const age = ref(0);
      const email = ref("");
      const mobilePhoneNumber = ref("");
      const area = ref("");
      const createDate = ref(0);
      const nickname = ref("");
      const sex = ref("");
      const work = ref("");
      const hobby = ref("");
      const design = ref("");
  
      onMounted(() => {
        userInfo($route.params.id)
          .then((res) => {
            avatar.value = res.data.avatar;
            account.value = res.data.account;
            age.value = res.data.age;
            email.value = res.data.email;
            mobilePhoneNumber.value = res.data.mobilePhoneNumber;
            area.value = res.data.area;
            createDate.value = res.data.createDate;
            nickname.value = res.data.nickname;
            sex.value = res.data.sex === 1 ? "男" : "女";
            work.value = res.data.work;
            design.value = res.data.design;
            hobby.value = res.data.hobby;
          })
          .catch((err) => {
            console.error("Error fetching user info:", err);
          });
      });
  
      return {
        avatar,
        account,
        age,
        email,
        mobilePhoneNumber,
        area,
        createDate,
        nickname,
        sex,
        work,
        hobby,
        design,
      };
    },
  };
  </script>
  