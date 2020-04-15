<template>
  <div>
    <el-dialog
      title="修改权限"
      :visible.sync="dialogVisible"
      @close="$emit('update:show', false)"
      center
    >
      <el-form :model="form">
        <el-form-item label="Git权限" :label-width="formLabelWidth" prop="git_authority">
          <el-input v-model="form.git_authority" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="File权限" :label-width="formLabelWidth" prop="file_authority">
          <el-input v-model="form.file_authority" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="Mail权限" :label-width="formLabelWidth" prop="mail_authority">
          <el-input v-model="form.mail_authority" autocomplete="off" ></el-input>
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
  name: 'AuthEdit',
  props: {
    show: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      dialogVisible: this.show,
      form: {
        git_authority: '1',
        file_authority: '2',
        mail_authority: 'success'
      },
      formLabelWidth: '100px'
    }
  },
  watch: {
    show () {
      this.dialogVisible = this.show
    }
  },
  methods: {
    onSubmit () {
      let _this = this
      this.$axios
        .post('/project_detail/authority_manage/modify', {
          uid: _this.form.uid,
          project_id: _this.form.project_id,
          git_authority: _this.form.git_authority,
          file_authority: _this.form.file_authority,
          mail_authority: _this.form.mail_authority
        })
        .then(resp => {
          if (resp && resp.status === 200) {
            this.dialogVisible = false
            this.$emit('onSubmit')
            _this.dialogVisible = false
            this.$message.success('保存成功')
          }
        })
    },
    closeDialog () {
      this.dialogVisible = false
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
