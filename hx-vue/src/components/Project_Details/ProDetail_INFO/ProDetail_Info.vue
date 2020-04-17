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
          <!-- <el-table-column
          label="项目状态"
          prop="status"
          column-key="status"
          :filters="filter_status"
          filter-placement="bottom-end"
        >
          <template slot-scope="props">
            <zx-tag :type="FlowStatusRules[props.row.status]">
              {{ FLOWS_STATUS[props.row.status] }}
            </zx-tag>
          </template> -->
        <!-- </el-table-column> -->
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
    <el-table-column label="状态" prop="stat"></el-table-column>
    <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="mini" @click="handleEdit(scope.$index, scope.row)"
              >查 看</el-button
            >
          </template>
        </el-table-column>
    </el-table>
    </div>
    <edit-form
      :show.sync="dialogFormVisible"
      :zid="tmpId"
      @updateAgain="this.getAllProjects"
      ref="edit"
    ></edit-form>
  </div>
</template>

<script>
import SideMenu from '../ProDetail_SideMenu'
import InfoEdit from './ProDetail_InfoEdit'
import { FlowStatusRules } from '../../home/rule/data-config'
import ZxTag from '../../tag/src/tag'
export default {
  name: 'ProDetailINFO',
  components: {
    'side-menu': SideMenu,
    'zx-tag': ZxTag,
    'edit-form': InfoEdit
  },
  data () {
    return {
      //   buttonFlag: false,
      tmpId: '-1',
      dialogFormVisible: this.show,
      FlowStatusRules,
      filter_status: [
        { text: 'rejection', value: 0 },
        { text: 'pending', value: 1 },
        { text: 'established', value: 2 },
        { text: 'processing', value: 3 },
        { text: 'paid', value: 4 },
        { text: 'finished', value: 5 },
        { text: 'archived', value: 6 }
      ],
      FLOWS_STATUS: [
        'rejection',
        'pending',
        'established',
        'processing',
        'paid',
        'finished',
        'archived'
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
    // handleEdit (index, row) {
    //   this.$refs.edit.form = {
    //     id: row.id
    //   }
    //   this.tmpId = row.id
    //   this.$refs.edit.form.id = row.id
    //   this.getAllInfo()
    //   this.dialogFormVisible = true
    // },
    // handleEdit (index, row) {
    //   console.log(index, row)
    // },
    getAllInfo () {
      let _this = this
      this.$axios
        .get('/project_detail/modify/show', {
          params: {
            id: _this.$route.query.id,
            // id: _this.id,
            name: _this.name,
            status: _this.status,
            update_time: _this.update_time,
            describe: _this.describe,
            scheduled_time: _this.scheduled_time,
            delivery_day: _this.delivery_day,
            project_superior_name: _this.project_superior_name,
            stonmajor_milestonese: _this.major_milestones,
            adopting_technology: _this.adopting_technology,
            business_area: _this.business_area,
            main_function: _this.main_function
          }
        })
        .then(successResponse => {
          _this.$refs.edit.form = successResponse.data
          _this.$refs.edit.form.status = _this.FLOWS_STATUS[successResponse.data.status]
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
            id: this.$route.query.id
          }
        })
        .then(successResponse => {
          _this.tableData = successResponse.data
        })
        .catch(failResponse => {})
    }
  },
  created () {
    // console.log(this.$route.query.id)
    localStorage.setItem('zprojectname', this.$route.query.id)
    this.$store.commit('handleProjectname', this.$route.query.id)
    console.log('124235262')
    console.log(this.$store.getters.projectname)
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
