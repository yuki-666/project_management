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
        <el-table-column label="缺陷内容" prop="flaw_detail"></el-table-column>
        <el-table-column label="优先级" prop="priority" sortable></el-table-column>
        <el-table-column label="跟进人" prop="follower"></el-table-column>
        <el-table-column label="缺陷状态" prop="status"></el-table-column>
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
  </div>
</template>

<script>
import SideMenu from './ProDetail_WorkerSideMenu'
export default {
  name: 'ProFLAW',
  components: {
    'side-menu': SideMenu
  },
  data () {
    return {
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
          equipment_name: '',
          begin_time: '',
          end_time: ''
        }
      ]
    }
  },
  methods: {
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
              project_id: '2020-0000-D-01',
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
        parent_function_id: row.function_id
      }
      // this.tmpId = row.id
      // this.$refs.edit.form.id = row.id
      // this.getAllInfo()
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
            id: '2020-0000-D-01'
          }
        })
        .then(successResponse => {
          _this.projects = successResponse.data
          // _this.tableDataTmp = successResponse.data
        })
        .catch(failResponse => {
        })
    }
  },
  created () {
    // this.uid = this.$store.getters.uid
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
