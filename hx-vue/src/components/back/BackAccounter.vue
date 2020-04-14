<template>
<div>
  <el-button type="primary" style="float: left" icon="el-icon-circle-plus-outline" @click="newClick" >新建</el-button         >
  <el-table
    :data="tableData"
    border
    stripe
    style="width: 100%">
    <el-table-column
      prop="username"
      label="用户名"
      width="180">
    </el-table-column>
    <el-table-column
      prop="password"
      label="登录密码"
      width="180">
    </el-table-column>
  </el-table>
  <edit-form
      :show.sync="dialogFormVisible"
      ref="edit"
    ></edit-form>
  </div>
</template>

<script>
import AccEdit from './AccEdit'
export default {
  name: 'BackAccounter',
  components: {
    'edit-form': AccEdit },
  data () {
    return {
      dialogFormVisible: false,
      tableData: [{
        username: '',
        password: ''
      }]
    }
  },
  methods: {
    newClick () {
      this.dialogFormVisible = true
      this.clear()
    },
    getAllProjects () {
      var _this = this
      this.$axios
        .get('/back/show_super_account', {
          params: {
            username: '123'
          }
        })
        .then(successResponse => {
          _this.tableData = successResponse.data
        })
        .catch(failResponse => {})
    }
  },
  created () {
    // this.uid = this.$store.getters.uid
    // this.career = this.$store.getters.career
    this.getAllProjects()
  }
}
</script>
