<template>
    <div class="module" id="div1">
        <div style="position: sticky;top:0">
          <el-button @click="expand('div1')">我参加的活动</el-button>
          <el-button @click="back">back</el-button>
        </div>
        <act_join></act_join>
    </div>
    <div class="module" id="div2">
      <div style="position: sticky;top:0">
        <el-button @click="expand('div2')">活动详情</el-button>
        <el-button @click="back">back</el-button>
      </div>
      <act_all></act_all>
    </div>
    <div class="module" id="div3">
      <div style="position: sticky;top:0">
        <el-button @click="expand('div3')">我创建的活动</el-button>
        <el-button @click="back">back</el-button>
      </div>
      <act_mycreate></act_mycreate>
    </div>
    <div class="module" id="div4">
      <div style="position: sticky;top:0">
        <el-button @click="expand('div4')">通知</el-button>
        <el-popover placement="right" :width="400" trigger="click" :visible="visible">
          <template #reference>
            <el-button type="primary" style="margin-right: 16px" @click="visible = true">创建日程提醒</el-button>
          </template>
          
          <div class="block">
            <span class="demonstration">提醒日期：</span>
            <el-date-picker
              v-model="time_value"
              type="datetime"
              placeholder="Select date and time"
              @change="handleDateChange"
            />
          </div>
          <span class="demonstration">消息内容：</span>
          <el-input
            v-model="textarea"
            style="width: 240px"
            :rows="2"
            type="textarea"
            placeholder="Please input"
          />
          <br/>
          <el-button size="small" text @click="visible = false">cancel</el-button>
          <el-button @click="set_reminder()">提交</el-button>
        </el-popover>
        <el-button @click="back">back</el-button>
      </div>
      <act_accept></act_accept>
    </div>
</template>

<script>
  import test from './test.vue'
  import act_join from './act_join.vue'
  import act_accept from './act_accept.vue'
  import act_mycreate from './act_mycreate.vue'
  import act_all from './act_all.vue'
  export default{
    data(){
      return {
        visible:false,
        time_value: '',
        textarea:'',
      }
      
    },
    components:{
      test,
      act_join,
      act_mycreate,
      act_accept,
      act_all
    },
    methods:{
      handleDateChange(value) {
        console.log("Selected Date and Time: ", value);
        this.time_value = value;
      },
      expand(divId) {
        var contents = document.getElementsByClassName('module');
        for (var i = 0; i < contents.length; i++) {
          contents[i].style.display = 'none';
        }
        document.getElementById(divId).style.display = 'block';
        var div = document.getElementById(divId);
        div.style.width = '96%';
        div.style.height = '96%';
      },
      back() {
        var contents = document.getElementsByClassName('module');
        for (var i = 0; i < contents.length; i++) {
          contents[i].style.display = 'block';
          contents[i].style="module"
        }
      },
      set_reminder(){

        this.visible = false,
        fetch('http://127.0.0.1:8000/api/set_reminder', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            time: this.time_value,
            text:this.textarea,
          })
        })
        .then(res => {
          return res.json()
        })
      }
    },
    created(){
    }
  }
  </script>

<style scoped="scoped">
  .module{
    display: inline-block;
    width: 48%;
    height: 48%;
    border-radius: 5px;
    margin-left: 10px;
    margin-bottom: 10px;
    overflow: auto;
    transition: width 0.5s ease-in-out,height 0.5s ease-in-out;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.1),
                0 0 5px rgba(0, 0, 0, 0.1),
                0 0 5px rgba(0, 0, 0, 0.1),
                0 0 5px rgba(0, 0, 0, 0.1);
  }


</style>