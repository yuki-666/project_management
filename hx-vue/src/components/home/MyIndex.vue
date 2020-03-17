<template>
  <div>
    <div style="color: #222;margin-top: 10px;">我的项目</div>
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
            <xm-tag :type="FlowStatusRules[props.row.status]">
              {{ FLOWS_STATUS[props.row.status] }}
            </xm-tag>
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
  </div>
</template>
<script>
import { FlowStatusRules } from './rule/data-config'
import SearchBar from './home_component/SearchBar'
import XmTag from '../tag'
export default {
  components: {
    'search-bar': SearchBar,
    'xm-tag': XmTag
  },
  name: 'AppIndex',
  data () {
    return {
      tableDataTmp: [],
      currentPage: 1,
      pagesize: 5,
      total: 10,
      uid: 0,
      FlowStatusRules,
      filter_status: [
        { text: 'pending', value: 1 },
        { text: 'established', value: 2 },
        { text: 'processing', value: 3 },
        { text: 'paid', value: 4 },
        { text: 'finished', value: 5 },
        { text: 'archived', value: 6 }
      ],
      FLOWS_STATUS: [
        'pending',
        'established',
        'processing',
        'paid',
        'finished',
        'archived'
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
      console.log(value)
      // this.filterTagTable()
      // return row.status === value
      return row.status === value
    },
    handleCurrentChange (currentPage) {
      this.currentPage = currentPage
      console.log(this.currentPage)
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
        .get('/homepage/project_mine', {
          params: {
            uid: _this.uid
          }
        })
        .then(successResponse => {
          _this.projects = successResponse.data
          _this.tableDataTmp = successResponse.data
        })
        .catch(failResponse => {
          console.log('OMmmmG')
        })
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

      console.log(_this.projects)
      console.log('after')
      this.$axios
        .post('/homepage/project_mine', {
          keyword: _this.$refs.SearchBar.keywords
        })
        .then(successResponse => {
          console.log(successResponse.data)
          // id为空
          if (successResponse.data.length === 0) {
            _this.projects.filter(item => {
              return false
            })
            this.$message.error('没有该项目')
          }
          // filter
          _this.projects = projectsTmp.filter(item =>
            // eslint-disable-next-line eqeqeq
            successResponse.data.some(ele => ele.id == item.id)
          )
        })
    }
  },
  created () {
    this.uid = this.$route.query.uid
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
