<template>
  <div>
    <div class="project_table">
  <el-table :data="tableData" style="width: 100%">
    <el-table-column label="Git权限" prop="git_authority"></el-table-column>
    <el-table-column label="文件权限" prop="file_authority"></el-table-column>
    <el-table-column label="Mail权限" prop="mail_authority"></el-table-column>
    </el-table>
    </div>
  </div>
</template>

<script>
// import { FlowStatusRules } from "./rule/data-config";
import SideMenu from './ProDetail_SideMenu'
export default {
  name: 'ProDetailAUTH',
  components: {
    'side-menu': SideMenu
    //    'edit-form': PDEdit
  },
  data () {
    return {
      //   buttonFlag: false,
      //   dialogFormVisible: this.show,
      tableData: [
        {
          git_authority: '',
          file_authority: '',
          mail_authority: ''
        }
      ]
    }
  },
  methods: {
    // newClick () {
    //   this.dialogFormVisible = true
    // },
    // handleEdit (index, row) {
    //   console.log(index, row)
    // },
    getAllInfo () {
      let _this = this
      this.$axios
        .get('/project_detail/authority', {
          params: {
            uid: '0012',
            project_id: '2020-0000-D-01'
          }
        })
        .then(successResponse => {
          _this.tableData = successResponse.data
        })
    }
  },
  created () {
    this.getAllInfo()
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
