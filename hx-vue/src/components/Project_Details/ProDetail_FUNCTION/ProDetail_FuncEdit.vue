<template>
  <div>
    <el-dialog
      title="修改功能"
      :visible.sync="dialogVisible2"
      @close="$emit('update:show', false)"
      center>
     <el-form :model="form">
        <el-form-item label="项目名称" :label-width="formLabelWidth" prop="id">
          <el-input v-model="form.function_name" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button round @click="closeDialog">取 消</el-button>
        <el-button type="success" round @click="closeDialog">保 存</el-button>
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
        function_name: '1'
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
          uid: _this.form.uid,
          project_id: _this.form.project_id,
          git_authority: _this.form.git_authority,
          file_authority: _this.form.file_authority,
          mail_authority: _this.form.mail_authority
        })
        .then(resp => {
          if (resp && resp.status === 200) {
            this.dialogVisible2 = false
            this.$emit('onSubmit')
            _this.dialogVisible2 = false
            this.$message.success('保存成功')
          }
        })
    },
    closeDialog () {
      this.dialogVisible2 = false
      this.$emit('update:show', false)
      this.onSubmit()
    }
  },
  created () {
    // let _this = this
    // _this.getAllInfo()
  }
}
</script>

<style></style>
