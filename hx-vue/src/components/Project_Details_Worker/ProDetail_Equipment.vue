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
        <el-table-column label="设备ID" prop="id"></el-table-column>
        <el-table-column label="设备名称" prop="name"></el-table-column>
        <el-table-column label="管理者" prop="manager"></el-table-column>
        <el-table-column label="租借日期" prop="start_time"></el-table-column>
        <el-table-column label="到期日期" prop="end_time"></el-table-column>
        <el-table-column
          label="设备状态"
          prop="status"
          column-key="status"
          :filters="filter_status"
          filter-placement="bottom-end"
        >
          <template slot-scope="props">
            <zx-tag>{{ FLOWS_STATUS[props.row.status] }}</zx-tag>
          </template>
        </el-table-column>
        <el-table-column
          label="是否归还"
          prop="label"
          column-key="label"
          :filters="filter_label"
          filter-placement="bottom-end"
        >
          <template slot-scope="props">
            <zx-tag>{{ FLOWS_LABEL[props.row.label] }}</zx-tag>
          </template>>
        </el-table-column>
        <el-table-column label="归还日期" prop="return_time"></el-table-column>
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
  name: 'Equipment',
  components: {
    'zx-tag': ZxTag,
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
      projectid: '',
      filter_status: [
        { text: '损坏', value: 0 },
        { text: '完好', value: 1 }
      ],
      FLOWS_STATUS: ['损坏', '完好'],
      filter_label: [
        { text: '否', value: 0 },
        { text: '是', value: 1 }
      ],
      FLOWS_LABEL: ['否', '是'],
      projects: [
        {
          id: '',
          name: '',
          manager_id: '',
          manager: '',
          start_time: '',
          end_time: '',
          status: '',
          label: '',
          return_time: ''
        }
      ]
    }
  },
  methods: {
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
