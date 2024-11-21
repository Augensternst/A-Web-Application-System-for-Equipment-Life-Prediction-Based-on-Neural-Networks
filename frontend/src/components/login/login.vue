<script setup lang="ts">
import {ref} from "vue";
import {useRouter} from "vue-router";
import {ElFormItem, ElForm, ElCard, ElButton, ElInput, ElMessage} from "element-plus";
import axiosInstance from "../../axios";
import type {FormInstance} from 'element-plus'
import {useAuth} from "../../composables/auth.ts"

const router = useRouter()
const auth = useAuth()
const formRef = ref<FormInstance | null>(null)
const fromRules = ref({
  username: [
    {required: true, message: '请输入用户名', trigger: 'blur'}
  ],
  password: [
    {required: true, message: '请输入密码', trigger: 'blur'}
  ]
})
const form = ref({
  username: '',
  password: '',
})


const login = async () => {
  if (!formRef.value) {
    ElMessage.error('请输入用户名和密码')
    return
  }
  await formRef.value?.validate((valid, _) => {
    if (valid) {
      const url = '/user/login'
      const data = {
        username: form.value.username,
        password: form.value.password
      }
      const headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
      axiosInstance.post(url, data, {headers}).then((res) => {
        if (res.data.code === 200) {
          ElMessage.success('登录成功')
          auth.setToken(res.data.data.token)
          router.push({
            path: "/home",
            replace: true
          });
        } else {
          ElMessage.error('登录失败，请检查用户名和密码')
          console.log(res.data)
        }
      })
    } else {
      ElMessage.error('登录失败，请检查用户名和密码')
    }
  })
}
</script>
<template>
  <div>
    <el-card class="box-card" style="width: 400px;margin: 100px auto;">
      <h2>登录</h2>
      <el-form ref="formRef" :model="form" :rules="fromRules" label-width="80px">
        <el-form-item label="用户名" prop="username">
          <el-input v-model="form.username"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-model="form.password" type="password"></el-input>
        </el-form-item>
        <div class="btnGroup">
          <el-button type="primary" @click="login">登录</el-button>
          <router-link to="/register">
            <el-button style="margin-left:10px">注册</el-button>
          </router-link>
        </div>
      </el-form>
    </el-card>
  </div>
</template>