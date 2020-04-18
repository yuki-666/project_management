<template>
  <div>
    <el-dialog
      title="添加设备"
      :visible.sync="dialogVisible"
      @close="$emit('update:show', false)"
      center
    >
      <el-form :model="form">
        <el-form-item label="设备名称" :label-width="formLabelWidth" prop="name">
          <el-input
            v-model="form.name"
            autocomplete="off"
            placeholder="请输入内容"
          ></el-input>
        </el-form-item>
        <el-form-item label="管理者" :label-width="formLabelWidth" prop="manager">
          <el-input
            v-model="form.manager"
            autocomplete="off"
            placeholder="请输入内容"
          ></el-input>
        </el-form-item>
        <el-form-item label="租借日期" :label-width="formLabelWidth" prop="ztime">
            <el-date-picker v-model="form.ztime" type="datetime" placeholder="租借日期" :picker-options="startDatePicker"></el-date-picker>
        </el-form-item>
        <el-form-item label="到期日期" :label-width="formLabelWidth" prop="dtime">
          <el-date-picker v-model="form.dtime" type="datetime" placeholder="到期日期" :picker-options="startDatePicker"></el-date-picker>
        </el-form-item>
        <el-form-item label="设备是否完好" :label-width="formLabelWidth" prop="status">
          <el-select v-model="form.status" placeholder="请选择设备状态">
            <el-option
              v-for="item in status_dict"
              :key="item.key"
              :label="item.value"
              :value="item.key"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="是否归还" :label-width="formLabelWidth" prop="label">
          <el-select v-model="form.label" placeholder="请选择归还状态">
            <el-option
              v-for="item in label_dict"
              :key="item.key"
              :label="item.value"
              :value="item.key"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="归还日期" :label-width="formLabelWidth" prop="htime">
          <el-date-picker v-model="form.htime" type="datetime" placeholder="归还日期" :picker-options="startDatePicker"></el-date-picker>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button round @click="closeDialog">取 消</el-button>
        <el-button type="success" round @click="closeDialog">确 认</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'EEdit',
  props: {
    show: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      dialogVisible: this.show,
      form: {
        name: '',
        manager: '',
        ztime: '',
        dtime: '',
        status: '',
        label: '',
        htime: '',
        label_dict: [{
          key: '0',
          value: '是'
        }, {
          key: '1',
          value: '否'
        }],
        status_dict: [{
          key: '0',
          value: '完好'
        }, {
          key: '1',
          value: '故障'
        }]
      },
      formLabelWidth: '100px'
    }
  },
  watch: {
    show () {
      this.dialogVisible = this.show
    }
  },
  methods: {
    onSubmit () {
      let _this = this
      this.$axios
        .post('/project_detail/project_equipment/modify', {
          project_id: '2020-04-18',
          name: _this.form.name,
          manager: _this.form.manager,
          ztime: _this.form.ztime,
          dtime: _this.form.dtime,
          status: _this.form.status,
          label: _this.form.label,
          htime: _this.form.htime
        })
        .then(resp => {
          if (resp.data.status === 'ok') {
            this.dialogVisible = false
            this.$emit('onSubmit')
            _this.dialogVisible = false
            this.$message.success('操作成功')
          }
        })
    },
    closeDialog () {
      this.dialogVisible = false
      this.$emit('update:show', false)
      this.onSubmit()
    }
  },
  created () {
    this.projectid = this.$store.getters.projectid
  }
}
</script>

<style></style>
