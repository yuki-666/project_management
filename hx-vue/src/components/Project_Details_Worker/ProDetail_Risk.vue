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
        <el-table-column label="风险id" prop="id"></el-table-column>
        <el-table-column label="风险内容" prop="describe"></el-table-column>
        <el-table-column label="优先级" prop="level" sortable></el-table-column>
        <el-table-column label="风险状态" prop="label"></el-table-column>
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
  name: 'ProRisk',
  components: {
    'side-menu': SideMenu
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
          id: '',
          describe: '',
          level: '',
          label: ''
        }
      ],
      level_dict: [{
        key: '0',
        value: '低'
      }, {
        key: '1',
        value: '中'
      }, {
        key: '2',
        value: '高'
      }],
      label_dict: [{
        key: '0',
        value: '存在'
      }, {
        key: '1',
        value: '已修复'
      }]
    }
  },
  methods: {
    handleCurrentChange (currentPage) {
      this.currentPage = currentPage
    },
    // 获取全部项目
    getAllProjects () {
      let _this = this
      this.$axios
        .get('/project_detail/project_risk', {
          params: {
            project_id: _this.projectid
          }
        })
        .then(successResponse => {
          _this.projects = successResponse.data
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
