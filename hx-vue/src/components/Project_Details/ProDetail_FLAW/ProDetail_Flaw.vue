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
            <el-button type="text" @click="handleEdit(scope.$index, scope.row)"
              >操作</el-button>
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
import SideMenu from '../ProDetail_SideMenu'
import FlawAdd from './ProDetail_FlawAdd'
import FlawEdit from './proDetail_FlawEdit'
// import { FlowStatusRules } from '../../home/rule/data-config'
// import ZxTag from '../../tag'
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
      projects: [
        {
          id: '',
          describe: '',
          level: '',
          follower: '',
          status: ''
        }
      ]
    }
  },
  methods: {
    newClick () {
      this.dialogVisible1 = true
    },
    handleEdit (index, row) {
      this.$refs.edit.form = {
        describe: row.describe,
        level: row.level,
        follower: row.follower,
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
            project_id: '2020-04-18'
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
