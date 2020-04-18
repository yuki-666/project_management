<template>
  <div>
    <el-dialog
      title="新建员工信息"
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
          <el-select v-model="form.career" placeholder="请选择职位">
            <el-option
              v-for="item in career_dict"
              :key="item.key"
              :label="item.value"
              :value="item.key"
            ></el-option>
          </el-select>
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
  name: 'WorkerEdit',
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
      career_dict: [{
        key: '0',
        value: '项目上级'
      }, {
        key: '1',
        value: '项目经理'
      }, {
        key: '2',
        value: '普通工人'
      }],
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
        .post('/back/create_normal_account', {
          username: _this.form.username,
          password: _this.form.password,
          name: _this.form.name,
          career: _this.form.career,
          department: _this.form.department
        })
        .then(successResponse => {
          if (successResponse.data.status === 0) {
            this.dialogFormVisible = false
            this.$emit('update:show', false)
            this.$emit('updateAgain')
            _this.dialogFormVisible = false
            this.$message.success('新建成功')
          }
          if (successResponse.data.status === 1) {
            this.$message.error('用户已存在')
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
