<template>
  <div>
    <div style="color: #222;margin-top: 10px;">所有的项目</div>
    <search-bar @onSearch="searchResult" ref="SearchBar"></search-bar>
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
    <my-index></my-index>
  </div>
</template>
<script>
import MyIndex from './MyIndex'
import { FlowStatusRules } from './rule/data-config'
import SearchBar from './home_component/SearchBar'
import ZxTag from '../tag'
export default {
  components: {
    'search-bar': SearchBar,
    'zx-tag': ZxTag,
    'my-index': MyIndex
  },
  name: 'AppIndex',
  data () {
    return {
      uid: 0,
      tableDataTmp: [],
      currentPage: 1,
      pagesize: 5,
      total: 10,
      FlowStatusRules,
      filter_status: [
        { text: '审批中', value: 1 },
        { text: '已立项', value: 2 },
        { text: '进行中', value: 3 },
        { text: '已交付', value: 4 },
        { text: '已结束', value: 5 },
        { text: '已归档', value: 6 }
      ],
      FLOWS_STATUS: [
        '0',
        '审批中',
        '已立项',
        '进行中',
        '已交付',
        '已结束',
        '已归档'
      ],
      projects: [
        {
          id: '',
          name: '',
          status: '',
          update_time: 'hh'
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
      // // this.handleCurrentChange(currentPage)
      // return row.status === value
    },
    filterTag (value, row) {
      return row.status === value
    },
    handleCurrentChange (currentPage) {
      this.currentPage = currentPage
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
        .get('/homepage/project_all', {
          params: {
            uid: _this.uid
          }
        })
        .then(successResponse => {
          _this.projects = successResponse.data
          _this.tableDataTmp = successResponse.data
        })
        .catch(failResponse => {})
    },
    searchResult () {
      let _this = this
      let projectsTmp = _this.projects
      if (
        _this.$refs.SearchBar.keywords === null ||
        _this.$refs.SearchBar.keywords === '' ||
        _this.$refs.SearchBar.keywords === undefined
      ) {
        this.getAllProjects()
        return
      }
      this.$axios
        .post('/homepage/search', {
          keyword: _this.$refs.SearchBar.keywords
        })
        .then(successResponse => {
          // id为空
          if (successResponse.data.length === 0) {
            this.getAllProjects()
            projectsTmp = _this.projects
            _this.projects = projectsTmp.filter(item => {
              return false
            })
            this.$message.error('没有该项目')
          } else {
            // filter
            this.getAllProjects()
            projectsTmp = _this.projects
            _this.projects = projectsTmp.filter(item =>
              // eslint-disable-next-line eqeqeq
              successResponse.data.some(ele => ele.id == item.id)
            )
          }
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
  margin: 10px 15%;
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
  color: red;
}
.pag {
  margin: 5px 70%;
}
</style>
