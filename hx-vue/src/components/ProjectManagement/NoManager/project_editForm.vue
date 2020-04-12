<template>
  <div>
    <el-dialog
      width="95%"
      title="查看工时"
      :visible.sync="dialogFormVisible"
      @close="$emit('update:show', false)"
      center
    >
      <div class="project_table">
        <el-table :data="form" style="width:100%" stripe>
          <el-table-column label="项目id" prop="id"></el-table-column>
          <el-table-column
            label="work_time_id"
            :label-width="formLabelWidth"
            prop="name"
          ></el-table-column>
          <el-table-column
            label="project_name"
            :label-width="formLabelWidth"
            prop="name"
          ></el-table-column>
          <el-table-column
            label="功能名称"
            :label-width="formLabelWidth"
            prop="function_name"
          ></el-table-column>
          <el-table-column
            label="活动名称"
            :label-width="formLabelWidth"
            prop="activity_name"
          ></el-table-column>
          <el-table-column
            label="开始时间"
            :label-width="formLabelWidth"
            prop="start_time"
          ></el-table-column>
          <el-table-column
            label="结束时间"
            :label-width="formLabelWidth"
            prop="end_time"
          ></el-table-column>
          <el-table-column
            label="date"
            :label-width="formLabelWidth"
            prop="date"
          ></el-table-column>
          <el-table-column
            label="work_time"
            :label-width="formLabelWidth"
            prop="work_time"
          ></el-table-column>
          <el-table-column
            label="remain"
            :label-width="formLabelWidth"
            prop="remain"
          ></el-table-column>
          <el-table-column
            label="项目状态"
            prop="status"
            column-key="status"
          >
            <template slot-scope="props">
              <zx-tag :type="FlowStatusRules[props.row.status]">
                {{ FLOWS_STATUS[props.row.status] }}
              </zx-tag>
            </template>
          </el-table-column>
          <el-table-column
            label="describe"
            :label-width="formLabelWidth"
            prop="describe"
          ></el-table-column>
        </el-table>
      </div>
      <!-- <el-form :model="form">
        <el-form-item
          label="work_time_id"
          :label-width="formLabelWidth"
          prop="work_time_id"
        >
          <el-input
            v-model="form.work_time_id"
            autocomplete="off"
            disabled
          ></el-input>
        </el-form-item>
        <el-form-item
          label="project_name"
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
          label="功能名称"
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
          label="活动名称"
          :label-width="formLabelWidth"
          prop="activity_name"
        >
          <el-input
            v-model="form.activity_name"
            autocomplete="off"
            disabled
          ></el-input>
        </el-form-item>
        <el-form-item
          label="开始时间"
          :label-width="formLabelWidth"
          prop="start_time"
        >
          <el-input
            v-model="form.start_time"
            autocomplete="off"
            disabled
          ></el-input>
        </el-form-item>
        <el-form-item
          label="结束时间"
          :label-width="formLabelWidth"
          prop="end_time"
        >
          <el-input
            v-model="form.end_time"
            autocomplete="off"
            disabled
          ></el-input>
        </el-form-item>
        <el-form-item label="date" :label-width="formLabelWidth" prop="date">
          <el-input v-model="form.date" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item
          label="work_time"
          :label-width="formLabelWidth"
          prop="work_time"
        >
          <el-input
            v-model="form.work_time"
            autocomplete="off"
            disabled
          ></el-input>
        </el-form-item>
        <el-form-item
          label="remain"
          :label-width="formLabelWidth"
          prop="remain"
        >
          <el-input
            v-model="form.remain"
            autocomplete="off"
            disabled
          ></el-input>
        </el-form-item>
        <el-form-item
          label="status"
          :label-width="formLabelWidth"
          prop="status"
        >
          <el-input
            v-model="form.status"
            autocomplete="off"
            disabled
          ></el-input>
        </el-form-item>
        <el-form-item
          label="describe"
          :label-width="formLabelWidth"
          prop="describe"
        >
          <el-input
            v-model="form.describe"
            autocomplete="off"
            disabled
          ></el-input>
        </el-form-item>
      </el-form> -->
      <div slot="footer" class="dialog-footer">
        <el-button @click="closeDialog">取 消</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { FlowStatusRules } from './../../home/rule/data-config'
import ZxTag from './../../tag'
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
  components: {
    'zx-tag': ZxTag
  },
  data () {
    return {
      dialogFormVisible: this.show,
      startDatePicker: this.beginDate(),
      endDatePicker: this.endDate(),
      FlowStatusRules,
      filter_status: [
        { text: 'rejection', value: 0 },
        { text: 'pending', value: 1 },
        { text: 'established', value: 2 },
        { text: 'processing', value: 3 },
        { text: 'paid', value: 4 },
        { text: 'finished', value: 5 },
        { text: 'archived', value: 6 }
      ],
      FLOWS_STATUS: [
        'rejection',
        'pending',
        'established',
        'processing',
        'paid',
        'finished',
        'archived'
      ],
      form: [
        {
          work_time_id: '',
          project_name: '',
          function_name: '',
          activity_name: '',
          start_time: '',
          end_time: '',
          date: '',
          work_time: '',
          remain: '',
          status: '',
          describe: ''
        }
      ],
      formLabelWidth: '10%'
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

<style lang="scss" scoped>
.project_table {
  padding-top: 0;
  margin: 10px 20px;
  position: relative;
  // margin-left: auto;
  // margin-right: auto;
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
.newProject {
  margin-bottom: 10px;
  margin-left: 60%;
}
</style>
