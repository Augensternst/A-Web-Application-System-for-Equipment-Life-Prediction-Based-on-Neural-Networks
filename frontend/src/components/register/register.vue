<script setup lang="ts">
import {
  ElForm,
  ElFormItem,
  ElInput,
  ElCard,
  ElButton,
  ElMessage,
  ElAvatar,
  ElUpload,
  type UploadUserFile
} from "element-plus"
import type { FormInstance, FormRules } from 'element-plus'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import axiosInstance from "../../axios";
const avafile=ref()
const form = ref({
  username: '',
  password: '',
  email: '',
  phone: '',
  avatar: ''
})
const formRules = ref<FormRules>({
  username: [
    { required: true, message: '请输入用户名', trigger: 'blur' }
  ],
  password: [
    { required: true, message: '请输入密码', trigger: 'blur' }
  ],
  email: [
    { required: true, message: '请输入邮箱', trigger: 'blur' }
  ],
  phone: [
    { required: true, message: '请输入手机号', trigger: 'blur' }
  ],
  avatar: [
    { required: true, message: '请上传头像', trigger: 'blur' }
  ]
})

const formRef = ref<FormInstance | null>(null)
const router = useRouter()
const handleAvatarSuccess = (res: any, file: any) => {
  console.log("Ok!")
  form.value.avatar = URL.createObjectURL(file.raw)
}
const beforeAvatarUpload = (file: any) => {
  const isJPG = file.type === 'image/jpeg'
  const isPNG = file.type === 'image/png'
  const isGIF = file.type === 'image/gif'
  const isLt2M = file.size / 1024 / 1024 < 2

  if (!isJPG && !isPNG && !isGIF) {
    ElMessage.error('上传头像图片只能是 JPG/PNG/GIF 格式!')
  }
  if (!isLt2M) {
    ElMessage.error('上传头像图片大小不能超过 2MB!')
  }
  if((isJPG || isPNG || isGIF) && isLt2M){
    const render = new FileReader();
    render.onload = (e) => {
      form.value.avatar = e.target?.result as string
    }
    render.readAsDataURL(file)
    console.log("src: ",form.value.avatar)
    avafile.value = file
    return false;
  }
  return false;
}
const handleRemove = () => {
  form.value.avatar = ''
}
const register =async()=>{
  const url = '/user/register'
  const formData = new FormData()
  // 读取src文件
  const file = avafile.value
  console.log(avafile.value)
  formData.append('username', form.value.username)
  formData.append('password', form.value.password)
  formData.append('email', form.value.email)
  formData.append('phone', form.value.phone)
  formData.append('avatar', file as File)
  axiosInstance.post(url, formData).then((res) => {
    console.log(res.data)
    if (res.data.code === 200) {
      ElMessage.success('注册成功')
      router.push({
        path: "/login",
        replace: true
      });
    } else {
      ElMessage.error('注册失败: '+ res.data.message)
      console.log(res.data)
    }
  })
}
</script>
<template>
  <div>
    <el-card class="box-card" style="width: 500px;margin: 0 auto;">
      <el-form :model="form" :rules="formRules" ref="formRef" label-width="80px">
        <el-form-item label="用户名" prop="username">
          <el-input v-model="form.username"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-model="form.password" type="password"></el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="form.email"></el-input>
        </el-form-item>
        <el-form-item label="手机号" prop="phone">
          <el-input v-model="form.phone"></el-input>
        </el-form-item>
        <el-form-item label="头像" prop="avatar">
          <el-upload
              class="upload-demo"
              :onSuccess="handleAvatarSuccess"
              :beforeUpload="beforeAvatarUpload"
              :show-file-list="false"
              :onRemove="handleRemove"
          >
            <el-avatar :src="form.avatar" shape="circle" size="large">user</el-avatar>
          </el-upload>
        </el-form-item>
        <div class="btnGroup">
          <el-button type="primary" @click="register">注册</el-button>
          <router-link to="/login">
            <el-button style="margin-left:10px">登录</el-button>
          </router-link>
        </div>
      </el-form>
    </el-card>
  </div>

</template>