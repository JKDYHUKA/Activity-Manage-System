<template>
  <div class="container">
    <div class="panel">
      <div class="content">
        <div class="switch">
          <h1 id="login">登录</h1>
        </div>
 
        <form action="">
 
          <div id="userName" class="input"><input type="text" placeholder="UserName"></div>
          <div id="password" class="input"><input type="password" placeholder="PassWord"></div>
 
          <div class="register-forget">
            <div id="signUp" class="input">跳转注册</div>
            <div id="forget" class="input">忘记密码？</div>
          </div>
          <button class="button">登录</button>
        </form>
      </div>
    </div>
  </div>
</template>
  
<script>
export default {
    name: 'LogInPage',
    data() {
      return {
        username: '',
        password: '',
        error: null,
      };
    },
    methods: {
      login() {
        // 这里处理登录逻辑，例如使用API与后端交互验证用户信息
        // 登录成功则跳转到其他页面，登录失败则显示错误信息
        // 示例中省略了实际的登录逻辑
        // 如果登录成功，可以使用this.$router.push('/dashboard')来跳转到仪表盘页面
        // 如果登录失败，可以设置this.error来显示错误信息
      },
    },
};
</script>
  
<style scoped>
.container {
    width: 24rem;
}
 
.panel {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
    background: rgba(0,0,0,.8);
    display: flex;
    justify-content: center;
    width: 400px;
    padding: 40px;
    box-sizing: border-box;
    box-shadow: 0 15px 25px rgba(0,0,0,.5);
    border-radius: 10px;
}
 
.switch h1 {
    text-align: center;
    font-size: 1.4rem;
    color: rgba(255, 255, 255,.8);
    border-bottom: rgba(255, 255, 255,.8) solid 2px;
    cursor: default;
}
 
.input input {
    outline: none;
    width: 100%;
    border: none;
    background: none;
    border-bottom: .1rem solid rgba(255, 255, 255,.8);
    color: rgba(37, 215, 202, 0.84);
    font-size: 1rem;
}
 
.input::after {
    content: attr(aria-placeholder);
    position: absolute;
    left: 0;
    top: -20%;
    font-size: 1.1rem;
    color: rgba(125, 116, 255, 0.44);
    transition: .3s;
}
 
.input.focus::after {
    top: -70%;
    font-size: 1rem;
}
 
.input#forget {
    color: #7d74ff;
    font-size: 0.8rem;
    text-decoration: none;
}
 
.input#forget:hover {
    color: #ffffff;
}
 
.input#signUp {
    color: #7d74ff;
    font-size: 0.8rem;
    text-decoration: none;
}
 
.input#signUp:hover {
    color: #ffffff;
}
 
form p {
    text-align: center;
}
 
form span {
    color: #7d74ff;
    font-size: 0.8rem;
    cursor: default;
}
 
form {
    width: 12rem;
    margin: 1rem 0 0;
}
 
form .input {
    position: relative;
    opacity: 1;
    width: 100%;
    margin: 2rem 0 0;
    height: 42px;
}
 
form .input#userName {
    margin: 3rem 0 0;
}
 
form .input#password {
    height: 1.6rem;
}
 
form button {
    display: block;
    border: none;
    outline: none;
    margin: 2rem 61px 0;
    width: 56px;
    height: 56px;
    border-radius: 50%;
    background: linear-gradient(90deg, #8a8fff, rgb(216, 174, 255));
    box-shadow: 0 0 8px #8a8fff;
    cursor: pointer;
}
 
form button:hover {
    border: none;
    outline: none;
    margin: 2rem -7px 0;
    width: 100%;
    height: 3.5rem;
    border-radius: 3rem;
    background: linear-gradient(90deg, rgba(138, 143, 255, 0.75), rgba(216, 174, 255, 0.75));
    box-shadow: 0 0 8px #8a8fff;
    cursor: pointer;
    color: rgba(0,0,0,0.6);
    transition: .4s;
}

.register-forget{
  display: flex;
}
</style>
  