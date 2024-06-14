<template>
    <!-- <div> -->
      <div class="PersonTop">
        <div class="PersonTop_img">
          <img src=../assets/top.png />
        </div>
        <div class="PersonTop_text">
          <div class="user_text">
            <!-- <el-button>sad</el-button> -->
          </div>
          
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
            <el-menu
              router
              active-text-color="#00c3ff"
              class="el-menu-vertical-demo"
            >
              <el-menu-item
                
                @click="toDetailPage"
              >
                <i class="el-icon-user"></i>
                <span>个人简介</span>
              </el-menu-item>
              <el-menu-item
                @click="toActivityPage"
              >
                <i class="el-icon-edit-outline"></i>
                <span>活动</span>
              </el-menu-item>
              <el-menu-item
                index="creation"
                :route="{ name: 'creation', params: $route.params.id }"
              >
                <i class="el-icon-document"></i>
                <span>创建活动</span>
              </el-menu-item>
              <el-menu-item @click="goToLogin">
                <i class="el-icon-tableware"></i>
                <span>退出登录</span>
              </el-menu-item>
              <el-menu-item @click="manage_activities"
              >
                <i class="el-icon-circle-plus-outline"></i>
                <span>审批测试</span>
              </el-menu-item>
              
            </el-menu>
          </el-card>
        </div>
        <div class="person_body_right" v-if="isRendered">
          <router-view></router-view>
          <!-- <activity></activity> -->
        </div>
      </div>
      <personal-dia ref="dia" @flesh="reload" />
    <!-- </div> -->
  </template>
  
  <script>
  import activity from '@/components/activity/activity.vue'
  import { isTokenExpired } from "../utils/httpUtils.js"
  import { set_post_header } from "../utils/httpUtils.js"
  import { mapActions } from "vuex"
  export default{
    data(){
      return {
        userId:'',
        username: '',
        phone_number: '',
        nickname:'',
        email: '',
        isRendered: false,
    }
      
    },
    components:{
      activity
    },
    created() {
    const jwtToken = localStorage.getItem("jwtToken");
    const csrfToken = localStorage.getItem("csrfToken");

    if (!jwtToken || !csrfToken) {
        //如果这两个token有一个为空，则跳到登录页面（一般都是两个同时为空）
        console.log("强桑修改这里1");
      }

      const code = '1';

    if (isTokenExpired()) {
        //令牌过期，跳转到登录模块
        console.log("强桑修改这里2");
    } 
    else {
        setTimeout(() => {
            fetch('http://127.0.0.1:8000/api/verify_token/', {
              method: 'GET',
              headers: set_post_header(),
            })
            .then(res => {
              return res.json();
            })
            .then(data => {
              console.log(data.message);
              const userData = {
                userId: data.personal_number,
                username: data.username,
                nickname: data.nickname,
                phone_number: data.phone_number,
                email: data.email,
              }
              this.userId = data.personal_number;
              this.username = data.username;
              this.updateUser(userData)
            });
            
        }, 500); // 1秒延迟
        }
    },
    methods: {
        goToLogin(){
          fetch('http://127.0.0.1:8000/api/user_logout/', {
            method: 'POST',
            headers: set_post_header()
          })
          .then(res => {
            return res.json()
          })
          .then(data => {
            localStorage.removeItem('jwtToken');
            localStorage.removeItem('csrfToken');
            localStorage.removeItem('tokenExpiration')

            this.$router.push({
                path: `/login`
            })
          }) 
        },
        toActivityPage(){
            const userId = this.userId;
            this.$router.push({
                path: `/activity/${userId}`
            })
        },
        toDetailPage(){
            const userId = this.userId;
            this.$router.push({
                path: `/info/${userId}`
            })
        },
        manage_activities(){
          fetch('http://127.0.0.1:8000/api/api_test/', {
            method: 'GET'
          })
        },
        ...mapActions(['updateUser']),
    },
    mounted() {
      setTimeout(() => {
        this.isRendered = true;
      }, 500);
    },
  }
  </script>
  
  <style scoped="scoped">
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
    width: 100%;
    height: 60px;
    padding-top: 20px;
    background-color: white;
    margin-top: -7px;
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
    width: 175px;
    height: 55px;
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
    width: 100%;
    margin-top: 80px;
    height: 84vh;
    display: flex;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    border-radius: 5px;
  }
  
  .person_body_left {
    width: 10%;
    border-radius: 5px;
    text-align: center;
  }
  
  .person_body_list {
    width: 100%;
    height: 100%;
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
    width: 100%;
    /* height: 500px; */
    overflow: auto;
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