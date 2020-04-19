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
        <el-table-column label="功能ID" prop="function_id"></el-table-column>
        <el-table-column label="功能名称" prop="function_name" sortable></el-table-column>
        <el-table-column label="员工姓名" prop="worker_name" show-overflow-tooltip></el-table-column>
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
  name: 'ProDetailFUNCTION',
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
          function_id: '',
          function_name: '',
          worker_name: ''
        }
      ]
    }
  },
  methods: {
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
  margin: 10px 20%;
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
