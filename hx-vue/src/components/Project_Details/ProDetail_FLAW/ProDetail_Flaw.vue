<template>
  <div>
    <el-button type="primary" style="float: right" round @click="newClick">新建缺陷</el-button>
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
        <el-table-column label="缺陷ID" prop="id"></el-table-column>
        <el-table-column label="缺陷内容" prop="describe"></el-table-column>
        <el-table-column label="优先级" prop="level" sortable></el-table-column>
        <el-table-column label="跟进人" prop="follower"></el-table-column>
        <el-table-column label="缺陷状态" prop="status"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="text" @click="handleEdit(scope.$index, scope.row)">修改</el-button>
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
      :zid="tmpId"
      @updateAgain="this.getAllProjects"
      ref="edit1"
    ></add-form>
  </div>
</template>

<script>
// import FlawEdit from './ProDetail_FlawEdit'
import SideMenu from '../ProDetail_ManagerSideMenu'
import FlawAdd from './ProDetail_FlawAdd'
import FlawEdit from './proDetail_FlawEdit'
export default {
  name: 'ProFLAW',
  components: {
    'side-menu': SideMenu,
    'add-form': FlawAdd,
    'edit-form': FlawEdit
  },
  data () {
    return {
      select: '',
      dialogVisible: false,
      dialogVisible1: false,
      tmpId: '-1',
      tableDataTmp: [],
      currentPage: 1,
      pagesize: 5,
      total: 10,
      projects: [{
        id: '',
        describe: '',
        level: '',
        follower_id: '',
        follower: '',
        status: ''
      }]
    }
  },
  methods: {
    newClick () {
      this.dialogVisible1 = true
    },
    handleEdit (index, row) {
      this.$refs.edit.form = {
        id: row.id,
        describe: row.describe,
        level: row.level,
        follower: row.follower_id,
        status: row.status
      }
      this.dialogVisible = true
    },
    // 获取全部项目
    getAllProjects () {
      var _this = this
      this.$axios
        .get('/project_detail/project_flaw', {
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
