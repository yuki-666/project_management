<template>
  <div>
    <el-dialog
      title="项目审批"
      :visible.sync="dialogFormVisible"
      @close="$emit('update:show', false)"
      center
    >
      <el-form :model="form">
        <el-form-item label="功能名称" :label-width="formLabelWidth" prop="function_name">
          <el-input v-model="form.function_name" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item
          label="事件名称"
          :label-width="formLabelWidth"
          prop="event_name"
        >
          <el-input v-model="form.event_name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item
          label="开始时间"
          :label-width="formLabelWidth"
          prop="start_time"
        >
          <el-input v-model="form.start_time" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item
          label="结束时间"
          :label-width="formLabelWidth"
          prop="end_time"
        >
          <el-input v-model="form.end_time" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button size="mini" type="primary" round @click="closeDialog">取 消</el-button>
        <el-button size="mini" type="primary" round @click="onSubmit">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  props: {
    show: {
      type: Boolean,
      default: false
    },
    zid: {
      type: String,
      default: ''
    }
  },
  data () {
    return {
      select: '',
      dialogFormVisible: this.show,
      startDatePicker: this.beginDate(),
      endDatePicker: this.endDate(),
      form: {
        id: '',
        function_name: '',
        event_name: 'c',
        start_time: '',
        end_time: '',
        status: ''
      },
      formLabelWidth: '100px'
    }
  },
  watch: {
    show () {
      this.dialogFormVisible = this.show
    }
  },
  methods: {
    dateFormat (value) {
      var date = new Date(value)
      var year = date.getFullYear()
      var month =
        date.getMonth() + 1 < 10
          ? '0' + (date.getMonth() + 1)
          : date.getMonth() + 1
      var day = date.getDate() < 10 ? '0' + date.getDate() : date.getDate()
      var hour = ('0' + date.getHours()).slice(-2)
      var minute = ('0' + date.getMinutes()).slice(-2)
      return year + '-' + month + '-' + day + ' ' + hour + ':' + minute
    },
    onSubmit () {
      let _this = this
      this.$axios
        .post('/approval/work_time/passive/modify', {
          id: _this.zid,
          function_name: _this.form.function_name,
          event_name: _this.form.event_name,
          start_time: _this.dateFormat(_this.form.start_time),
          end_time: _this.dateFormat(_this.form.end_time)
        })
        .then(successResponse => {
          let status = successResponse.data.status
          if (status === 'ok') {
            this.dialogFormVisible = false
            this.$emit('update:show', false)
            this.$emit('updateAgain')
            _this.dialogFormVisible = false
            this.$message.success('更新成功')
          }
        })
        .catch(failResponse => {
        })
    },
    endDate () {
      let _this = this
      return {
        disabledDate (time) {
          if (_this.form.start_time) {
            return new Date(_this.form.start_time).getTime() >= time.getTime()
          } else {
            return time.getTime() > Date.now()
          }
        }
      }
    },
    beginDate () {
      let _this = this
      return {
        disabledDate (time) {
          if (_this.form.end_time) {
            return (
              new Date(_this.form.end_time).getTime() <= time.getTime()
            )
          } else {
            return time.getTime() > Date.now()
          }
        }
      }
    },
    closeDialog () {
      this.dialogFormVisible = false
      this.$emit('update:show', false)
    }
  },
  mounted () {
  }
}
</script>

<style></style>
