<template>
  <div>
    <el-dialog
      title="新建风险"
      :visible.sync="dialogVisible"
      @close="$emit('update:show', false)"
      center
    >
      <el-form :model="form">
        <el-form-item label="风险类型" :label-width="formLabelWidth" prop="type">
          <el-input v-model="form.type" autocomplete="off" placeholder="请输入内容"></el-input>
        </el-form-item>
        <el-form-item label="风险描述" :label-width="formLabelWidth" prop="describe">
          <el-input v-model="form.describe" autocomplete="off" placeholder="请输入内容"></el-input>
        </el-form-item>
        <el-form-item label="风险级别" :label-width="formLabelWidth" prop="level">
          <el-select v-model="form.level" placeholder="请选择风险级别">
            <el-option
              v-for="item in level_dict"
              :key="item.key"
              :label="item.value"
              :value="item.key"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="风险影响度" :label-width="formLabelWidth" prop="effect">
          <el-input v-model="form.effect" autocomplete="off" placeholder="请输入内容"></el-input>
        </el-form-item>
        <el-form-item label="风险应对策略" :label-width="formLabelWidth" prop="solve">
          <el-input v-model="form.solve" autocomplete="off" placeholder="请输入内容"></el-input>
        </el-form-item>
        <el-form-item label="风险责任人" :label-width="formLabelWidth" prop="duty">
          <el-select v-model="form.duty" placeholder="请选择责任人">
            <el-option
              v-for="item in member"
              :key="item.worker_id"
              :label="item.worker_name"
              :value="item.worker_id"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="风险相关者" :label-width="formLabelWidth" prop="follower">
          <el-select v-model="form.follower" placeholder="请选择相关者">
            <el-option
              v-for="item in member"
              :key="item.worker_id"
              :label="item.worker_name"
              :value="item.worker_id"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="风险跟踪频度" :label-width="formLabelWidth" prop="rate">
          <el-input v-model="form.rate" autocomplete="off" placeholder="请输入内容"></el-input>
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
      projectid: '',
      form: {
        id: '',
        type: '',
        describe: '',
        level: '',
        effect: '',
        solve: '',
        duty: '',
        rate: '',
        follower: ''
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
      member: [{
        worker_id: '',
        worker_name: ''
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
    getMember () {
      var _this = this
      this.$axios
        .get('/project_detail/get_user', {
          params: {
            project_id: _this.projectid
          }
        })
        .then(successResponse => {
          _this.member = successResponse.data
        })
        .catch(failResponse => {
        })
    },
    onSubmit () {
      let _this = this
      this.$axios
        .post('/project_detail/project_risk/add', {
          id: _this.form.id,
          project_id: _this.projectid,
          type: _this.form.type,
          describe: _this.form.describe,
          level: _this.form.level,
          effect: _this.form.effect,
          solve: _this.form.solve,
          duty: _this.form.duty,
          rate: _this.form.rate,
          follower: _this.form.follower
        })
        .then(resp => {
          if (resp.data.status === 'ok') {
            this.dialogFormVisible = false
            this.$emit('update:show', false)
            this.$emit('updateAgain')
            _this.form.type = ''
            _this.form.describe = ''
            _this.form.level = ''
            _this.form.effect = ''
            _this.form.solve = ''
            _this.form.duty = ''
            _this.form.rate = ''
            _this.form.follower = ''
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
    this.getMember()
  }
}
</script>

<style></style>
