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
          <el-form-item label="活动主题" prop="act_name">
              <el-input v-model="ruleForm.act_name"/>
          </el-form-item>
          <el-form-item label="活动描述" prop="act_describe">
              <el-input type="textarea" v-model="ruleForm.act_describe" />
          </el-form-item>

          <el-form-item label="活动时间1" prop="act_time1">
            <div class="block">
              <el-date-picker
                v-model="act_time1"
                type="datetimerange"
                :disabled-date="disabledDate"
                range-separator="To"
                start-placeholder="Start date"
                end-placeholder="End date"
              />
            </div>
          </el-form-item>

          <el-form-item label="活动时间2" prop="act_time2">
            <div class="block">
              <el-date-picker
                v-model="act_time2"
                type="datetimerange"
                :disabled-date="disabledDate"
                range-separator="To"
                start-placeholder="Start date"
                end-placeholder="End date"
              />
            </div>
          </el-form-item>

          <el-form-item label="活动时间3" prop="act_time3">
            <div class="block">
              <el-date-picker
                v-model="act_time3"
                :disabled-date="disabledDate"
                type="datetimerange"
                range-separator="To"
                start-placeholder="Start date"
                end-placeholder="End date"
              />
            </div>
          </el-form-item>
          
          <el-form-item label="活动地点要求" prop="act_demand">
              <el-segmented :options="locationOptions" v-model="ruleForm.act_demand" />
          </el-form-item>
          <el-form-item label="参会人员" prop="act_userId">
              <el-input v-model="ruleForm.act_userId" />
              <el-form-item label="活动人员类型" prop="act_usertype">
                <el-segmented :options="UserOptions" v-model="ruleForm.act_usertype" />
              </el-form-item>
              <el-button class="mt-4" style="width: 240" @click="onAddItem">
                添加至名单
              </el-button>
          </el-form-item>
          
          <el-upload
            ref="uploadRef"
            class="upload-demo"
            action="https://run.mocky.io/v3/9d059bf9-4660-45f2-925d-ce80ad6c4d15"
            :auto-upload="false"
            :data="uploadData"
          >
            <template #trigger>
              <el-button type="primary">select file</el-button>
            </template>
          </el-upload>
          <el-form-item label="预算" prop="act_budget">
              <el-input v-model="ruleForm.act_budget" />
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="submitForm(ruleFormRef)">
              提交
            </el-button>
            <el-button @click="resetForm(ruleFormRef)" >重置</el-button>
        </el-form-item>
      </el-form>
    </div>
    <div class="places" >
        
    </div>
    <div class="main-content">
      <el-card style="max-width: 100%">
        <p class="text item">0-50人教室:{{placenum[0]}}</p>
        <p class="text item">50-100人教室:{{placenum[1]}}</p>
        <p class="text item">100-200人教室:{{placenum[2]}}</p>
      </el-card>
      <div style="width: 400" class="my-border">
        <el-table :data="tableData" style="width: 100%" max-height="250">
          <el-table-column prop="userid" label="人员列表" width="120" />
          <el-table-column prop="usertype" label="人员类型" width="120" />
          <el-table-column fixed="right" label="Operations" width="120">
            <template #default="scope">
              <el-button
                link
                type="primary"
                size="small"
                @click.prevent="deleteRow(scope.$index)"
              >
                Remove
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ElMessage } from 'element-plus'
import { ElNotification } from 'element-plus'
import { ref, reactive,VNode, VNodeProps, onMounted } from 'vue'
import type { ComponentSize, FormInstance, FormRules,UploadInstance } from 'element-plus'
import { set_no_csrf_header } from '@/utils/httpUtils'

const uploadData = () => {
    return {
      act_name:ruleForm.act_name,
      // 添加其他需要上传的用户信息
    }
  }

const disabledDate = (time) => {
  const sevenDaysLater = new Date();
  sevenDaysLater.setDate(sevenDaysLater.getDate() + 2);
  const tomorrow = new Date();
  tomorrow.setDate(tomorrow.getDate() + 1); 
  return time.getTime() > sevenDaysLater.getTime() || time.getTime() < tomorrow.getTime();
};
interface RuleForm {
    act_name:string,
    act_describe:string,
    act_demand:string,
    act_userId:string,
    act_usertype:string,
    act_budget:string,
    inti:number
}

var placenum = ref([0, 0, 1]);
onMounted(()=>{
  GetPlace(placenum)
  console.log(placenum)
});
function GetPlace(item:any){
  fetch('http://127.0.0.1:8000/api/get_place/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(res => {
    return res.json()
  })
  .then(data => {  
    item.value=data.place_num 
    return item.value
  })
}
  
const formSize = ref<ComponentSize>('default')
const ruleFormRef = ref<FormInstance>()
const ruleForm = reactive<RuleForm>({
    act_name:"",
    act_describe:"",
    act_demand:"",
    act_userId:"",
    act_usertype:"参会人员",
    act_budget:"",
    inti:0,
});

const uploadRef = ref<UploadInstance>()

const act_time1 = ref<[Date, Date]>()
const act_time2 = ref<[Date, Date]>()
const act_time3 = ref<[Date, Date]>()
const locationOptions = ['0-50', '50-100', '100-200']
const UserOptions = ['参会人员', '嘉宾']
const userid_str: string[]=[]
const usertype_str: string[]=[]


const now = new Date()

const tableData = ref([{}])

const deleteRow = (index: number) => {
  tableData.value.splice(index, 1)
}

const onAddItem = () => {
  const personal_number = ruleForm.act_userId
  fetch('http://127.0.0.1:8000/api/get_user_by_personal_number/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      userId: personal_number
    })
  })
  .then(res => {
    return res.json()
  })
  .then(data => {
    if (data.code === '0'){
      now.setDate(now.getDate() + 1)
      userid_str[ruleForm.inti]=ruleForm.act_userId
      usertype_str[ruleForm.inti]=ruleForm.act_usertype
      ruleForm.inti=ruleForm.inti+1
      tableData.value.push({
        userid: data.username,
        usertype:ruleForm.act_usertype,
      })
    }
    else{
      alert(data.message)
    }
  })
  
  
}

//rule
const rules = reactive<FormRules<RuleForm>>({
  act_name: [
    { required: true, message: 'Please input Activity name', trigger: 'blur' },

  ],
  act_demand: [
    { required: true, message: 'Please input Activity demand', trigger: 'blur' },

  ],

})
const open1 = () => {
  ElNotification({
    title: 'Success',
    message: '创建活动成功',
    type: 'success',
  })
}
const submitForm = async (formEl: FormInstance | undefined) => {
  if (!formEl) return
  await formEl.validate((valid, fields) => {
    if (valid) {
      console.log('submit!')
      uploadRef.value!.submit()
      fetch('http://127.0.0.1:8000/api/create_new_activity/', {
        method: 'POST',
        headers: set_no_csrf_header(),
        body: JSON.stringify({
          name:ruleForm.act_name,
          activity_describe:ruleForm.act_describe,
          activity_level:ruleForm.act_demand,
          activity_budget:ruleForm.act_budget,
          activity_type: 'meeting',
          time1:act_time1,
          time2:act_time2,
          time3:act_time3,
          userid_str:userid_str,
          usertype_str:usertype_str,
        })
      })
      .then(response => {
          return response.json()
      })
      .then(data => {
          // alert(data.message);
          open1();
          window.location.href = "http://localhost:8080/";
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
}
.sidebar {
  flex: 1;
  display: inline-block;
  background-color: #f2f2f2;
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
