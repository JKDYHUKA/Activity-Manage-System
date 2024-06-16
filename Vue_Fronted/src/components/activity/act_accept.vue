<template>
  <div class="person_body_right" v-for="item in notice_Array">
    <div class="everyone" v-if="item.act_name && isVisible&&!item.is_choose" @click="hideDivs(item)">
      <div class="div-inline-block-left">{{ item.act_name }}</div>
      <div class="div-inline-block-right">{{ item.notice_title }}</div>
    </div>
  </div>
  <div v-if="!isVisible">
    <el-container>
      <el-header style="border: 1px solid black;height: 33px;">
        <el-button @click="isVisible=true">back</el-button>
        {{ clickedItem.act_name }}
      </el-header>
      <el-main style="border: 1px solid black;padding: 10px">
          <div>
            <span>活动描述:</span>
            {{ clickedItem.notice_content }}
          </div>
          <div v-if="clickedItem.notice_title==='Invitation'">
            <span>邀请你参加</span>
            <span class="p-name">{{clickedItem.act_name}}</span>
            <span>是否接受  </span>
            <el-button @click="actAccept(clickedItem)" size="small">
              <el-icon size="20px"><Check /></el-icon>
            </el-button>
            <el-button @click="actRefuse(clickedItem)" size="small">
              <el-icon size="20px"><Close /></el-icon>
            </el-button>
          </div>

          <div v-if="clickedItem.notice_title==='Feedback'">
            <el-form-item label="活动人员类型" >
              <el-segmented :options="UserOptions" v-model="questionnaire.usertype"/>
            </el-form-item>
            <div class="demo-rate-block">
              <span class="demonstration">为活动打分</span>
              <el-rate v-model="questionnaire.rate" />
            </div>
            <span class="demonstration">建议：</span>
            <el-input
              v-model="questionnaire.suggestion"
              style="width: 240px"
              :rows="2"
              type="textarea"
              placeholder="Please input"
            />
            <br/>
            <el-button @click="SubQuestionnaire()">提交</el-button>
          </div>
      </el-main>
    </el-container>
  </div>
</template>
  
  <script>
  import { mapGetters } from 'vuex';
  import { set_no_csrf_header } from '@/utils/httpUtils'
  export default{
    data(){
      return {
        isVisible: true,
        clickedItem : null,
        act_type:"",
        UserOptions : [],
        notice_Array: [
          { act_name: "11", notice_content: "22",notice_type:"",notice_title:"Feedback", notice_id: "111", act_accept: null, is_choose:false }
        ],
        questionnaire:{userid:"",usertype:"",rate:"",suggestion:"",notice_id:""}
      }
      
    },
    computed: {
    ...mapGetters([
      'getUsername',
      'getUserId',
    ])
    },
    methods:{
      SubQuestionnaire(){
        this.isVisible=true;
        fetch('http://127.0.0.1:8000/api/get_ActivityType/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
              userid:this.questionnaire.userid,
              usertype:this.questionnaire.usertype,
              rate:this.questionnaire.rate,
              suggestion:this.questionnaire.suggestion,
              notice_id:this.questionnaire.notice_id,
            })
        })       
        .then(response => {
            return response.json()
        })
        .catch(error => {
            console.error(error)
        })
      },
      GetType(){
        fetch('http://127.0.0.1:8000/api/get_ActivityType/', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id: this.clickedItem.notice_id,
                userid: this.getUserId,
            })
        })       
        .then(response => {
            return response.json()
        })
        .then(data=>{
            this.act_type=data.activity_type
            if(this.act_type==="meeting"){
              this.UserOptions = ['参会人员', '嘉宾']
            }else if(this.act_type==="contact"){
              this.UserOptions = ['参与人员']
            }
            else if(this.act_type==="customize"){
              this.UserOptions = ['参会人员', '嘉宾']
            }else if(this.act_type==="interview"){
              this.UserOptions = ['答辩学生', '评审老师']
            }else if(this.act_type==="seminar"){
              this.UserOptions = ['参会人员', '嘉宾']
            }
        })
        .catch(error => {
            console.error(error)
        })
      },
      hideDivs(item) {
        this.isVisible = false;
        this.clickedItem = item;
        this.questionnaire.notice_id=this.clickedItem.notice_id;
        this.questionnaire.userid=this.getUserId;
        this.GetType();
      },
      actAccept(item){
        item.is_choose=true;
        item.act_accept=true;
        this.isVisible=true;
        fetch('http://127.0.0.1:8000/api/accept_invitation/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                id: this.clickedItem.notice_id,
                userid: this.getUserId,
                content: this.clickedItem.notice_content,
            })
        })
        
        .then(response => {
            return response.json()
        })
        .catch(error => {
            console.error(error)
        })
      },
      actRefuse(item){
        item.is_choose=true;
        item.act_accept=false;
        this.isVisible=true;
        fetch('http://127.0.0.1:8000/api/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                act_username:this.getUsername,
                act_name: clickedItem.act_name,
                act_accept: clickedItem.act_accept,
            })
        })
        
        .then(response => {
            return response.json()
        })
        .catch(error => {
            console.error(error)
        })
      },
      fetchNotices() {
      fetch('http://127.0.0.1:8000/api/get_notices/', {
        method: 'GET',
        headers:set_no_csrf_header(),
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('网络响应错误');
        }
        return response.json();
      })
      .then(data => {
        this.notice_Array = data.notice_details;
      })
      .catch(error => {
        console.error('获取数据失败:', error);
      });
    }
    },
    created(){
      this.fetchNotices()
  
    }
  }
  
  </script>
  
  <style scoped="scoped">
.div-inline-block-left {
  display: inline-block;
  width: 80%; /* 或者你需要的宽度 */
  justify-content: center;
  align-items: center;
  text-align: left; /* 左对齐 */
  padding: 10px; /* 设置内边距，你可以根据需要调整这个值 */
  border-right: 2px solid black;
}

.div-inline-block-right {
  display: inline-block;
  width: 20%; /* 或者你需要的宽度 */
  justify-content: center;
  align-items: center;
  text-align: right; /* 右对齐 */
  padding: 10px; /* 设置内边距，你可以根据需要调整这个值 */
}

  .everyone {
  width: 100%;
  height:60px;
  margin-top: 0px;
  margin-bottom: 20px;
  border-radius: 5px;
  display: flex;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1),
              0 0 5px rgba(0, 0, 0, 0.1),
              0 0 5px rgba(0, 0, 0, 0.1),
              0 0 5px rgba(0, 0, 0, 0.1);
  }

  </style>
  