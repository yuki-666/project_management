<template>
  <div>
    <div style="color: #222;margin-top: 10px;">所有的项目</div>
    <search-bar @onSearch="searchResult" ref="SearchBar"></search-bar>
    <div class="project_table">
      <el-table
        :data="
          tableDataTest.slice(
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
         <!-- <el-table-column
          label="项目状态"
          prop="status"
          column-key="status"
          :filters="filter_status"
          :filter-method="filterTag"
          filter-placement="bottom-end"
        >
          <template slot-scope="props">
            <xm-tag :type="FlowStatusRules[props.row.status]">
              {{ FLOWS_STATUS[props.row.status] }}
            </xm-tag>
          </template>
        </el-table-column> -->
        <el-table-column
          label="项目状态"
          prop="status"
          column-key="status"
          :filters="filter_status"
          :filter-method="filterTag"
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
          :total="tableDataTest.length"
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
import XmTag from '../tag'
export default {
  components: {
    'search-bar': SearchBar,
    'xm-tag': XmTag,
    'my-index': MyIndex
  },
  name: 'AppIndex',
  data () {
    return {
      currentPage: 1,
      pagesize: 2,
      FlowStatusRules,
      filter_status: [
        { text: '进行中', value: 1 },
        { text: '已启用', value: 0 },
        { text: '已删除', value: 3 }
      ],
      FLOWS_STATUS: ['已启用', '进行中', '已失效', '已删除'],
      projects: [
        {
          id: '',
          name: '',
          status: '',
          update_time: ''
        }
      ],
      tableDataTest: [
        {
          id: '1',
          name: 'biu',
          status: 0,
          update_time: '2016-05-04'
        },
        {
          id: '2',
          name: 'bau',
          status: 1,
          update_time: '2016-05-02'
        },
        {
          id: '3',
          name: 'biu2',
          status: 3,
          update_time: '2017-05-02'
        }
      ]
    }
  },
  methods: {
    filterTagTable (filters) {
      console.log(filters.status)
      if (filters.status) {
        this.tableDataTest.status = filters.status
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
        console.log(-1)
        return -1
      } else {
        return 1
      }
    },
    searchResult () {
      var _this = this
      this.$axios
        .get('/search?keywords=' + this.$refs.searchBar.keywords, {})
        .then(resp => {
          if (resp && resp.status === 200) {
            _this.projects = resp.data
          }
        })
    }
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
