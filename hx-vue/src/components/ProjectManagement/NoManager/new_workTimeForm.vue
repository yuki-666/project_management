<template>
  <div>
    <el-dialog
      title="项目审批"
      :visible.sync="dialogFormVisible"
      @close="$emit('update:show', false)"
      center
    >
      <el-form :model="form">
        <el-form-item
          label="function_id"
          :label-width="formLabelWidth"
          prop="function_id"
        >
          <el-input
            v-model="form.function_id"
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
        <el-form-item
          label="remain"
          :label-width="formLabelWidth"
          prop="remain"
        >
          <el-input v-model="form.remain" autocomplete="off"></el-input>
        </el-form-item>

        <el-form-item
          label="describe"
          :label-width="formLabelWidth"
          prop="describe"
        >
          <el-input v-model="form.describe" autocomplete="off"></el-input>
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
      dialogFormVisible: this.show,
      startDatePicker: this.beginDate(),
      endDatePicker: this.endDate(),
      form: {
        function: [
          {
            function_id: '',
            function_name: ''
          }
        ],
        date: '',
        event_name: '',
        start_time: '',
        end_time: '',
        remain: '',
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
    onSubmit () {
      let _this = this
      this.$axios
        .post('/project/work_time/create/save', {
          uid: _this.$store.getters.uid,
          project_id: _this.zid,
          date: _this.date,
          function_id: _this.function_id,
          event_name: _this.event_name,
          start_time: _this.start_time,
          end_time: _this.end_time,
          remain: _this.remain,
          describe: _this.describe
        })
        .then(successResponse => {
          let status = successResponse.data.status
          if (status === 'ok') {
            _this.dialogFormVisible = false
            _this.$emit('update:show', false)
            _this.$emit('updateAgain')
            this.$message.success('已经更新')
          } else if (status === 'fail_1') {
            _this.dialogFormVisible = false
            _this.$emit('update:show', false)
            _this.$emit('updateAgain')
            this.$message.error('work_time > 24h')
          } else if (status === 'fail_2') {
            _this.dialogFormVisible = false
            _this.$emit('update:show', false)
            _this.$emit('updateAgain')
            this.$message.error('start_time < end_time')
          } else if (status === 'fail_3') {
            _this.dialogFormVisible = false
            _this.$emit('update:show', false)
            _this.$emit('updateAgain')
            this.$message.error('remain < 0')
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
  created () {
    // let _this = this
    // _this.getAllInfo()
  }
}
</script>

<style></style>
