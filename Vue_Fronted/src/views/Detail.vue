<template>
    <div>
      <div class="PersonTop">
        <div class="PersonTop_img">
          <img v-image-preview :src="avatar" />
        </div>
        <div class="PersonTop_text">
          <div class="user_text">
            <!-- <div class="user_name">
              <span> {{ nickname }} </span>
            </div>
            <div class="user-v" v-if="v === 3">
              <img src="@/assets/logo.png" class="user-v-img" />
              <span class="user-v-font">优质媒体作者</span>
            </div>
            <div class="user_qianming">
              <span> {{ design }}</span>
            </div>
            <div class="user_anniu">
              <el-button
                class="el-icon-edit"
                v-if="this.$route.params.id === this.$store.state.id"
                type="primary"
                size="medium"
                plain
                @click="edit"
                >编辑</el-button
              >
              <el-button
                v-else
                @click="follow"
                type="primary"
                size="medium"
                icon="el-icon-check"
                :text="isfollowid.indexOf(this.$route.params.id) > -1 ? '已关注' : '关注'">
                {{ isfollowid.indexOf(this.$route.params.id) > -1 ? '已关注' : '关注' }}
              </el-button>

            </div> -->
          </div>
          <!-- <div class="user_num">
            <div style="cursor: pointer" @click="myfan">
              <div class="num_number">{{ fanCounts }}</div>
              <span class="num_text">粉丝</span>
            </div>
            <div style="cursor: pointer" @click="myfollow">
              <div class="num_number">{{ followCounts }}</div>
              <span class="num_text">关注</span>
            </div>
            <div>
              <div class="num_number">{{ goodCounts }}</div>
              <span class="num_text">获赞</span>
            </div>
          </div> -->
        </div>
      </div>
      <div class="person_body">
        <div class="person_body_left">
          <el-card class="box-card" :body-style="{ padding: '0px' }">
            <div class="clearfix">
              <span class="person_body_list" style="border-bottom: none"
                >个人中心</span
              >
            </div>
            <!-- <div
              class="person_body_list"
              v-for="(item, index) in person_body_list"
              :key="index"
            >
              <router-link :to="{ name: item.name, params: item.params }">{{
                item.label
              }}</router-link>
            </div> -->
            <el-menu
              router
              active-text-color="#00c3ff"
              class="el-menu-vertical-demo"
            >
              <el-menu-item
                index="info"
                :route="{ name: 'info', params: { id: $route.params.id } }"
              >
                <i class="el-icon-user"></i>
                <span>个人简介</span>
              </el-menu-item>
              <el-menu-item
                index="activity"
                :route="{ name: 'activity', params: { id: $route.params.id } }"
              >
                <i class="el-icon-edit-outline"></i>
                <span>活动</span>
              </el-menu-item>
              <el-menu-item
                index="mycollect"
                :route="{ name: 'mycollect', params: $route.params.id }"
              >
                <i class="el-icon-document"></i>
                <span>收藏</span>
              </el-menu-item>
              <el-menu-item
                index="myfan"
                :route="{ name: 'myfan', params: $route.params.id }"
              >
                <i class="el-icon-tableware"></i>
                <span>粉丝</span>
              </el-menu-item>
              <el-menu-item
                index="myfollow"
                :route="{ name: 'myfollow', params: $route.params.id }"
              >
                <i class="el-icon-circle-plus-outline"></i>
                <span>关注</span>
              </el-menu-item>
            </el-menu>
          </el-card>
        </div>
        <div class="person_body_right">
          <router-view></router-view>
        </div>
      </div>
      <personal-dia ref="dia" @flesh="reload" />
    </div>
  </template>
  
  <script>
  
  
  </script>
  
  <style scoped>
  .me-video-player {
    background-color: transparent;
    width: 100%;
    height: 100%;
    object-fit: fill;
    display: block;
    position: fixed;
    left: 0;
    z-index: 0;
    top: 0;
  }
  .PersonTop {
    width: 1000px;
    height: 140px;
    padding-top: 20px;
    background-color: white;
    margin-top: 30px;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    border-radius: 5px;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.1),
                0 0 5px rgba(0, 0, 0, 0.1),
                0 0 5px rgba(0, 0, 0, 0.1),
                0 0 5px rgba(0, 0, 0, 0.1);
  }
  
  .PersonTop_img {
    width: 150px;
    height: 120px;
    background-color: #8c939d;
    margin-right: 24px;
    margin-left: 20px;
    overflow: hidden;
    border-radius: 20px;
  }
  
  .PersonTop_img img {
    width: 100%;
    height: 100%;
    border-radius: 20px;
  }
  
  .PersonTop_text {
    height: 120px;
    width: 880px;
    display: flex;
  }
  
  .user_text {
    width: 60%;
    height: 100%;
    line-height: 30px;
  }
  
  .user_name {
    font-weight: bold;
  }
  .user-v {
    margin-bottom: -5px;
  }
  .user-v-img {
    width: 15px;
    height: 15px;
  }
  .user-v-font {
    font-size: 15px;
    color: #00c3ff;
  }
  .user_qianming {
    font-size: 14px;
    color: #999;
  }
  
  .user_num {
    width: 40%;
    height: 100%;
    display: flex;
    align-items: center;
  }
  
  .user_num > div {
    text-align: center;
    border-right: 1px dotted #999;
    box-sizing: border-box;
    width: 80px;
    height: 40px;
    line-height: 20px;
  }
  
  .num_text {
    color: #999;
  }
  
  .num_number {
    font-size: 20px;
    color: #333;
  }
  .el-menu-item>span {
    font-size: 16px;
    color: #999;
  }
  
  /*下面部分样式*/
  .person_body {
    width: 1000px;
    margin-top: 210px;
    display: flex;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    border-radius: 5px;
  }
  
  .person_body_left {
    width: 27%;
    height: 600px;
    border-radius: 5px;
    margin-right: 3%;
    text-align: center;
  }
  
  .person_body_list {
    width: 100%;
    height: 50px;
    margin-top: 25px;
    font-size: 22px;
    border-bottom: 1px solid #f0f0f0;
    background-image: -webkit-linear-gradient(
      left,
      rgb(42, 134, 141),
      #e9e625dc 20%,
      #3498db 40%,
      #e74c3c 60%,
      #09ff009a 80%,
      rgba(82, 196, 204, 0.281) 100%
    );
    -webkit-text-fill-color: transparent;
    -webkit-background-clip: text;
    -webkit-background-size: 200% 100%;
    -webkit-animation: masked-animation 4s linear infinite;
  }
  
  .el-menu-item {
    margin-top: 22px;
  }
  
  .person_body_right {
    width: 70%;
    /* height: 500px; */
    border-radius: 5px;
    background-color: white;
  }
  
  .box-card {
    height: 500px;
  }
  
  /*ui样式*/
  .el-button {
    width: 84px;
  }
  </style>