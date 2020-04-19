<template>
  <div>
    <el-dialog
      title="修改功能"
      :visible.sync="dialogVisible2"
      @close="$emit('update:show', false)"
      center>
     <el-form :model="form">
        <el-form-item label="功能名称" :label-width="formLabelWidth" prop="id">
          <el-input v-model="form.function_name" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button round @click="closeDialog">取 消</el-button>
        <el-button type="success" round @click="onSubmit">保 存</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'FuncEdit',
  props: {
    show: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      dialogVisible2: this.show,
      form: {
        function_id: '',
        project_id: '',
        function_name: ''
      },
      formLabelWidth: '100px'
    }
  },
  watch: {
    show () {
      this.dialogVisible2 = this.show
    }
  },
  methods: {
    onSubmit () {
      let _this = this
      this.$axios
        .post('/project_detail/function/modify', {
          function_id: _this.form.function_id,
          project_id: _this.form.project_id,
          function_name: _this.form.function_name
        })
        .then(resp => {
          if (resp.data.status === 'ok') {
            this.dialogVisible2 = false
            this.$emit('update:show', false)
            this.$emit('updateAgain')
            _this.dialogVisible2 = false
            this.$message.success('保存成功')
          }
        })
    },
    closeDialog () {
      this.dialogVisible2 = false
    }
  },
  created () {
    this.form.project_id = this.$store.getters.projectid
  }
}
</script>

<style></style>
