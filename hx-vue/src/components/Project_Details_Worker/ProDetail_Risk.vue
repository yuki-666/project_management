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
        <el-table-column type="expand">
          <template slot-scope="props">
            <el-form label-position="left" inline class="demo-table-expand">
              <el-form-item label="风险ID：">
                <span>{{ props.row.id}}</span>
              </el-form-item>
              <el-form-item label="风险类型：">
                <span>{{ props.row.type }}</span>
              </el-form-item>
              <el-form-item label="风险描述：">
                <span>{{ props.row.describe }}</span>
              </el-form-item>
              <el-form-item label="风险级别：" column-key="level">
                <span>{{  FLOWS_LEVEL[props.row.level] }}</span>
              </el-form-item>
              <el-form-item label="风险影响度：">
                <span>{{ props.row.effect }}</span>
              </el-form-item>
              <el-form-item label="风险应对策略：">
                <span>{{ props.row.solve }}</span>
              </el-form-item>
              <el-form-item label="风险状态：">
                <span>{{ FLOWS_STATUS[props.row.status] }}</span>
              </el-form-item>
              <el-form-item label="风险责任人">
                <span>{{ props.row.duty_name }}</span>
              </el-form-item>
              <el-form-item label="风险跟踪频度：">
                <span>{{ props.row.rate }}</span>
              </el-form-item>
              <el-form-item label="风险相关者">
                <span>{{ props.row.follower_name }}</span>
              </el-form-item>
            </el-form>
          </template>
        </el-table-column>
        <el-table-column label="风险描述" prop="describe"></el-table-column>
        <el-table-column label="风险级别" prop="level"
         column-key="level"
          :filters="filter_level"
          filter-placement="bottom-end"
        >
          <template slot-scope="props">
            <zx-tag>
              {{ FLOWS_LEVEL[props.row.level] }}
            </zx-tag>
          </template></el-table-column>
        <el-table-column label="风险状态" prop="status" column-key="status"
          :filters="filter_status"
          filter-placement="bottom-end"
        >
          <template slot-scope="props">
            <zx-tag>
              {{ FLOWS_STATUS[props.row.status] }}
            </zx-tag>
          </template></el-table-column>
        <el-table-column label="风险责任人" prop="duty_name"></el-table-column>-column>
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
  name: 'ProRisk',
  components: {
    'side-menu': SideMenu,
    'zx-tag': ZxTag
  },
  data () {
    return {
      select: '',
      dialogVisible: false,
      dialogVisible1: false,
      currentPage: 1,
      pagesize: 5,
      total: 10,
      filter_level: [
        { text: '低', value: 0 },
        { text: '中', value: 1 },
        { text: '高', value: 2 }
      ],
      FLOWS_LEVEL: [
        '低',
        '中',
        '高'
      ],
      filter_status: [
        { text: '未修复', value: 0 },
        { text: '已修复', value: 1 }
      ],
      FLOWS_STATUS: [
        '未修复',
        '已修复'
      ],
      projects: [{
        id: '',
        type: '',
        describe: '',
        level: '',
        effect: '',
        solve: '',
        status: '',
        duty_id: '',
        duty_name: '',
        follower_id: '',
        follower_name: '',
        rate: ''
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
  color: #99a9bf;
}
.pag {
  margin: 10px 70%;
}
</style>
