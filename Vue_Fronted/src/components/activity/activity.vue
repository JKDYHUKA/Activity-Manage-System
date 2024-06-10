<template>
    <div class="module" id="div1">
        <el-button @click="expand('div1')">我参加的活动</el-button>
        <el-button @click="back">back</el-button>
        <act_join></act_join>
    </div>
    <div class="module" id="div2">
        <el-button @click="expand('div2')">2</el-button>
        <el-button @click="back">back</el-button>
        <act_all></act_all>
    </div>
    <div class="module" id="div3">
        <el-button @click="expand('div3')">我创建的活动</el-button>
        <el-button @click="back">back</el-button>
        <act_mycreate></act_mycreate>
    </div>
    <div class="module" id="div4">
        <el-button @click="expand('div4')">通知</el-button>
        <el-button @click="back">back</el-button>
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