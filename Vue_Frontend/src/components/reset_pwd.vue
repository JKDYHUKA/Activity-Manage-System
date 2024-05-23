<template>
	<div class="login-register">
		<div class="contain">
			<div class="big-box" :class="{active:isTurn}">
				<div class="big-contain" key="bigContainLogin" v-if="isTurn">
					<div class="btitle">密码找回</div>
					<div class="bform">
						<input type="text" placeholder="用户名" v-model="form.username">
						<input type="phone_number" placeholder="电话" v-model="form.phone_number">
                        <div>
                            <button class="captcha_button" @click="getCaptcha">发送验证码</button>
                            <input type="text" v-model="form.input_captcha" class="captcha_input">
                        </div>
					</div>
					<button class="bbutton" @click="reset">重置密码</button>
				</div>
				<div class="big-contain" key="bigContainRegister" v-else>
					<div class="btitle">设置新密码</div>
					<div class="bform">
                        <input type="password" placeholder="密码" v-model="form.password1">
						<input type="password" placeholder="再次输入" v-model="form.password2">
					</div>
					<button class="bbutton" @click="resetpwd">确定</button>
				</div>
			</div>
			<div class="small-box" :class="{active:isTurn}">
				<div class="small-contain" key="smallContainRegister" v-if="isTurn">
					<div class="stitle">密码找回</div>

				</div>
				<div class="small-contain" key="smallContainLogin" v-else>
					<div class="stitle">设置新密码</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default{
		name:'login-register',
		data(){
			return {
				isTurn:true,
				emailError: false,
				passwordError: false,
				existed: false,
				form:{
					username:'',
					useremail:'',
					userpwd:'',
                    password1:'',
                    password2:'',
                    phone_number:'',
                    input_captcha: '',
				},
                received_captcha:' '
			}
		},
		methods:{
			changeType() {
				this.isTurn = !this.isTurn
				this.form.username = ''
				this.form.useremail = ''
				this.form.userpwd = ''
				this.form.input_captcha = ''
				this.form.phone_number = ''
			},
			reset(){
                if (this.received_captcha === this.form.input_captcha){
                    this.isTurn = !this.isTurn
                }
                else {
                    alert("验证码不对")
                }
				
			},
            resetpwd(){
                if (this.form.password1 === this.form.password2){
                    this.form.userpwd=this.form.password1
                    fetch('http://127.0.0.1:8000/api/submit_register_form/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({
                            username: this.form.username,
                            password: this.form.userpwd,
                        })
                    })
                    
                    .then(response => {
                        return response.json()
                    })
                    .then(data => {
                        alert(data.message)
                    })
                    .catch(error => {
                        console.error(error)
                    })
                }
                else {
                    alert("两次密码不同")
                }
            },
            getCaptcha(){
                fetch('http://127.0.0.1:8000/api/get_captcha/', {
                    method:'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        phone_number: this.form.phone_number
                    })
                })
                .then(response => {
                    return response.json()
                })
                .then(data => {
                    this.received_captcha = data.code
                })
                .catch(error => {
                    console.error("发送验证码出错", error)
                });
            },
		}
	}
</script>

<style scoped="scoped">
	.login-register{
		width: 100vw;
		height: 100vh;
		box-sizing: border-box;
	}
	.contain{
		width: 60%;
		height: 60%;
		position: relative;
		top: 50%;
		left: 50%;
		transform: translate(-50%,-50%);
		background-color: #fff;
		border-radius: 20px;
		box-shadow: 0 0 3px #f0f0f0,
					0 0 6px #f0f0f0;
	}
	.big-box{
		width: 70%;
		height: 100%;
		position: absolute;
		top: 0;
		left: 30%;
		transform: translateX(0%);
		transition: all 1s;
	}
	.big-contain{
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
	.btitle{
		font-size: 1.5em;
		font-weight: bold;
		color: rgb(57,167,176);
	}
	.bform{
		width: 100%;
		height: 40%;
		padding: 2em 0;
		display: flex;
		flex-direction: column;
		justify-content: space-around;
		align-items: center;
	}
	.bform .errTips{
		display: block;
		width: 50%;
		text-align: left;
		color: red;
		font-size: 0.7em;
		margin-left: 1em;
	}
	.bform input{
		width: 50%;
		height: 30px;
		border: none;
		outline: none;
		border-radius: 10px;
		padding-left: 2em;
		background-color: #f0f0f0;
	}
	.bbutton{
		width: 20%;
		height: 40px;
		border-radius: 24px;
		border: none;
		outline: none;
		background-color: rgb(57,167,176);
		color: #fff;
		font-size: 0.9em;
		cursor: pointer;
	}
	.small-box{
		width: 30%;
		height: 100%;
		background: linear-gradient(135deg,rgb(57,167,176),rgb(56,183,145));
		position: absolute;
		top: 0;
		left: 0;
		transform: translateX(0%);
		transition: all 1s;
		border-top-left-radius: inherit;
		border-bottom-left-radius: inherit;
	}
	.small-contain{
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
	.stitle{
		font-size: 1.5em;
		font-weight: bold;
		color: #fff;
	}
	.scontent{
		font-size: 0.8em;
		color: #fff;
		text-align: center;
		padding: 2em 4em;
		line-height: 1.7em;
	}
	.sbutton{
		width: 60%;
		height: 40px;
		border-radius: 24px;
		border: 1px solid #fff;
		outline: none;
		background-color: transparent;
		color: #fff;
		font-size: 1em;
		cursor: pointer;
		
	}
	
	.big-box.active{
		left: 0;
		transition: all 0.5s;
	}
	.small-box.active{
		left: 100%;
		border-top-left-radius: 0;
		border-bottom-left-radius: 0;
		border-top-right-radius: inherit;
		border-bottom-right-radius: inherit;
		transform: translateX(-100%);
		transition: all 1s;
	}
    .captcha_zone {
        display: flex;
        align-items: center;
    }

    .captcha_button {
        background-color: #007bff;
        color: white;
        padding: 8px 12px;
        cursor: pointer;
        margin-right: 10px;
        border-radius: 4px;
        user-select: none;
    }

    .captcha_button:hover {
        background-color: #0056b3;
    }

    .captcha_input {
        flex: 1;
        padding: 8px;
        border: 1px solid #ccc;
        border-radius: 4px;
    }
</style>
