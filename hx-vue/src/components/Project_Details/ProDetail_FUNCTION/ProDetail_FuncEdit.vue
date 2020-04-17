<template>
  <div>
    <el-dialog
      title="修改功能"
      :visible.sync="dialogVisible2"
      @close="$emit('update:show', false)"
      center>
      <el-table
        :data="tableData"
        style="width:100%"
      >
      <el-table-column label="项目id" prop="project_id"></el-table-column>
      <el-table-column label="功能ID" prop="function_id"></el-table-column>
      <el-table-column label="项目全部成员" prop="uid" >
       <el-form-item label="活动性质">
          <el-checkbox-group v-model="form.type">
          <el-checkbox label="美食/餐厅线上活动" name="type"></el-checkbox>
          <el-checkbox label="地推活动" name="type"></el-checkbox>
          <el-checkbox label="线下主题活动" name="type"></el-checkbox>
          <el-checkbox label="单纯品牌曝光" name="type"></el-checkbox>
          </el-checkbox-group>
       </el-form-item>
      </el-table-column>
      </el-table>
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
        git_authority: '1',
        file_authority: '2',
        mail_authority: 'success'
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
