<template>
  <div>
    <el-dialog
      title="修改工时"
      :visible.sync="dialogFormVisible"
      @close="$emit('update:show', false)"
      center
    >
      <el-form :model="form">
         <el-form-item
          label="项目名称"
          :label-width="formLabelWidth"
          prop="project_name"
        >
          <el-input
            v-model="form.project_name"
            autocomplete="off"
            disabled
          ></el-input>
        </el-form-item>
        <el-form-item
          label="function_name"
          :label-width="formLabelWidth"
          prop="function_name"
        >
          <el-input
            v-model="form.function_name"
            autocomplete="off"
            disabled
          ></el-input>
        </el-form-item>
        <el-form-item
          label="event_name"
          :label-width="formLabelWidth"
          prop="event_name"
        >
          <el-input v-model="form.event_name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item
          label="start_time"
          :label-width="formLabelWidth"
          prop="start_time"
        >
          <el-date-picker
            v-model="form.start_time"
            type="datetime"
            placeholder="开始日期"
            :picker-options="startDatePicker"
          >
          </el-date-picker>
        </el-form-item>
        <el-form-item
          label="end_time"
          :label-width="formLabelWidth"
          prop="end_time"
        >
          <el-date-picker
            v-model="form.end_time"
            type="datetime"
            placeholder="结束日期"
            :picker-options="endDatePicker"
          >
          </el-date-picker>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="closeDialog">取 消</el-button>
        <el-button type="primary" @click="onSubmit">确 定</el-button>
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
        project_name: '',
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
          project_name: _this.form.project_name,
          function_name: _this.form.function_name,
          event_name: _this.form.event_name,
          start_time: _this.dateFormat(_this.form.start_time),
          end_time: _this.dateFormat(_this.form.end_time)
        })
        .then(successResponse => {
          let status = successResponse.data.status
          if (status === 'ok') {
            _this.dialogFormVisible = false
            _this.$emit('update:show', false)
            _this.$emit('updateAgain')
            this.$message.success('已经更新')
          }
        })
        .catch(failResponse => {})
    },
    endDate () {
      let _this = this
      return {
        disabledDate (time) {
          if (_this.form.start_time) {
            return new Date(_this.form.start_time).getTime() >= time.getTime()
          } else {
            return time.getTime() < Date.now() - 8.64e7 // 8.64e7=1000*60*60*24一天
          }
        }
      }
    },
    beginDate () {
      let _this = this
      return {
        disabledDate (time) {
          if (_this.form.end_time) {
            return new Date(_this.form.end_time).getTime() <= time.getTime()
          } else {
            return time.getTime() < Date.now() - 8.64e7 // 8.64e7=1000*60*60*24一天
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
    // let _this = this
    // _this.getAllInfo()
  }
}
</script>

<style></style>
