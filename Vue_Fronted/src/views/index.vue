<template>
  <div>

      <p>主页</p>
  </div>
  <button @click="toDetailPage">
    用户详情
  </button>


</template>

<script>
import { isTokenExpired } from "../utils/httpUtils.js"
import { set_post_header } from "../utils/httpUtils.js"
import { mapActions } from "vuex"
export default{
  name: "HomePage",
  data(){
    return {
        userId:'',
        username: '',
        phone_number: '',
        nickname:'',
        email: '',
    }
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
            
        }, 1000); // 1秒延迟
        }
    },
    methods: {
        toDetailPage(){
            const userId = this.userId;
            this.$router.push({
                path: `/detail/info/${userId}`
            })
        },
        ...mapActions(['updateUser']),
    }

}

</script>

