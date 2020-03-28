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
          label="function_name"
          prop="function_name"
          sortable
        ></el-table-column>
        <el-table-column
          label="event_name"
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
            <el-button size="mini" @click="handleEdit(scope.$index, scope.row)"
              >修改</el-button
            >
            <el-button
              size="mini"
              type="danger"
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
      @updateAgain="this.getAllInfo"
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
      tmpId: -1,
      tableDataTmp: [],
      currentPage: 1,
      pagesize: 5,
      total: 10,
      FLOWS_STATUS: [
        '驳回',
        '已审批'
      ],
      FlowStatusRules,
      filter_status: [
        { text: 'pending', value: 0 },
        { text: 'established', value: 1 },
        { text: 'processing', value: 2 },
        { text: 'paid', value: 3 },
        { text: 'finished', value: 4 },
        { text: 'archived', value: 5 },
        { text: 'rejection', value: 6 }
      ],
      projects: [
        {
          id: '',
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
      this.$confirm('此操作将永久删除该书籍, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      })
        .then(() => {
          // 前端删除 仅供测试
          let tmp = { id: row.id }
          console.log('zhxxxxxx' + row.id)
          let tmpArr = [tmp]
          _this.projects = _this.projects.filter(item =>
            tmpArr.every(ele => ele.id !== item.id)
          )
          _this.tmpId = row.id
          // 后端删除
          this.$axios
            .post('/approval/work_time/passive/delete', { id: _this.tmpId })
            .then(resp => {
              if (resp.data.status === 'ok') {
                console.log(resp.data.status)
                this.$message.success('已经删除')
                // this.getAllProjects()
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
    zhxFun () {
      console.log('fuccckkkkkkkk')
    },
    getAllInfo () {
      // console.log('xxx')
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
      console.log(row.id + 'zzzzz')
      console.log(this.$refs.edit.form.name)
      // let _this = this
      // console.log(_this.tableDataTmp[row].id + 'zhx')
      this.$refs.edit.form = {
        id: row.id
      }
      this.tmpId = row.id
      this.$refs.edit.form.id = row.id
      console.log(this.$refs.edit.form.id)
      this.getAllInfo()
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
          // console.log(successResponse)
          _this.projects = successResponse.data
          _this.tableDataTmp = successResponse.data
        })
        .catch(failResponse => {
          console.log('OMmmmG,my_audit')
        })
    }
  },
  created () {
    // this.arr = this.biu.biu2
    // console.log('hhhhhhh')
    this.uid = this.$route.query.uid
    this.getAllProjects()
    console.log('try3')
    // console.log(store.getters.uid)
    console.log(this.$store.getters.uid)
    // console.log(store.getters.username)
    console.log(this.$store.getters.username)
    console.log('try2')
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
