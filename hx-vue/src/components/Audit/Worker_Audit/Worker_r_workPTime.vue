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
        <el-table-column label="工时ID" prop="id" sortable></el-table-column>
        <el-table-column
          label="项目名称"
          prop="project_name"
          sortable
        ></el-table-column>
        <el-table-column
          label="功能名称"
          prop="function_name"
          sortable
        ></el-table-column>
        <el-table-column
          label="事件名称"
          prop="event_name"
          sortable
        ></el-table-column>
        <el-table-column
          label="开始时间"
          prop="start_time"
          :sortable="true"
          :sort-method="sortByDate"
        ></el-table-column>
        <el-table-column
          label="结束时间"
          prop="end_time"
          :sortable="true"
          :sort-method="sortByDate2"
        ></el-table-column>
        <el-table-column label="status" prop="status"
          ><template slot-scope="props">
            <zx-tag :type="FlowStatusRules[props.row.status]">
              {{ FLOWS_STATUS[props.row.status] }}
            </zx-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="mini" type="primary" round @click="handleEdit(scope.$index, scope.row)"
              >修改</el-button
            >
            <el-button
              size="mini"
              type="danger"
              round
              @click="handleDelete(scope.$index, scope.row)"
              >删除</el-button
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
    <edit-form
      :show.sync="dialogFormVisible"
      :zid="tmpId"
      @updateAgain="this.getAllProjects"
      ref="edit"
    ></edit-form>
  </div>
</template>

<script>
import EditForm from './Worker_editForm'
import SideMenu from './Worker_SideMenu'
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
      tmpId: '-1',
      tableDataTmp: [],
      currentPage: 1,
      pagesize: 5,
      total: 10,
      FlowStatusRules,
      filter_status: [
        { text: '驳回', value: 0 },
        { text: '审批中', value: 1 },
        { text: '已审批', value: 2 }
      ],
      FLOWS_STATUS: ['驳回', '审批中', '已审批'],
      projects: [
        {
          id: '',
          project_name: '',
          function_name: '',
          event_name: '',
          start_time: '',
          end_time: '',
          status: ''
        }
      ]
    }
  },
  methods: {
    handleDelete (index, row) {
      let _this = this
      this.$confirm('此操作将删除该工时, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      })
        .then(() => {
          _this.tmpId = row.id
          this.$axios
            .post('/approval/work_time/passive/delete', { id: _this.tmpId })
            .then(resp => {
              if (resp.data.status === 'ok') {
                this.getAllProjects()
                this.$message.success('已经删除')
              }
            })
        })
        .catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          })
        })
    },
    getAllInfo () {
      let _this = this
      this.$axios
        .get('/approval/work_time/passive/show', {
          params: {
            id: _this.tmpId
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
      return row.status === value
    },
    handleCurrentChange (currentPage) {
      this.currentPage = currentPage
    },
    sortByDate (obj1, obj2, column) {
      var a = Date.parse(obj1.start_time)
      var b = Date.parse(obj2.start_time)
      if (a > b) {
        return -1
      } else {
        return 1
      }
    },
    sortByDate2 (obj1, obj2, column) {
      var a = Date.parse(obj1.end_time)
      var b = Date.parse(obj2.end_time)
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
        .get('/approval/work_time/passive', {
          params: {
            uid: _this.uid
          }
        })
        .then(successResponse => {
          _this.projects = successResponse.data
          _this.tableDataTmp = successResponse.data
        })
        .catch(failResponse => {
        })
    }
  },
  created () {
    this.uid = this.$store.getters.uid
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
