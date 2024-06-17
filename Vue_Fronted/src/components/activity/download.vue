<template>
    <div>
      <button @click="downloadFile('file1.pdf')">下载文件1</button>
      <button @click="downloadFile('file2.jpg')">下载文件2</button>
    </div>
    <el-scrollbar height="250px">
        <p v-for="item in filenamelist" :key="item" 
        class="scrollbar-demo-item" @click="downloadFile(item)">
          {{ item }}
        </p>
    </el-scrollbar>
  </template>
   
  <script>
  import { mapGetters } from 'vuex'
  import { set_no_csrf_header } from '@/utils/httpUtils'
  export default {

    data(){
      return{
        filenamelist:[]//接受的内容为['a.txt','b.txt']
      }
    },
    computed: {
    ...mapGetters([
      'getActLoad',
    ])
    },
    methods: {
      getfilename(){
        fetch('http://127.0.0.1:8000/api/get_filename/', {
          method: 'POST',
          headers: set_no_csrf_header(),
          body: JSON.stringify({
            act_id:this.getActLoad,
          })
        })
        .then(response => {
            return response.json()
        })
        .then(data =>{
          this.filenamelist=data.filenamelist
        })
        .catch(error => {
            console.error(error)
        })
      },
      downloadFile(fileName) {
        const fileUrl = 'http://127.0.0.1:8000/api/download/' + this.getActLoad.act_id + '/' + fileName; // 文件的URL地址
        fetch(fileUrl)
          .then(response => response.blob())
          .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', fileName);
            document.body.appendChild(link);
            link.click();
          })
          .catch(error => {
            console.error(error);
          });
      }
    },
    created(){
      this.getfilename()
    }
  };
  </script>

<style scoped>
.scrollbar-demo-item {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 50px;
  margin: 10px;
  text-align: center;
  border-radius: 4px;
  background: var(--el-color-primary-light-9);
  color: var(--el-color-primary);
}
</style>