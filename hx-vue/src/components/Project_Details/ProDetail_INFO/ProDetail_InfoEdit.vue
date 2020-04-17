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
          <el-input v-model="form.project_id" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="项目名称" :label-width="formLabelWidth" prop="name">
          <el-input v-model="form.project_name" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="项目状态" :label-width="formLabelWidth" prop="status">
          <el-input v-model="form.project_stat" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="更新时间" :label-width="formLabelWidth" prop="update_time">
          <el-input v-model="form.update_time" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="项目描述" :label-width="formLabelWidth" prop="describe">
          <el-input v-model="form.describe" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="预定时间" :label-width="formLabelWidth" prop="scheduled_time">
          <el-input v-model="form.scheduled_time" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="交付日" :label-width="formLabelWidth" prop="deliveyr_day">
          <el-input v-model="form.delivery_day" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="项目上级" :label-width="formLabelWidth" prop="project_superior_name">
          <el-input v-model="form.project_superior_name" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="主要里程碑" :label-width="formLabelWidth" prop="major_milestones">
          <el-input v-model="form.major_milestones" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="采用技术" :label-width="formLabelWidth" prop="adopting_technology">
          <el-input v-model="form.adopting_technology" autocomplete="off" ></el-input>
        </el-form-item>
        <el-form-item label="业务领域" :label-width="formLabelWidth" prop="business_area">
          <el-input v-model="form.business_area" autocomplete="off" ></el-input>
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
        status: 'success',
        update_time: '',
        describe: '',
        scheduled_time: '',
        delivery_day: '',
        project_superior_name: '',
        major_milestones: '',
        adopting_technology: '',
        business_area: '',
        main_function: ''
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
        .post('/project_detail/modify/save', {
          id: _this.form.id,
          name: _this.form.name,
          status: _this.form.status,
          update_time: _this.form.update_time,
          scheduled_time: _this.form.scheduled_time,
          delivery_day: _this.form.delivery_day,
          project_superior_name: _this.form.project_superior_name,
          major_milestones: _this.form.major_milestones,
          adopting_technology: _this.form.adopting_technology,
          business_area: _this.form.business_area,
          main_function: _this.form.main_function
        })
        .then(resp => {
          if (resp && resp.status === 200) {
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
      // this.status = 2
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
