<template>
  <div>
    <el-dialog
      title="修改"
      :visible.sync="dialogFormVisible"
      @close="$emit('update:show', false)"
      center
    >
      <el-form :model="form">
        <el-form-item label="项目ID" :label-width="formLabelWidth" prop="id">
          <el-input v-model="form.id" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item label="项目名称" :label-width="formLabelWidth" prop="name">
          <el-input v-model="form.name" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="项目状态" :label-width="formLabelWidth" prop="status">
          <el-select v-model="form.status" placeholder="请选择项目状态" :disabled="StatusFunc()">
            <el-option v-for="item in status_dict" :key="item.key" :label="item.value" :value="item.key" :disabled="item.disabled"  ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="更新时间" :label-width="formLabelWidth" prop="update_time">
          <el-input v-model="form.update_time" autocomplete="off" disabled></el-input>
        </el-form-item>
        <el-form-item label="项目描述" :label-width="formLabelWidth" prop="describe">
          <el-input v-model="form.describe" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="预定时间" :label-width="formLabelWidth" prop="scheduled_time">
          <el-date-picker v-model="form.scheduled_time" type="datetime" placeholder="预定时间" :picker-options="startDatePicker"></el-date-picker>
        </el-form-item>
        <el-form-item label="交付日" :label-width="formLabelWidth" prop="deliveyr_day">
          <el-date-picker v-model="form.delivery_day" type="datetime" placeholder="交付日" :picker-options="startDatePicker"></el-date-picker>
        </el-form-item>
        <el-form-item label="项目上级" :label-width="formLabelWidth" prop="project_superior">
          <el-select v-model="form.project_superior_id" placeholder="请选择项目上级">
            <el-option v-for="item in form.project_superior" :key="item.project_superior_id" :label="item.project_superior_name" :value="item.project_superior_id"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="主要里程碑" :label-width="formLabelWidth" prop="major_milestones">
          <el-input v-model="form.major_milestones" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="采用技术" :label-width="formLabelWidth" prop="adopting_technology">
          <el-input v-model="form.adopting_technology" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="业务领域" :label-width="formLabelWidth" prop="business_area">
          <el-select v-model="form.business_area" placeholder="请选择业务领域">
            <el-option v-for="item in form.business" :key="item.business_id" :label="item.business_name" :value="item.business_id"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="主要功能" :label-width="formLabelWidth" prop="main_function">
          <el-input v-model="form.main_function" autocomplete="off" ></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button round @click="closeDialog">取 消</el-button>
        <el-button type="success" round @click="onSubmit1">保 存</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'InfoEdit',
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
      form: {
        id: '',
        name: '',
        status: '',
        update_time: '',
        describe: '',
        scheduled_time: '',
        delivery_day: '',
        major_milestones: '',
        adopting_technology: '',
        main_function: '',
        project_superior_id: '',
        project_superior: [
          {
            project_superior_id: '',
            project_superior_name: ''
          }
        ],
        business_area: '',
        business: [
          {
            business_id: '',
            business_name: ''
          }
        ]
      },
      status_dict: [{
        key: '0',
        value: '驳回',
        disabled: true
      }, {
        key: '1',
        value: '审批中',
        disabled: true
      }, {
        key: '2',
        value: '已立项'
      }, {
        key: '3',
        value: '进行中'
      }, {
        key: '4',
        value: '已交付'
      }, {
        key: '5',
        value: '已结束'
      }, {
        key: '6',
        value: '已归档'
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
    Status1 () {
      if (this.form.status === '0' || this.form.status === '1') {
        return true
      }
      console.log('hhhhhhh')
      return false
    },
    StatusFunc () {
      if (this.form.status === '0' || this.form.status === '1') {
        return true
      }
      console.log('hhhhhhh')
      return false
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
        .post('/project_detail/modify/save', {
          id: _this.form.id,
          name: _this.form.name,
          status: _this.form.status,
          scheduled_time: _this.dateFormat(_this.form.scheduled_time),
          delivery_day: _this.dateFormat(_this.form.delivery_day),
          project_superior_id: _this.form.project_superior_id,
          major_milestones: _this.form.major_milestones,
          adopting_technology: _this.form.adopting_technology,
          business_area: _this.form.business_area,
          main_function: _this.form.main_function,
          describe: _this.form.describe
        })
        .then(resp => {
          if (resp.data.status === 'ok') {
            this.dialogFormVisible = false
            this.$emit('update:show', false)
            this.$emit('updateAgain')
            _this.dialogFormVisible = false
            this.$message.success('保存成功')
          }
        })
    },
    closeDialog () {
      this.dialogFormVisible = false
      this.$emit('update:show', false)
      this.onSubmit()
    },
    onSubmit1 () {
      this.onSubmit()
    }
  },
  created () {
    // let _this = this
    // _this.getAllInfo()
  }
}
</script>

<style></style>
