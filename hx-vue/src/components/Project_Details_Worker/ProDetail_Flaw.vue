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
        <el-table-column label="缺陷ID" prop="id"></el-table-column>
        <el-table-column label="缺陷内容" prop="describe"></el-table-column>
        <el-table-column label="优先级" prop="level" column-key="level"
          :filters="filter_level"
          filter-placement="bottom-end"
        >
          <template slot-scope="props">
            <zx-tag>
              {{ FLOWS_LEVEL[props.row.level] }}
            </zx-tag>
          </template></el-table-column>
        <el-table-column label="跟进人" prop="follower_name"></el-table-column>
        <el-table-column label="缺陷状态" prop="status" column-key="status"
          :filters="filter_status"
          filter-placement="bottom-end"
        >
          <template slot-scope="props">
            <zx-tag>
              {{ FLOWS_STATUS[props.row.status] }}
            </zx-tag>
          </template></el-table-column>
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
import ZxTag from '../tag/src/tag'
export default {
  name: 'ProFLAW',
  components: {
    'zx-tag': ZxTag,
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
      projectid: '',
      filter_status: [
        { text: '未修复', value: 0 },
        { text: '已修复', value: 1 }
      ],
      FLOWS_STATUS: ['未修复', '已修复'],
      filter_level: [
        { text: '低', value: 0 },
        { text: '中', value: 1 },
        { text: '高', value: 2 }
      ],
      FLOWS_LEVEL: ['低', '中', '高'],
      projects: [{
        id: '',
        describe: '',
        level: '',
        follower_id: '',
        follower_name: '',
        status: ''
      }]
    }
  },
  methods: {
    handleCurrentChange (currentPage) {
      this.currentPage = currentPage
    },
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
