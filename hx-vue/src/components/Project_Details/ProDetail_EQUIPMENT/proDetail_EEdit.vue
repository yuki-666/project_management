<template>
  <div>
    <el-dialog
      title="添加设备"
      :visible.sync="dialogVisible"
      @close="$emit('update:show', false)"
      center
    >
      <el-form :model="form">
        <el-form-item label="设备名称" :label-width="formLabelWidth" prop="name">
          <el-input
            v-model="form.name"
            autocomplete="off"
            placeholder="请输入内容"
          ></el-input>
        </el-form-item>
        <el-form-item label="管理者" :label-width="formLabelWidth" prop="manager">
          <el-select v-model="form.manager" placeholder="请选择管理者">
            <el-option
              v-for="item in member"
              :key="item.worker_id"
              :label="item.worker_name"
              :value="item.worker_id"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="租借日期" :label-width="formLabelWidth" prop="start_time">
            <el-date-picker v-model="form.start_time" type="datetime" placeholder="租借日期" :picker-options="startDatePicker"></el-date-picker>
        </el-form-item>
        <el-form-item label="到期日期" :label-width="formLabelWidth" prop="end_time">
          <el-date-picker v-model="form.end_time" type="datetime" placeholder="到期日期" :picker-options="startDatePicker"></el-date-picker>
        </el-form-item>
        <el-form-item label="设备是否完好" :label-width="formLabelWidth" prop="status">
          <el-select v-model="form.status" placeholder="请选择设备状态">
            <el-option
              v-for="item in status_dict"
              :key="item.key"
              :label="item.value"
              :value="item.key"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="是否归还" :label-width="formLabelWidth" prop="label">
          <el-select v-model="form.label" placeholder="请选择归还状态">
            <el-option
              v-for="item in label_dict"
              :key="item.key"
              :label="item.value"
              :value="item.key"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="归还日期" :label-width="formLabelWidth" prop="return_time">
          <el-date-picker v-model="form.return_time" type="datetime" placeholder="归还日期" :picker-options="startDatePicker"></el-date-picker>
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
  name: 'EEdit',
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
        id: '',
        name: '',
        manager: '',
        start_time: '',
        end_time: '',
        status: '',
        label: '',
        return_time: ''
      },
      label_dict: [{
        key: 0,
        value: '否'
      }, {
        key: 1,
        value: '是'
      }],
      status_dict: [{
        key: 0,
        value: '损坏'
      }, {
        key: 1,
        value: '完好'
      }],
      member: [{
        worker_id: '',
        worker_name: ''
      }],
      formLabelWidth: '100px'
    }
  },
  watch: {
    show () {
      this.dialogVisible = this.show
    }
  },
  methods: {
    getMember () {
      var _this = this
      this.$axios
        .get('/project_detail/project_equipment/user', {
          params: {
            project_id: _this.projectid
          }
        })
        .then(successResponse => {
          _this.member = successResponse.data
        })
        .catch(failResponse => {
        })
    },
    dateFormat (value) {
      var date = new Date(value)
      var year = date.getFullYear()
      var month =
        date.getMonth() + 1 < 10
          ? '0' + (date.getMonth() + 1)
          : date.getMonth() + 1
      var day = date.getDate() < 10 ? '0' + date.getDate() : date.getDate()
      return year + '-' + month + '-' + day
    },
    onSubmit () {
      let _this = this
      this.$axios
        .post('/project_detail/project_equipment/modify', {
          project_id: _this.projectid,
          id: _this.form.id,
          name: _this.form.name,
          manager: _this.form.manager,
          start_time: _this.dateFormat(_this.form.start_time),
          end_time: _this.dateFormat(_this.form.end_time),
          status: _this.form.status,
          label: _this.form.label,
          return_time: _this.dateFormat(_this.form.return_time)
        })
        .then(resp => {
          if (resp.data.status === 'ok') {
            this.dialogVisible = false
            this.$emit('update:show', false)
            this.$emit('updateAgain')
            _this.dialogVisible = false
            this.$message.success('修改成功')
          }
        })
    },
    closeDialog () {
      this.dialogVisible = false
    }
  },
  created () {
    this.projectid = this.$store.getters.projectid
    this.getMember()
  }
}
</script>

<style></style>
