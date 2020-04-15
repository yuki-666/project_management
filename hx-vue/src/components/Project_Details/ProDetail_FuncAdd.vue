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
        <el-button type="success" round @click="closeDialog">确 认</el-button>
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
          project_id: '2020-0000-D-01',
          parent_function_id: _this.form.parent_function_id,
          function_name: _this.form.function_name
        })
        .then(resp => {
          if (resp && resp.status === 200) {
            this.dialogVisible3 = false
            this.$emit('onSubmit')
            _this.dialogVisible3 = false
            this.$message.success('添加成功')
          }
        })
    },
    closeDialog () {
      this.dialogVisible3 = false
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
