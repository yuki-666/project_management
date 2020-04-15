<template>
  <div>
    <div class="project_table">
  <el-table :data="tableData" style="width: 100%">
      <el-table-column label="项目ID" prop="project_id"></el-table-column>
      <el-table-column
          label="用户ID"
          prop="uid"
          sortable
        ></el-table-column>
      <el-table-column label="Git权限" prop="git_authority"></el-table-column>
      <el-table-column label="文件权限" prop="file_authority"></el-table-column>
      <el-table-column label="Mail权限" prop="mail_authority"></el-table-column>
      <el-table-column label="操作">
        <el-button type="primary" round @click="newClick2">修改权限</el-button>
      </el-table-column>
    </el-table>
    </div>
    <edit-form
      :show.sync="dialogVisible"
      ref="edit"
    ></edit-form>
  </div>
</template>

<script>
import SideMenu from './ProDetail_SideMenu'
import AuthEdit from './ProDetail_AuthEdit'
export default {
  name: 'ProDetailAuManage',
  components: {
    'side-menu': SideMenu,
    'edit-form': AuthEdit
  },
  data () {
    return {
      //   buttonFlag: false,
      dialogVisible: this.show,
      tableData: [
        {
          uid: '1',
          project_id: '2',
          git_authority: '3',
          file_authority: '4',
          mail_authority: '5'
        }
      ]
    }
  },
  methods: {
    newClick2 () {
      this.dialogVisible = true
    },
    getAllInfo () {
      let _this = this
      this.$axios
        .get('/project_detail/authority_manage', {
          params: {
            uid: _this.uid,
            project_id: _this.project_id,
            git_authority: _this.git_authority,
            file_authority: _this.file_authority,
            mail_authority: _this.mail_authority
          }
        })
        .then(successResponse => {
          _this.$refs.edit.form = successResponse.data
          _this.$refs.edit.form.status = _this.FLOWS_STATUS[successResponse.data.status]
        })
    },
    // 获取全部项目
    getAllProjects () {
      var _this = this
      this.$axios
        .get('/project/mine', {
          params: {
            project_id: _this.project_id
          }
        })
        .then(successResponse => {
          _this.projects = successResponse.data
          _this.tableDataTmp = successResponse.data
        })
        .catch(failResponse => {})
    }
  },
  created () {
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
