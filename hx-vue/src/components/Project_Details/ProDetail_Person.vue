<template>
  <div>
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
        <el-table-column label="项目id" prop="project_id"></el-table-column>
        <el-table-column label="员工姓名" prop="name"></el-table-column>
        <el-table-column label="是否已在项目中" prop="status"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="primary" round @click="handleAdd(scope.$index, scope.row)"
              >添加人员</el-button>
          </template>
          <!-- </el-button-group> -->
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
      @updateAgain="this.getAllInfo"
      ref="edit"
    ></editfunc-form>
    <add-form
      :show.sync="dialogVisible3"
      :zid="tmpId"
      @updateAgain="this.getAllInfo"
      ref="edit"
    ></add-form>
  </div>
</template>

<script>
import SideMenu from './ProDetail_SideMenu'
// import FuncAdd from './ProDetail_FuncAdd'
// import { FlowStatusRules } from '../../home/rule/data-config'
// import ZxTag from '../../tag'
export default {
  name: 'ProDetailFUNCTION',
  components: {
    'side-menu': SideMenu
    // 'add-form': FuncAdd
  },
  data () {
    return {
      // arr: [],
      select: '',
      dialogVisible2: false,
      dialogVisible3: false,
      tmpId: '-1',
      tableDataTmp: [],
      currentPage: 1,
      pagesize: 5,
      total: 10,
      projects: [
        {
          project_id: '1',
          function_id: '2',
          function_name: '3',
          worker_id: '124,13523,23523463',
          worker_name: '4 asdn asdgkn asdlgh asodhgn',
          parent_function_id: '7'
        }
      ]
    }
  },
  methods: {
    // handleDelete (index, row) {
    //   let _this = this
    //   this.$confirm('此操作将永久删除此功能, 是否继续?', '提示', {
    //     confirmButtonText: '确定',
    //     cancelButtonText: '取消',
    //     type: 'warning'
    //   })
    //     .then(() => {
    //       // 前端删除 仅供测试
    //       let tmp = { id: row.id }
    //       let tmpArr = [tmp]
    //       _this.projects = _this.projects.filter(item =>
    //         tmpArr.every(ele => ele.id !== item.id)
    //       )
    //       _this.tmpId = row.id
    //       // 后端删除
    //       this.$axios
    //         .post('/project_detail/function/delete', {
    //           project_id: _this.tmpId,
    //           function_id: '-1'
    //         })
    //         .then(resp => {
    //           if (resp.data.status === 'ok') {
    //             this.getAllProjects()
    //             this.$message.success('已经删除')
    //           }
    //         })
    //     })
    //     .catch(() => {
    //       this.$message({
    //         type: 'info',
    //         message: '已取消删除'
    //       })
    //     })
    // },
    getAllInfo () {
      let _this = this
      this.$axios
        .get('/project_detail/project_worker', {
          params: {
            project_id: _this.tmpId
          }
        })
        .then(successResponse => {
          _this.$refs.edit.form = successResponse.data
        })
    },
    handleEdit (index, row) {
      this.$refs.edit.form = {
        id: row.id
      }
      this.tmpId = row.id
      this.$refs.edit.form.id = row.id
      this.getAllInfo()
      this.dialogVisible2 = true
    },
    handleAdd (index, row) {
      this.$refs.edit.form = {
        id: row.id
      }
      this.tmpId = row.id
      this.$refs.edit.form.id = row.id
      this.getAllInfo()
      this.dialogVisible3 = true
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
            id: _this.id
          }
        })
        .then(successResponse => {
          _this.projects = successResponse.data
          _this.tableDataTmp = successResponse.data
        })
        .catch(failResponse => {
        })
    }
  },
  created () {
    this.uid = this.$store.getters.uid
    this.getAllProjects()
  }
}
</script>

<style lang="scss" scoped>
.project_table {
  padding-top: 0;
  margin: 20px 100px;
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
  width: 50%;
  color: red;
}
.pag {
  margin: 10px 70%;
}
</style>
