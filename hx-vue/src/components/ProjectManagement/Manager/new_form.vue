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
          label="项目上级"
          :label-width="formLabelWidth"
          prop="project_superior"
        >
          <el-select v-model="form.project_superior_id" placeholder="请选择项目上级">
            <el-option
              v-for="item in form.project_superior"
              :key="item.project_superior_id"
              :label="item.project_superior_name"
              :value="item.project_superior_id"
            ></el-option>
          </el-select>
        </el-form-item>
  <el-form-item
          label="客户"
          :label-width="formLabelWidth"
          prop="custom"
        >
          <el-select v-model="form.custom_id" placeholder="请选择项目客户">
            <el-option
              v-for="item in form.custom"
              :key="item.custom_id"
              :label="item.company_name"
              :value="item.custom_id"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="name" :label-width="formLabelWidth" prop="name">
          <el-input v-model="form.name" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item
          label="describe"
          :label-width="formLabelWidth"
          prop="describe"
        >
          <el-input v-model="form.describe" autocomplete="off"></el-input>
        </el-form-item>

               <el-form-item
          label="development_type"
          :label-width="formLabelWidth"
          prop="development_type"
        >
          <el-select v-model="form.development_type" placeholder="请选择研发类型">
            <el-option
              v-for="item in development_type_dict"
              :key="item.key"
              :label="item.value"
              :value="item.key"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item
          label="预定时间"
          :label-width="formLabelWidth"
          prop="scheduled_time"
        >
          <el-date-picker
            v-model="form.scheduled_time"
            type="date"
            placeholder="开始日期"
            :picker-options="startDatePicker"
          >
          </el-date-picker>
        </el-form-item>
        <el-form-item
          label="交付日"
          :label-width="formLabelWidth"
          prop="delivery_day"
        >
          <el-date-picker
            v-model="form.delivery_day"
            type="date"
            placeholder="结束日期"
            :picker-options="endDatePicker"
          >
          </el-date-picker>
        </el-form-item>
        <el-form-item
          label="主要里程碑"
          :label-width="formLabelWidth"
          prop="major_milestones"
        >
          <el-input
            v-model="form.major_milestones"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item
          label="采用技术"
          :label-width="formLabelWidth"
          prop="adopting_technology"
        >
          <el-input
            v-model="form.adopting_technology"
            autocomplete="off"
          ></el-input>
        </el-form-item>
        <el-form-item
          label="业务领域"
          :label-width="formLabelWidth"
          prop="business_area"
        >
          <el-select v-model="form.business_area" placeholder="请选择业务领域">
            <el-option
              v-for="item in form.business"
              :key="item.business_id"
              :label="item.business_name"
              :value="item.business_id"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item
          label="主要功能"
          :label-width="formLabelWidth"
          prop="main_function"
        >
          <el-input v-model="form.main_function" autocomplete="off"></el-input>
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
    }
  },
  data () {
    return {
      dialogFormVisible: this.show,
      startDatePicker: this.beginDate(),
      endDatePicker: this.endDate(),
      form: {
        project_superior_id: '',
        custom_id: '',
        development_type: '',
        project_superior: [
          {
            project_superior_id: '',
            project_superior_name: ''
          }
        ],
        custom: [
          {
            custom_id: '',
            company_name: ''
          }
        ],
        business: [
          {
            business_id: '',
            business_name: ''
          }
        ],
        name: '',
        describe: 'c',
        scheduled_time: '',
        delivery_day: '',
        major_milestones: '',
        adopting_technology: '',
        business_area: '',
        main_function: ''
      },
      development_type_dict: [{
        key: 'D',
        value: '开发'
      }, {
        key: 'M',
        value: '维护'
      }, {
        key: 'S',
        value: '服务'
      }, {
        key: 'O',
        value: '其他'
      }],
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
        .post('/project/create/save', {
          uid: _this.$store.getters.uid,
          name: _this.form.name,
          describe: _this.form.describe,
          development_type: _this.form.development_type,
          scheduled_time: _this.dateFormat(_this.form.scheduled_time),
          delivery_day: _this.dateFormat(_this.form.delivery_day),
          project_superior_id: _this.form.project_superior_id,
          custom_id: _this.form.custom_id,
          major_milestones: _this.form.major_milestones,
          adopting_technology: _this.form.adopting_technology,
          business_area: _this.form.business_area,
          main_function: _this.form.main_function
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
        .catch(failResponse => {
        })
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
