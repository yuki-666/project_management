<template>
  <div>
    <div class="project_table">
    <el-table :data="tableData" style="width:100%" header-row-style="height:50px" stripe @filter-change="filterTagTable">
    <el-table-column type="expand">
      <template slot-scope="props">
        <el-form label-position="left" inline class="demo-table-expand">
          <el-form-item label="项目ID">
            <span>{{ props.row.id }}</span>
          </el-form-item>
          <el-form-item label="项目名称">
            <span>{{ props.row.name }}</span>
          </el-form-item>
          <el-form-item label="更新时间">
            <span>{{ props.row.update_time }}</span>
          </el-form-item>
          <el-form-item label="项目描述">
            <span>{{ props.row.describe }}</span>
          </el-form-item>
          <el-form-item label="预定时间">
            <span>{{ props.row.scheduled_time }}</span>
          </el-form-item>
          <el-form-item label="交付日">
            <span>{{ props.row.delivery_day }}</span>
          </el-form-item>
          <el-form-item label="项目上级">
            <span>{{ props.row.project_superior_name }}</span>
          </el-form-item>
          <el-form-item label="主要里程碑">
            <span>{{ props.row.major_milestones }}</span>
          </el-form-item>
          <el-form-item label="采用技术">
            <span>{{ props.row.adopting_technology }}</span>
          </el-form-item>
          <el-form-item label="业务领域">
            <span>{{ props.row.business_area }}</span>
          </el-form-item>
          <el-form-item label="主要功能">
            <span>{{ props.row.main_function }}</span>
          </el-form-item>
        </el-form>
      </template>
    </el-table-column>
    <el-table-column label="项目ID" prop="id"></el-table-column>
    <el-table-column label="名称" prop="name"></el-table-column>
    <el-table-column label="状态" prop="status" column-key="status" :filters="filter_status" filter-placement="bottom-end">
      <template slot-scope="props">
        <zx-tag :type="FlowStatusRules[props.row.status]">
          {{ FLOWS_STATUS[props.row.status] }}
        </zx-tag>
      </template>
    </el-table-column>
    </el-table>
    </div>
  </div>
</template>

<script>
import SideMenu from './ProDetail_WorkerSideMenu'
import { FlowStatusRules } from '../home/rule/data-config'
import ZxTag from '../tag/src/tag'
export default {
  name: 'ProDetailINFO',
  components: {
    'side-menu': SideMenu,
    'zx-tag': ZxTag
  },
  data () {
    return {
      //   buttonFlag: false,
      tmpId: '-1',
      dialogFormVisible: this.show,
      FlowStatusRules,
      filter_status: [
        { text: '驳回', value: 0 },
        { text: '审批中', value: 1 },
        { text: '已立项', value: 2 },
        { text: '进行中', value: 3 },
        { text: '已交付', value: 4 },
        { text: '已结束', value: 5 },
        { text: '已归档', value: 6 }
      ],
      FLOWS_STATUS: [
        '驳回',
        '审批中',
        '已立项',
        '进行中',
        '已交付',
        '已结束',
        '已归档'
      ],
      tableData: [
        {
          id: '',
          name: '',
          status: '',
          update_time: '',
          describe: '',
          scheduled_time: '',
          delivery_day: '',
          project_superior_name: '',
          major_milestones: '',
          adopting_technology: '',
          business_area: '',
          main_function: ''
        }
      ]
    }
  },
  methods: {
    getAllInfo () {
      let _this = this
      this.$axios
        .get('/project_detail/modify/show', {
          params: {
            id: _this.projectid
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
      this.dialogFormVisible = true
    },
    // 获取全部项目
    getAllProjects () {
      var _this = this
      this.$axios
        .get('/project_detail/info', {
          params: {
            id: _this.projectid
          }
        })
        .then(successResponse => {
          _this.tableData = successResponse.data
        })
        .catch(failResponse => {})
    }
  },
  created () {
    localStorage.setItem('zprojectid', this.$route.query.id)
    this.$store.commit('handleProjectid', this.$route.query.id)
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
  width: 90px;
  color: #99a9bf;
}
.demo-table-expand .el-form-item {
  margin-right: 0;
  margin-bottom: 0;
  width: 50%;
}
.pag {
  margin: 5px 70%;
}
</style>
