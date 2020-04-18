<template>
  <div>
    <el-dialog
      title="新建风险"
      :visible.sync="dialogVisible"
      @close="$emit('update:show', false)"
      center
    >
      <el-form :model="form">
        <el-form-item label="风险内容" :label-width="formLabelWidth" prop="describe">
          <el-input
            v-model="form.describe"
            autocomplete="off"
            placeholder="请输入内容"
          ></el-input>
        </el-form-item>
        <el-form-item label="优先级" :label-width="formLabelWidth" prop="level">
         <el-select v-model="form.level" placeholder="请选择优先级">
            <el-option
              v-for="item in level_dict"
              :key="item.key"
              :label="item.value"
              :value="item.key"
            ></el-option>
          </el-select>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button round @click="closeDialog">取 消</el-button>
        <el-button type="success" round @click="onSubmit">确 认</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'RiskAdd',
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
        describe: '',
        level: ''
      },
      level_dict: [{
        key: '0',
        value: '低'
      }, {
        key: '1',
        value: '中'
      }, {
        key: '2',
        value: '高'
      }],
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
        .post('/project_detail/project_risk/add', {
          project_id: _this.projectid,
          describe: _this.form.describe,
          level: _this.form.level
        })
        .then(resp => {
          if (resp.data.status === 'ok') {
            this.dialogFormVisible = false
            this.$emit('update:show', false)
            this.$emit('updateAgain')
            _this.dialogFormVisible = false
            this.$message.success('添加成功')
          }
        })
    },
    closeDialog () {
      this.dialogVisible = false
    }
  },
  created () {
    this.projectid = this.$store.getters.projectid
  }
}
</script>

<style></style>
