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
      <el-table-column label="员工姓名" prop="name"></el-table-column>
      <el-table-column label="Git权限" prop="git_authority"></el-table-column>
      <el-table-column label="文件权限" prop="file_authority"></el-table-column>
      <el-table-column label="Mail权限" prop="mail_authority"></el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button size="mini" type="primary" round @click="newClick2(scope.$index, scope.row)" >修改权限</el-button>
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
      :show.sync="dialogVisible"
      @updateAgain="this.getAllInfo"
      ref="edit"
    ></edit-form>
  </div>
</template>

<script>
import SideMenu from '../ProDetail_ManagerSideMenu'
import AuthEdit from './ProDetail_AuthEdit'
export default {
  name: 'ProDetailAuManage',
  components: {
    'side-menu': SideMenu,
    'edit-form': AuthEdit
  },
  data () {
    return {
      dialogVisible: this.show,
      tableData: [
        {
          worker_id: '',
          name: '',
          git_authority: '',
          file_authority: '',
          mail_authority: ''
        }
      ]
    }
  },
  methods: {
    handleCurrentChange (currentPage) {
      this.currentPage = currentPage
    },
    newClick2 (index, row) {
      this.$refs.edit.form = {
        worker_id: row.worker_id,
        git_authority: row.git_authority,
        file_authority: row.file_authority,
        mail_authority: row.mail_authority
      }
      this.dialogVisible = true
    },
    getAllInfo () {
      let _this = this
      this.$axios
        .get('/project_detail/authority_manage', {
          params: {
            project_id: _this.projectid
          }
        })
        .then(successResponse => {
          _this.tableData = successResponse.data
        })
    }
  },
  created () {
    this.projectid = this.$store.getters.projectid
    this.getAllInfo()
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
  color: red;
}
.pag {
  margin: 5px 70%;
}
</style>
