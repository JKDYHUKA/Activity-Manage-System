<template>
    <div class="container">
      <div class="sidebar">
        <el-form
        ref="ruleFormRef"
          style="max-width: 600px"
          :model="ruleForm"
          :rules="rules"
          label-width="auto"
          class="demo-ruleForm"
          :size="formSize"
          status-icon
        >
            <el-form-item label="支出" prop="cost_out">
                <el-input v-model="ruleForm.cost_out"/>
            </el-form-item>
            <el-form-item label="入账" prop="cost_in">
                <el-input v-model="ruleForm.cost_in"/>
            </el-form-item>
            <el-form-item label="交易类型" prop="Type">
                <el-segmented :options="UserOptions" v-model="ruleForm.Type" />
              </el-form-item>
            <el-form-item label="相关描述" prop="description">
                <el-input type="textarea" v-model="ruleForm.description"/>
            </el-form-item>
            
            <el-upload
              ref="uploadRef"
              class="upload-demo"
              action="http://127.0.0.1:8000/api/upload/"
              :auto-upload="false"
              :data="uploadData"
            >
              <template #trigger>
                <el-button type="primary">上传报销凭证</el-button>
              </template>
            </el-upload>
            <el-form-item>
              <el-button type="primary" @click="submitForm(ruleFormRef)">
                提交
              </el-button>
              <el-button @click="resetForm(ruleFormRef)" >重置</el-button>
              <el-button @click="backButton" >返回</el-button>
          </el-form-item>
        </el-form>
      </div>
    </div>
</template>

<script lang="ts" setup>
import { ElMessage } from 'element-plus'
import { ref, reactive,VNode, VNodeProps, onMounted } from 'vue'
import type { ComponentSize, FormInstance, FormRules,UploadInstance } from 'element-plus'
import { set_no_csrf_header } from '@/utils/httpUtils'



// const disabledDate = (time: Date) => {
//   return time.getTime() < Date.now()
// }
interface RuleForm {
    cost_in:number,
    cost_out:number,
    description:string,
    Type:string,
}

const formSize = ref<ComponentSize>('default')
const ruleFormRef = ref<FormInstance>()
const ruleForm = reactive<RuleForm>({
    cost_in:0,
    cost_out:0,
    description:"",
    Type:"",
});

const uploadRef = ref<UploadInstance>()

const UserOptions = ['资源购买', '场地租赁','其他']
const userid_str: string[]=[]
const usertype_str: string[]=[]

const now = new Date()

const tableData = ref([{}])




const backButton = () => {
  window.history.back();
}

//rule
const rules = reactive<FormRules<RuleForm>>({
  Type: [
    { required: true, message: 'Please input Type', trigger: 'blur' },

  ],

})

var url = window.location.href ;  
var cs_arr = url.split('/');
// console.log(cs_arr[4])
const uploadData = () => {
    return {
        act_id: cs_arr[5],
      // 添加其他需要上传的用户信息
    }
}

const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return
  await formEl.validate((valid, fields) => {
    if (valid) {
      console.log('submit!')
      uploadRef.value!.submit()
      fetch('http://127.0.0.1:8000/api/update_cost/', {
        method: 'POST',
        headers: set_no_csrf_header(),
        body: JSON.stringify({
        act_id:cs_arr[5],
        cost_in:ruleForm.cost_in,
        cost_out:ruleForm.cost_out,
        description:ruleForm.description,
        Type:ruleForm.Type,
        userid_str:cs_arr[4],
        })
      })
      .then(response => {
          return response.json()
      })
      .then(data => {
          alert(data.message)
          window.history.back();
      })
      .catch(error => {
          console.error(error)
      })
    } else {
      console.log('error submit!', fields)
    }
  })
}

const resetForm = (formEl: FormInstance | undefined) => {
  if (!formEl) return
  formEl.resetFields()
}
const options = Array.from({ length: 10000 }).map((_, idx) => ({
  value: `${idx + 1}`,
  label: `${idx + 1}`,
}))

</script>

<style scoped="scoped">
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
.sidebar {
  flex: 1;
  display: inline-block;
  max-width: 600px;
  padding: 30px;
  background-color: #f2f2f2;
  border-radius: 10px;
}
.places {
  display: flex;
  justify-content: center;
}
.main-content {
  display: inline-block;
  flex: 1;
  background-color: #fff;
}
.my-border {
    border: 1px solid white;
    margin-left: 100px;
}
</style>
