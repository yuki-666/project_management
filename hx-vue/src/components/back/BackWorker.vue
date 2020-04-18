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
        <el-button type="primary" plain @click="editData(scope.$index, scope.row)">修改</el-button>
        <el-button type="primary" plain @click="deleteData(scope.$index, scope.row)">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
    <edit-form
      :show.sync="dialogFormVisible"
      :zid="tmpId"
      @updateAgain="this.getAllProjects"
      ref="edit"
    ></edit-form>
    <work-edit
      :show.sync="dialogForm"
      @updateAgain="this.getAllProjects"
      ref="create"
    ></work-edit>
    <file-edit
      :show.sync="dialogForm2"
      @updateAgain="this.getAllProjects"
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
        id: '',
        username: '',
        name: '',
        career: '',
        department: ''
      }]
    }
  },
  methods: {
    deleteData (index, row) {
      this.$confirm('此操作将删除该员工, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$axios
          .post('/back/delete_normal_account', { id: row.id })
          .then(resp => {
            if (resp.data.status === 'ok') {
              this.getAllProjects()
              this.$message.success('已经删除')
            }
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
        id: row.id,
        username: row.username,
        name: row.name,
        career: row.career,
        department: row.department
      }
      this.dialogFormVisible = true
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
        .get('/back/show_normal_account')
        .then(successResponse => {
          _this.tableData = successResponse.data
        })
        .catch(failResponse => {})
    }
  },
  created () {
    this.getAllProjects()
  }
}
</script>
