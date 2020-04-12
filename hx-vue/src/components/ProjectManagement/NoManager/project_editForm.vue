<template>
  <div>
    <el-dialog
      title="查看工时"
      :visible.sync="dialogFormVisible"
      @close="$emit('update:show', false)"
      center
    >
      <el-form :model="form">
           <el-form-item label="work_time_id" :label-width="formLabelWidth" prop="work_time_id">
          <el-input v-model="form.work_time_id" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item label="project_name" :label-width="formLabelWidth" prop="project_name">
          <el-input v-model="form.project_name" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item label="功能名称" :label-width="formLabelWidth" prop="function_name">
          <el-input v-model="form.function_name" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item label="活动名称" :label-width="formLabelWidth" prop="event_name">
          <el-input v-model="form.event_name" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item label="开始时间" :label-width="formLabelWidth" prop="start_time">
          <el-input v-model="form.start_time" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item label="结束时间" :label-width="formLabelWidth" prop="end_time">
          <el-input v-model="form.end_time" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item label="date" :label-width="formLabelWidth" prop="date">
          <el-input v-model="form.date" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item label="work_time" :label-width="formLabelWidth" prop="work_time">
          <el-input v-model="form.work_time" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item label="remain" :label-width="formLabelWidth" prop="remain">
          <el-input v-model="form.remain" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item label="status" :label-width="formLabelWidth" prop="status">
          <el-input v-model="form.status" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item
          label="describe"
          :label-width="formLabelWidth"
          prop="describe"
        >
          <el-input v-model="form.describe" autocomplete="off" disabled></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="closeDialog">取 消</el-button>
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
      dialogFormVisible: this.show,
      startDatePicker: this.beginDate(),
      endDatePicker: this.endDate(),
      form: {
        work_time_id: '',
        project_name: '',
        function_name: '',
        event_name: '',
        start_time: '',
        end_time: '',
        date: '',
        work_time: '',
        remain: '',
        status: '',
        describe: ''
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
      return year + '-' + month + '-' + day
    },
    beginDate () {
      let _this = this
      return {
        disabledDate (time) {
          if (_this.form.delivery_day) {
            return new Date(_this.form.delivery_day).getTime() < time.getTime()
          } else {
            return time.getTime() > Date.now()
          }
        }
      }
    },
    endDate () {
      let _this = this
      return {
        disabledDate (time) {
          if (_this.form.scheduled_time) {
            return (
              new Date(_this.form.scheduled_time).getTime() > time.getTime()
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
  created () {
    // let _this = this
    // _this.getAllInfo()
  }
}
</script>

<style></style>
