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
          label="功能名称"
          :label-width="formLabelWidth"
          prop="function_id"
        >
          <el-select v-model="form.function_id" placeholder="请选择功能名称">
            <el-option
              v-for="item in form.function"
              :key="item.function_id"
              :label="item.function_name"
              :value="item.function_id"
            ></el-option>
          </el-select>
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
        <el-form-item
          label="剩余时间"
          :label-width="formLabelWidth"
          prop="remain"
        >
          <el-input v-model="form.remain" autocomplete="off"></el-input>
        </el-form-item>

        <el-form-item
          label="描述"
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
        function_id: '',
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
          function_id: _this.form.function_id,
          event_name: _this.form.event_name,
          start_time: _this.form.start_time,
          end_time: _this.form.end_time,
          remain: _this.form.remain,
          describe: _this.form.describe
        })
        .then(successResponse => {
          let status = successResponse.data.status
          if (status === 'ok') {
            _this.dialogFormVisible = false
            _this.$emit('update:show', false)
            _this.$emit('updateAgain')
            this.$message.success('新建成功')
          } else if (status === 'fail_1') {
            this.$message.error('一天的工作时间不得超过24h')
          } else if (status === 'fail_2') {
            this.$message.error('开始时间>=结束时间')
          } else if (status === 'fail_3') {
            this.$message.error('开始、结束、剩余时间必须为数字')
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
