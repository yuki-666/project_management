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
        stripe
        @filter-change="filterTagTable"
      >
        <el-table-column label="工时id" prop="id" sortable></el-table-column>
        <el-table-column
          label="worker_name"
          prop="worker_name"
          sortable
        ></el-table-column>
        <el-table-column
          label="功能名称"
          prop="function_name"
          sortable
        ></el-table-column>
        <el-table-column
          label="活动名称"
          prop="event_name"
          sortable
        ></el-table-column>
        <el-table-column
          label="start_time"
          prop="start_time"
          :sortable="true"
          :sort-method="sortByDate"
        ></el-table-column>
        <el-table-column
          label="end_time"
          prop="end_time"
          :sortable="true"
          :sort-method="sortByDate"
        ></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button
              size="mini"
              type="primary"
              @click="zhandleEdit(scope.$index, scope.row)"
              >确认</el-button
            >
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
    <!-- <edit-form :show.sync="dialogFormVisible" ref="edit"></edit-form> -->
    <el-dialog
      title="审批提醒"
      :visible.sync="dialogFormVisible"
      @close="dialogFormVisible = false"
    >
      <div slot="footer" class="dialog-footer">
        <el-button @click="auditNo">不 审 批</el-button>
        <el-button type="primary" @click="auditYes">审 批</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import EditForm from './Manager_editForm'
import SideMenu from './Manager_SideMenu'
import { FlowStatusRules } from '../../home/rule/data-config'
import ZxTag from '../../tag'
export default {
  name: 'ManagerRAudit',
  components: {
    'side-menu': SideMenu,
    'zx-tag': ZxTag,
    'edit-form': EditForm
  },
  data () {
    return {
      // arr: [],
      select: '',
      dialogFormVisible: false,
      uid: 0,
      wid: '', // 工时id
      tableDataTmp: [],
      currentPage: 1,
      pagesize: 5,
      total: 10,
      FlowStatusRules,
      status: 0,
      projects: [
        {
          id: '',
          worker_name: '',
          function_name: '',
          event_name: '',
          start_time: '',
          end_time: ''
        }
      ]
    }
  },
  methods: {
    auditNo () {
      // this.dialogFormVisible = false;
      this.status = 0 // 不同意
      this.auditConfirm()
    },
    auditYes () {
      // this.dialogFormVisible = false;
      this.status = 1 // 不同意
      this.auditConfirm()
    },
    auditConfirm () {
      let _this = this
      this.$axios
        .post('/approval/work_time/confirm', {
          id: _this.wid,
          status: _this.status
        })
        .then(successResponse => {
          let status = successResponse.data.status
          if (status === 'ok') {
            _this.dialogFormVisible = false
            this.$message.success('已经更新')
          }
        })
        .catch(failResponse => {
          this.$message.error('更新失败')
          // console.log('OMmmmG,my_audit')
        })
    },
    getAllInfo (value) {
      // console.log('xxx')
      let _this = this
      this.$axios
        .get('/approval/project/show', {
          params: {
            id: value
          }
        })
        .then(successResponse => {
          // console.log('hhzzzzzzhh')
          _this.$refs.edit.form = successResponse.data
          // console.log(_this.$refs.edit.form.name)
        })
    },
    zhandleEdit (index, row) {
      let _this = this
      _this.dialogFormVisible = true
      _this.wid = row.id
    },
    handleEdit (index, row) {
      // console.log(row.id + 'zzzzz')
      // console.log(this.$refs.edit.form.name)
      // let _this = this
      // console.log(_this.tableDataTmp[row].id + 'zhx')
      this.$refs.edit.form = {
        id: row.id
      }
      this.$refs.edit.form.id = row.id
      this.getAllInfo(row.id)
      this.dialogFormVisible = true
      // console.log(index, row)
      // console.log(this.dialogFormVisible)
    },
    filterTagTable (filters) {
      this.projects = this.tableDataTmp
      // eslint-disable-next-line eqeqeq
      if (filters.status.length == 0) {
        this.projects = this.tableDataTmp
      } else {
        this.currentPage = 1
        this.projects = this.tableDataTmp.filter(item =>
          // eslint-disable-next-line eqeqeq
          filters.status.some(ele => ele == item.status)
        )
      }
    },
    filterTag (value, row) {
      // console.log(value)
      return row.status === value
    },
    handleCurrentChange (currentPage) {
      this.currentPage = currentPage
      // console.log(`当前页: ${val}`);
    },
    sortByDate (obj1, obj2, column) {
      var a = Date.parse(obj1.update_time)
      var b = Date.parse(obj2.update_time)
      if (a > b) {
        return -1
      } else {
        return 1
      }
    },
    // 获取全部项目
    getAllProjects () {
      var _this = this
      this.$axios
        .get('/approval/work_time/initiative', {
          params: {
            uid: _this.uid
          }
        })
        .then(successResponse => {
          // console.log(successResponse)
          _this.projects = successResponse.data
          _this.tableDataTmp = successResponse.data
        })
        .catch(failResponse => {
          // console.log('OMmmmG,my_workTime')
        })
    }
  },
  created () {
    // this.arr = this.biu.biu2
    // console.log('hhhhhhh')
    this.uid = this.$route.query.uid
    this.getAllProjects()
  }
}
</script>

<style lang="scss" scoped>
.project_table {
  padding-top: 0;
  margin: 10px 20px;
  position: relative;
  // margin-left: auto;
  // margin-right: auto;
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
  color: red;
}
.pag {
  margin: 5px 70%;
}
</style>
