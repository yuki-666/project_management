<template>
  <div>
    <el-dialog
      title="新建管理员"
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
        <el-form-item prop="id" style="height: 0">
          <el-input
            type="hidden"
            v-model="form.id"
            autocomplete="off"
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
  name: 'AccEdit',
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
        password: ''
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
        password: ''
      }
    },
    onSubmit () {
      let _this = this
      this.$axios
        .post('/back/create_super_account', {
          username: _this.form.username,
          password: _this.form.password
        })
        .then(resp => {
          if (resp && resp.status === 200) {
            this.dialogFormVisible = false
            this.$emit('onSubmit')
            _this.dialogFormVisible = false
            this.$message.success('新建成功')
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
