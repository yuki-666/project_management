<template>
  <div>
    <el-dialog
      title="添加功能"
      :visible.sync="dialogVisible3"
      @close="$emit('update:show', false)"
      center
    >
      <el-form :model="form">
        <el-form-item label="功能名称" :label-width="formLabelWidth" prop="function_name">
          <el-input v-model="form.function_name" autocomplete="off" ></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button round @click="closeDialog">取 消</el-button>
        <el-button type="success" round @click="onSubmit">确 认</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'FuncAdd',
  props: {
    show: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      dialogVisible3: this.show,
      form: {
        parent_function_id: '',
        project_id: '',
        function_name: ''
      },
      formLabelWidth: '100px'
    }
  },
  watch: {
    show () {
      this.dialogVisible3 = this.show
    }
  },
  methods: {
    onSubmit () {
      let _this = this
      this.$axios
        .post('/project_detail/function/add', {
          project_id: _this.form.project_id,
          parent_function_id: _this.form.parent_function_id,
          function_name: _this.form.function_name
        })
        .then(resp => {
          if (resp.data.status === 'ok') {
            this.dialogVisible3 = false
            this.$emit('update:show', false)
            this.$emit('updateAgain')
            _this.dialogVisible3 = false
            this.$message.success('添加成功')
          }
        })
    },
    closeDialog () {
      this.dialogVisible3 = false
    }
  },
  created () {
    this.form.project_id = this.$store.getters.projectid
  }
}
</script>

<style></style>
