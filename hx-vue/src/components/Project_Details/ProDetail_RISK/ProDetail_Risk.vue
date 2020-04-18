<template>
  <div>
    <el-button type="primary" style="float: right" round @click="newClick">新建风险</el-button>
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
        <el-table-column label="风险内容" prop="describe"></el-table-column>
        <el-table-column label="优先级" prop="level" sortable></el-table-column>
        <el-table-column label="风险状态" prop="label"></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button type="text" @click="handleEdit(scope.$index, scope.row)"
              >修改</el-button>
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
    <risk-edit
      :show.sync="dialogVisible"
      @updateAgain="this.getAllProjects"
      ref="edit"
    ></risk-edit>
    <risk-add
      :show.sync="dialogVisible1"
      @updateAgain="this.getAllProjects"
      ref="edit1"
    ></risk-add>
  </div>
</template>

<script>
// import FlawEdit from './ProDetail_FlawEdit'
import SideMenu from '../ProDetail_SideMenu'
// import FlawAdd from './ProDetail_FlawAdd'
// import { FlowStatusRules } from '../../home/rule/data-config'
// import ZxTag from '../../tag'
import RiskEdit from './proDetail_RiskEdit'
import RiskAdd from './proDetail_RiskAdd'
export default {
  name: 'ProRisk',
  components: {
    'side-menu': SideMenu,
    'risk-edit': RiskEdit,
    'risk-add': RiskAdd
    // 'add-form': FlawAdd
  },
  data () {
    return {
      select: '',
      dialogVisible: false,
      dialogVisible1: false,
      currentPage: 1,
      pagesize: 5,
      total: 10,
      projects: [
        {
          describe: '',
          level: '',
          label: ''
        }
      ]
    }
  },
  methods: {
    handleEdit (index, row) {
      this.$refs.edit.form = {
        describe: row.describe,
        level: row.level,
        label: row.label
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
      let _this = this
      this.$axios
        .get('/project_detail/project_risk', {
          params: {
            project_id: '2020-04-18'
          }
        })
        .then(successResponse => {
          _this.projects = successResponse.data
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
