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
        <el-table-column label="项目id" prop="id" sortable></el-table-column>
        <el-table-column
          label="项目名称"
          prop="name"
          sortable
        ></el-table-column>
        <el-table-column
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
          </template>
        </el-table-column>
        <el-table-column
          label="更新时间"
          prop="update_time"
          :sortable="true"
          :sort-method="sortByDate"
        ></el-table-column>
        <el-table-column label="操作">
          <template slot-scope="scope">
            <el-button size="mini" @click="handleEdit(scope.$index, scope.row)"
              >编辑</el-button
            >
            <el-button
              size="mini"
              type="danger"
              @click="handleDelete(scope.$index, scope.row)"
              >删除</el-button
            >
            <el-button size="mini" type="success" @click="handleEdit(scope.$index, scope.row)"
              >编辑</el-button
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
  </div>
</template>

<script>
import SideMenu from './Manager_SideMenu'
import { FlowStatusRules } from '../../home/rule/data-config'
import ZxTag from '../../tag'
export default {
  name: 'ManagerRAudit',
  components: {
    'side-menu': SideMenu,
    'zx-tag': ZxTag
  },
  data () {
    return {
      uid: 0,
      tableDataTmp: [],
      currentPage: 1,
      pagesize: 5,
      total: 10,
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
      FLOWS_STATUS: [
        'pending',
        'established',
        'processing',
        'paid',
        'finished',
        'archived',
        'rejection'
      ],
      projects: [
        {
          id: '',
          name: '',
          status: '',
          update_time: ''
        }
      ]
    }
  },
  methods: {
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
      console.log(value)
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
        .get('/approval/project', {
          params: {
            uid: _this.uid
          }
        })
        .then(successResponse => {
          console.log(successResponse)
          _this.projects = successResponse.data
          _this.tableDataTmp = successResponse.data
        })
        .catch(failResponse => {
          console.log('OMmmmG,my_audit')
        })
    }
  },
  created () {
    console.log('hhhhhhh')
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
