<template>
  <body id="poster">
    <!-- <el-row class="login-wrap">
      hhhhhhss
    </el-row>  -->
    <div class="login-wrap">
      <el-form class="login-container" label-position="left" label-width="0px">
        <h3 class="login_title">后台系统管理登录</h3>
        <el-form-item>
          <el-input
            type="text"
            v-model="loginForm.username"
            auto-complete="off"
            placeholder="账号"
          ></el-input>
        </el-form-item>
        <el-form-item>
          <el-input
            type="password"
            v-model="loginForm.password"
            auto-complete="off"
            placeholder="密码"
          ></el-input>
        </el-form-item>
        <el-form-item style="width: 100%">
          <el-button
            type="primary"
            style="width: 100%;background: #505458;border: none"
            v-on:click="login"
            >登录</el-button
          >
        </el-form-item>
      </el-form>
    </div>
  </body>
</template>

<script>
export default {
  name: 'BackLogin',
  data () {
    return {
      career: 0,
      uid: 0,
      loginForm: {
        username: '',
        password: ''
      },
      responseResult: [],
      status
    }
  },
  methods: {
    login () {
      var _this = this
      if (!this.loginForm.username) {
        this.$message.error('用户名不能为空')
        return
      }
      if (!this.loginForm.password) {
        this.$message.error('密码不能为空')
        return
      }
      this.$axios
        .post('/back/login', {
          username: this.loginForm.username,
          password: this.loginForm.password
        })
        .then(successResponse => {
          if (successResponse.data.status === 0) {
            _this.$store.commit('login', _this.loginForm)
            var path = this.$route.query.redirect
            _this.uid = successResponse.data.uid
            localStorage.setItem('zuid', successResponse.data.uid)
            _this.$store.commit('handleUid', successResponse.data.uid)
            this.$router.push({
              path: path === '/' || path === undefined ? '/back/home' : path,
              query: {
                uid: _this.uid
              }
            })
          }
          if (successResponse.data.status === 1) {
            this.$message.error('登陆失败')
          }
        })
        .catch(failResponse => {
        })
    }
  }
}
</script>
<style lang="scss"></style>

<style>
.login-wrap {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
#poster {
  background: url("./../../assets/eva.jpg") no-repeat;
  background-position: center;
  height: 100%;
  width: 100%;
  background-size: cover;
  position: fixed;
}
body {
  margin: 0px;
}

.login-container {
  border-radius: 15px;
  background-clip: padding-box;
  margin: 90px auto;
  width: 350px;
  padding: 35px 35px 15px 35px;
  background: #fff;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 25px #cac6c6;
}

.login_title {
  margin: 0px auto 40px auto;
  text-align: center;
  color: #505458;
}
</style>
