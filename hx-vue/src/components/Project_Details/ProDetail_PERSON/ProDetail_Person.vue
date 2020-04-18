<template>
  <div>
    <!-- <div> -->
       <!-- <template slot-scope="scope"> -->
          <!-- </template> -->
    <!-- </div> -->
    <el-button type="primary" style="float: right" round @click="handleAdd">添加人员</el-button>
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
        <el-table-column label="员工姓名" prop="worker_name"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="primary" round @click="deletePerson(scope.$index, scope.row)">删除</el-button>
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
    <add-form
      :show.sync="dialogVisible4"
      :zid="tmpId"
      @updateAgain="this.getAllProjects"
      ref="edit"
    ></add-form>
  </div>
</template>

<script>
import SideMenu from '../ProDetail_SideMenu'
import PerAdd from './ProDetail_PerAdd'
export default {
  name: 'ProDetailFUNCTION',
  components: {
    'side-menu': SideMenu,
    'add-form': PerAdd
  },
  data () {
    return {
      select: '',
      dialogVisible4: false,
      tmpId: '-1',
      tableDataTmp: [],
      currentPage: 1,
      pagesize: 5,
      total: 10,
      projects: [
        {
          worker_id: '',
          worker_name: ''
        }
      ]
    }
  },
  methods: {
    deletePerson: function (index, row) {
      let _this = this
      this.$confirm('此操作将在该项目中删除该员工, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      })
        .then(() => {
          this.$axios
            .post('/project_detail/project_worker/delete', {
              project_id: _this.projectid,
              worker_id: row.worker_id
            })
            .then(resp => {
              if (resp.data.status === 'ok') {
                this.getAllProjects()
                this.$message.success('删除成功')
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
        .get('/project_detail/project_worker/add/show', {
          params: {
            project_id: _this.projectid
          }
        })
        .then(successResponse => {
          _this.$refs.edit.form = successResponse.data
          console.log(successResponse.data)
        })
    },
    handleAdd () {
      this.getAllInfo()
      this.dialogVisible4 = true
    },
    handleCurrentChange (currentPage) {
      this.currentPage = currentPage
    },
    // 获取全部项目
    getAllProjects () {
      var _this = this
      this.$axios
        .get('/project_detail/project_worker', {
          params: {
            id: _this.projectid
          }
        })
        .then(successResponse => {
          _this.projects = successResponse.data
        })
        .catch(failResponse => {
        })
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
  margin: 20px 10%;
  position: relative;
  // margin-left: auto;
  // margin-right: auto;
}
.demo-table-expand {
  font-size: 0;
}
.demo-table-expand label {
  width: 90px;
  color: #99a9bf;
}
.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
  color: red;
}
.pag {
  margin: 5px 70%;
}
</style>
