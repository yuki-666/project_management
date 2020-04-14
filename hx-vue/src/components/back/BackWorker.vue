<template>
<div>
  <el-button type="primary" style="float: left"  icon="el-icon-circle-plus-outline" @click="newClick" >新建</el-button>
  <el-button type="primary" style="float: left" icon="el-icon-upload2" @click="newClick1" >上传</el-button>
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
      prop="name"
      label="姓名"
      width="180">
    </el-table-column>
    <el-table-column
      prop="career"
      label="职位"
      width="180">
    </el-table-column>
    <el-table-column
      prop="department"
      label="部门"
      width="180">
    </el-table-column>
    <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="primary" plain @click="editData(scope.$index, scope.row)" >修改</el-button
            >
            <el-button type="primary" plain @click="deleteData(index)">删除</el-button
            >
          </template>
        </el-table-column>
  </el-table>
  <edit-form
      :show.sync="dialogFormVisible"
      ref="edit"
    ></edit-form>
    <work-edit
      :show.sync="dialogForm"
      ref="create"
    ></work-edit>
    <file-edit
      :show.sync="dialogForm2"
      ref="create"
    ></file-edit>
  </div>
</template>

<script>
import EditForm from './EditForm'
import WorkerEdit from './WorkerEdit'
import FileEdit from './FileEdit'
export default {
  name: 'BackWorker',
  components: {
    'edit-form': EditForm,
    'work-edit': WorkerEdit,
    'file-edit': FileEdit
  },
  data () {
    return {
      dialogFormVisible: false,
      dialogForm: false,
      dialogForm2: false,
      tableData: [{
        username: '',
        name: '',
        career: '',
        department: ''
      }]
    }
  },
  methods: {
    deleteData: function (index) {
      this.$confirm('此操作将永久删除该员工信息, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.tableData.splice(index, 1)
        this.$message({
          type: 'success',
          message: '删除成功!'
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消删除'
        })
      })
    },
    editData (index, row) {
      this.$refs.edit.form = {
        username: row.username,
        name: row.name,
        career: row.career,
        department: row.department
      }
      // this.tmpId = row.id
      // this.getAllInfo()
      this.dialogFormVisible = true
      // this.$refs.edit.form = {
      //   username: item.username,
      //   password: item.password,
      // }
    },
    newClick () {
      this.dialogForm = true
    },
    newClick1 () {
      this.dialogForm2 = true
    },
    getAllProjects () {
      var _this = this
      this.$axios
        .get('/back/show_normal_account', {
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
