<template>
  <div>
    <el-dialog
      title="添加人员"
      :visible.sync="dialogVisible4"
      @close="$emit('update:show', false)"
      center
    >
      <el-form :model="form">
        <el-form-item label="添加员工" :label-width="formLabelWidth" prop="status">
          <el-select v-model="form.uid" placeholder="请选择添加的员工">
            <el-option v-for="item in form.total_member" :key="item.id" :label="item.name" :value="item.id"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="员工上级" :label-width="formLabelWidth" prop="status">
          <el-select v-model="form.leader_id" placeholder="请选择该员工项目中的领导">
            <el-option v-for="item in form.project_member" :key="item.worker_id" :label="item.worker_name" :value="item.worker_id"></el-option>
          </el-select>
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
  name: 'PerAdd',
  props: {
    show: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      dialogVisible4: this.show,
      form: {
        uid: '',
        leader_id: '',
        total_member: [
          {
            id: '',
            name: ''
          }
        ],
        project_member: [
          {
            worker_id: '',
            worker_name: ''
          }
        ]
      },
      formLabelWidth: '100px'
    }
  },
  watch: {
    show () {
      this.dialogVisible4 = this.show
    }
  },
  methods: {
    onSubmit () {
      let _this = this
      this.$axios
        .post('/project_detail/project_worker/add', {
          project_id: _this.projectid,
          worker_id: _this.form.uid,
          leader_id: _this.form.leader_id
        })
        .then(resp => {
          if (resp.data.status === 'ok') {
            this.dialogVisible4 = false
            this.$emit('onSubmit')
            _this.dialogVisible4 = false
            this.$message.success('添加成功')
          }
        })
    },
    closeDialog () {
      this.dialogVisible4 = false
      this.$emit('update:show', false)
      this.onSubmit()
    }
  },
  created () {
    this.projectid = this.$store.getters.projectid
  }
}
</script>

<style></style>
