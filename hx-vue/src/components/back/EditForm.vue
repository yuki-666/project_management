<template>
  <div>
    <el-dialog
      title="修改员工信息"
      :visible.sync="dialogFormVisible"
      @close="$emit('update:show', false)"
      center
    >
      <el-form v-model="form" style="text-align: left" ref="dataForm">
        <el-form-item label="用户名" :label-width="formLabelWidth" prop="username">
          <el-input
            v-model="form.username"
            autocomplete="off"
            placeholder="请输入用户名"
          ></el-input>
        </el-form-item>
        <el-form-item label="密码" :label-width="formLabelWidth" prop="password">
          <el-input
            v-model="form.password"
            autocomplete="off"
            placeholder="请输入密码"
          ></el-input>
        </el-form-item>
        <el-form-item label="姓名" :label-width="formLabelWidth" prop="name">
          <el-input
            v-model="form.name"
            autocomplete="off"
            placeholder="请输入密码"
          ></el-input>
        </el-form-item>
        <el-form-item label="职位" :label-width="formLabelWidth" prop="career">
          <el-input
            v-model="form.career"
            autocomplete="off"
            placeholder="请输入职位"
          ></el-input>
        </el-form-item>
        <el-form-item label="部门" :label-width="formLabelWidth" prop="department">
          <el-input
            v-model="form.department"
            autocomplete="off"
            placeholder="请输入部门"
          ></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="closeDialog">取 消</el-button>
        <el-button type="primary" @click="onSubmit">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'EditForm',
  props: {
    show: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      dialogFormVisible: this.show,
      form: {
        username: '',
        password: '',
        name: '',
        career: '',
        department: ''
      },
      formLabelWidth: '120px'
    }
  },
  watch: {
    show () {
      this.dialogFormVisible = this.show
    }
  },
  methods: {
    clear () {
      this.form = {
        username: '',
        password: '',
        name: '',
        career: '',
        department: ''
      }
    },
    onSubmit () {
      let _this = this
      this.$axios
        .post('/back/modify_normal_account', {
          username: _this.form.username,
          password: _this.form.password,
          name: _this.form.name,
          career: _this.form.career,
          department: _this.form.department
        })
        .then(resp => {
          if (resp && resp.status === 200) {
            this.dialogFormVisible = false
            this.$emit('update:show', false)
            _this.dialogFormVisible = false
            this.$message.success('修改成功')
          }
        })
    },
    closeDialog () {
      this.dialogFormVisible = false
    }
  }
}
</script>

<style scoped>
.el-icon-circle-plus-outline {
  margin: 50px 0 0 20px;
  font-size: 100px;
  float: left;
  cursor: pointer;
}
</style>
