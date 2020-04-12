<template>
  <div>
    hhhhhhh
    <el-form-item label="开始时间" prop="startTime">
      <el-date-picker
        v-model="form.startTime"
        format="yyyy-MM-dd HH:mm:ss"
        value-format="yyyy-MM-dd HH:mm:ss"
        clearable
        style="width: 100%"
        :picker-options="startDatePicker"
        type="datetime"
      ></el-date-picker>
    </el-form-item>
    <el-form-item label="结束时间" prop="endTime">
      <el-date-picker
        v-model="form.endTime"
        format="yyyy-MM-dd HH:mm:ss"
        value-format="yyyy-MM-dd HH:mm:ss"
        clearable
        style="width: 100%"
        :picker-options="endDatePicker"
        :disabled="dialogStatus == 'view'"
        type="datetime"
      ></el-date-picker>
    </el-form-item>
  </div>
</template>
<script>
export default {
  data () {
    return {
      startDatePicker: this.beginDate(),
      endDatePicker: this.processDate()
    }
  },
  methods: {
    beginDate () {
      const self = this
      return {
        disabledDate (time) {
          if (self.form.endTime) {
            // 如果结束时间不为空，则小于结束时间
            return new Date(self.form.endTime).getTime() < time.getTime()
          } else {
            // return time.getTime() > Date.now()//开始时间不选时，结束时间最大值小于等于当天
          }
        }
      }
    },
    processDate () {
      const self = this
      return {
        disabledDate (time) {
          if (self.form.startTime) {
            // 如果开始时间不为空，则结束时间大于开始时间
            return new Date(self.form.startTime).getTime() > time.getTime()
          } else {
            // return time.getTime() > Date.now()//开始时间不选时，结束时间最大值小于等于当天
          }
        }
      }
    }
  }
}
</script>
<style lang="scss" scoped>
.project_table {
  padding-top: 0;
  margin: 10px 15%;
  position: relative;
}
.demo-table-expand {
  font-size: 0;
}
.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}
.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
  color: red;
}
.pag {
  margin: 5px 70%;
}
</style>
