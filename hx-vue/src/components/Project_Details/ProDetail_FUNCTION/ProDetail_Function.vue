<template>
  <div>
    <el-button size="mini" type="primary" style="float: right" round @click="Add">添加功能</el-button>
    <div class="project_table">
      <el-table
        :data="
          projects.slice(
            (this.currentPage - 1) * pagesize,
            this.currentPage * pagesize
          )
        "
        style="width:100%"
        header-row-style="height:50px"
        stripe
        @filter-change="filterTagTable"
      >
        <el-table-column label="功能ID" prop="function_id"></el-table-column>
        <el-table-column
          label="功能名称"
          prop="function_name"
          sortable
        ></el-table-column>
        <el-table-column label="员工姓名" prop="worker_name" show-overflow-tooltip></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="mini" type="text" @click="handleAdd(scope.$index, scope.row)">添加功能</el-button>
            <el-button size="mini" type="text" @click="handleEdit(scope.$index, scope.row)">修改</el-button>
            <el-button size="mini" type="text" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
            <el-button size="mini" type="text" @click="handleAddPerson(scope.$index, scope.row)">添加人员</el-button>
            <el-button size="mini" type="text" @click="handleDeletePerson(scope.$index, scope.row)">删除人员</el-button>
          </template>
        </el-table-column>
      </el-table>
      <el-row class="pag">
        <el-pagination
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-size="pagesize"
          :total="projects.length"
        >
        </el-pagination>
      </el-row>
    </div>
    <editfunc-form
      :show.sync="dialogVisible2"
      :zid="tmpId"
      @updateAgain="this.getAllProjects"
      ref="edit2"
    ></editfunc-form>
    <add-form
      :show.sync="dialogVisible3"
      :zid="tmpId"
      @updateAgain="this.getAllProjects"
      ref="edit1"
    ></add-form>
    <add-person-form
      :show.sync="dialogVisibleAddPerson"
      :zid="tmpId"
      @updateAgain="this.getAllProjects"
      ref="edit"
    ></add-person-form>
    <delete-person-form
      :show.sync="dialogVisibleDeletePerson"
      :zid="tmpId"
      @updateAgain="this.getAllProjects"
      ref="editDel"
    ></delete-person-form>
  </div>
</template>

<script>
import FuncEdit from './ProDetail_FuncEdit'
import SideMenu from '../ProDetail_ManagerSideMenu'
import FuncAdd from './ProDetail_FuncAdd'
import FuncAddPerson from './ProDetail_FuncAddPerson'
import FuncDeletePerson from './ProDetail_FuncDeletePerson'
export default {
  name: 'ProDetailFUNCTION',
  components: {
    'side-menu': SideMenu,
    'editfunc-form': FuncEdit,
    'add-form': FuncAdd,
    'add-person-form': FuncAddPerson,
    'delete-person-form': FuncDeletePerson
  },
  data () {
    return {
      projectid: '',
      worker_id: '',
      function_id: '',
      select: '',
      dialogVisible2: false,
      dialogVisible3: false,
      dialogVisibleAddPerson: false,
      dialogVisibleDeletePerson: false,
      tmpId: '-1',
      tableDataTmp: [],
      currentPage: 1,
      pagesize: 5,
      total: 10,
      projects: [
        {
          function_id: '',
          function_name: '',
          worker_name: ''
        }
      ]
    }
  },
  methods: {
    Add () {
      this.$refs.edit1.form.parent_function_id = '000'
      this.dialogVisible3 = true
    },
    handleDelete (index, row) {
      let _this = this
      this.$confirm('此操作将永久删除此功能, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      })
        .then(() => {
          _this.tmpId = row.function_id
          this.$axios
            .post('/project_detail/function/delete', {
              project_id: _this.projectid,
              function_id: _this.tmpId
            })
            .then(resp => {
              if (resp.data.status === 'ok') {
                this.getAllProjects()
                this.$message.success('已经删除')
              }
            })
        })
        .catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          })
        })
    },
    getAllInfo () {
      let _this = this
      this.$axios
        .get('/project_detail/function', {
          params: {
            project_id: _this.projectid
          }
        })
        .then(successResponse => {
          _this.$refs.edit.form = successResponse.data
        })
    },
    getAllPerson () {
      let _this = this
      this.$axios
        .get('/project_detail/function/person/add/get', {
          params: {
            project_id: _this.projectid,
            function_id: _this.$refs.edit.form.function_id
          }
        })
        .then(successResponse => {
          _this.$refs.edit.member = successResponse.data
        })
    },
    getAllDeletePerson () {
      let _this = this
      this.$axios
        .get('/project_detail/function/person/delete/get', {
          params: {
            project_id: _this.projectid,
            function_id: _this.$refs.editDel.form.function_id
          }
        })
        .then(successResponse => {
          _this.$refs.editDel.member = successResponse.data
        })
    },
    handleEdit (index, row) {
      this.$refs.edit2.form.function_id = row.function_id
      this.$refs.edit2.form.function_name = row.function_name
      this.dialogVisible2 = true
    },
    handleAdd (index, row) {
      this.$refs.edit1.form.parent_function_id = row.function_id
      this.dialogVisible3 = true
    },
    handleAddPerson (index, row) {
      this.$refs.edit.form.function_id = row.function_id
      this.getAllPerson()
      this.dialogVisibleAddPerson = true
    },
    handleDeletePerson (index, row) {
      this.$refs.editDel.form.function_id = row.function_id
      this.getAllDeletePerson()
      this.dialogVisibleDeletePerson = true
    },
    handleCurrentChange (currentPage) {
      this.currentPage = currentPage
    },
    // 获取全部项目
    getAllProjects () {
      var _this = this
      this.$axios
        .get('/project_detail/function', {
          params: {
            id: _this.projectid
          }
        })
        .then(successResponse => {
          _this.projects = successResponse.data
        })
        .catch(failResponse => {})
    }
  },
  created () {
    this.projectid = this.$store.getters.projectid
    this.getAllProjects()
  }
}
</script>

<style lang="scss" scoped>
.project_table {
  padding-top: 0;
  margin: 10px 10%;
  position: relative;
  // margin-left: auto;
  // margin-right: auto;
}
.demo-table-expand {
  font-size: 0;
}
.demo-table-expand label {
  width: 20px;
  color: #99a9bf;
}
.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 20%;
  color: red;
}
.pag {
  margin: 10px 70%;
}
</style>
