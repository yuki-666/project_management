<template>
  <div>
    <el-dialog
      title="添加人员"
      :visible.sync="dialogVisibleAddPerson"
      @close="$emit('update:show', false)"
      center
    >
      <el-form :model="form">
        <el-form-item label="添加人员" :label-width="formLabelWidth" prop="worker_id">
          <el-select v-model="form.worker_id" placeholder="请选择添加的员工">
            <el-option
              v-for="item in member"
              :key="item.worker_id"
              :label="item.worker_name"
              :value="item.worker_id"
            ></el-option>
          </el-select>
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
      dialogVisibleAddPerson: this.show,
      projectid: '',
      form: {
        function_id: '',
        worker_id: ''
      },
      member: [{
        worker_id: '',
        worker_name: ''
      }],
      formLabelWidth: '100px'
    }
  },
  watch: {
    show () {
      this.dialogVisibleAddPerson = this.show
    }
  },
  methods: {
    onSubmit () {
      let _this = this
      this.$axios
        .post('/project_detail/function/person/add', {
          project_id: _this.projectid,
          function_id: _this.form.function_id,
          worker_id: _this.form.worker_id
        })
        .then(resp => {
          if (resp.data.status === 'ok') {
            this.dialogVisibleAddPerson = false
            this.$emit('update:show', false)
            this.$emit('updateAgain')
            _this.member.worker_name = ''
            _this.dialogVisibleAddPerson = false
            this.$message.success('添加成功')
          }
        })
    },
    closeDialog () {
      this.dialogVisibleAddPerson = false
    }
  },
  created () {
    this.projectid = this.$store.getters.projectid
  }
}
</script>

<style></style>
