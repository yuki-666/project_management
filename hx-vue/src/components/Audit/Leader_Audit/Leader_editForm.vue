<template>
  <div>
    <el-dialog
      title="项目审批"
      :visible.sync="dialogFormVisible"
      @close="$emit('update:show', false)"
      center
    >
      <el-form :model="form">
        <el-form-item label="funcName" :label-width="formLabelWidth" prop="function_name">
          <el-input v-model="form.function_name" autocomplete="off"></el-input>
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
      type: Number,
      default: -1
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
        end_time: ''
      },
      formLabelWidth: '100px'
    }
  },
  watch: {
    // show: function (value) {
    //   this.dialogFormVisible = value
    //   console.log(this.dialogFormVisible)
    // }
    show () {
      this.dialogFormVisible = this.show
    }
  },
  methods: {
    dateFormat (value) {
      console.log('hhhhhhh')
      console.log(value)
      var date = new Date(value)
      var year = date.getFullYear()
      var month =
        date.getMonth() + 1 < 10
          ? '0' + (date.getMonth() + 1)
          : date.getMonth() + 1
      var day = date.getDate() < 10 ? '0' + date.getDate() : date.getDate()
      console.log(year + '-' + month + '-' + day)
      var hour = ('0' + date.getHours()).slice(-2)
      var minute = ('0' + date.getMinutes()).slice(-2)
      console.log(year + '-' + month + '-' + day + ' ' + hour + ':' + minute)
      return year + '-' + month + '-' + day + ' ' + hour + ':' + minute
    },
    onSubmit () {
      let _this = this
      // console.log('test3')
      // console.log(_this.select)
      // console.log(_this.select.project_superior)
      // console.log(_this.form.project_superior.project_superior_name)
      // console.log('test2')
      // console.log(_this.form.name)
      this.$axios
        .post('/approval/work_time/passive/modify', {
          id: _this.zid,
          function_name: _this.form.function_name,
          event_name: _this.form.event_name,
          start_time: _this.dateFormat(_this.form.start_time),
          end_time: _this.dateFormat(_this.form.end_time)
        })
        .then(successResponse => {
          // console.log(successResponse)
          console.log(successResponse.data)
          let status = successResponse.data.status
          if (status === 'ok') {
            _this.dialogFormVisible = false
            _this.$emit('update:show', false)
            _this.$emit('updateAgain')
            this.$message.success('已经更新')
          }
          // this.dialogFormVisible = false
        })
        .catch(failResponse => {
          console.log('OMmmmG,my_audit')
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
    // getAllInfo () {
    //   // console.log('xxx')
    //   let _this = this
    //   this.$axios
    //     .get('/approval/project/show', {
    //       params: {
    //         id: _this.form.id
    //       }
    //     })
    //     .then(successResponse => {
    //       // console.log('hhzzzzzzhh')
    //       _this.form = successResponse.data
    //     })
    // },
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
