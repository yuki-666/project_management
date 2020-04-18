<template>
  <div>
    <el-button type="primary" style="float: right" round @click="newClick">添加设备</el-button>
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
        <el-table-column label="设备ID" prop="id"></el-table-column>
        <el-table-column label="设备名称" prop="name"></el-table-column>
        <el-table-column label="管理者" prop="manager"></el-table-column>
        <el-table-column label="租借日期" prop="start_time" ></el-table-column>
        <el-table-column label="到期日期" prop="end_time"></el-table-column>
        <el-table-column label="设备状态" prop="status"></el-table-column>
        <el-table-column label="是否归还" prop="label"></el-table-column>
        <el-table-column label="归还日期" prop="return_time"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="text" @click="handleEdit(scope.$index, scope.row)">操作</el-button>
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
    <edit-form
      :show.sync="dialogVisible"
      @updateAgain="this.getAllProjects"
      ref="edit"
    ></edit-form>
    <add-form
      :show.sync="dialogVisible1"
      @updateAgain="this.getAllProjects"
      ref="edit1"
    ></add-form>
  </div>
</template>

<script>
import SideMenu from '../ProDetail_SideMenu'
import EEdit from './proDetail_EEdit'
import EAdd from './proDetail_EAdd'
export default {
  name: 'Equipment',
  components: {
    'side-menu': SideMenu,
    'edit-form': EEdit,
    'add-form': EAdd
  },
  data () {
    return {
      select: '',
      dialogVisible: false,
      dialogVisible1: false,
      currentPage: 1,
      pagesize: 5,
      total: 10,
      projects: [{
        id: '',
        name: '',
        manager_id: '',
        manager: '',
        start_time: '',
        end_time: '',
        status: '',
        label: '',
        return_time: ''
      }]
    }
  },
  methods: {
    handleEdit (index, row) {
      this.$refs.edit.form = {
        id: row.id,
        name: row.name,
        manager: row.manager_id,
        start_time: row.start_time,
        end_time: row.end_time,
        status: row.status,
        label: row.label,
        return_time: row.return_time
      }
      this.dialogVisible = true
    },
    newClick () {
      this.dialogVisible1 = true
    },
    handleCurrentChange (currentPage) {
      this.currentPage = currentPage
    },
    // 获取全部项目
    getAllProjects () {
      var _this = this
      this.$axios
        .get('/project_detail/project_equipment', {
          params: {
            project_id: _this.projectid
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
