<template>
  <div>
    <el-dialog
      title="上传文件"
      :visible.sync="dialogFormVisible"
      @close="$emit('update:show', false)"
      center
    >
      <el-upload
        :action="'https://jsonplaceholder.typicode.com/posts/'"
        :http-request="modeUpload"
        :limit="1"
>
        <el-button slot="trigger" type="primary">选取文件</el-button>
        <a href="http://127.0.0.1:7777/api/back/export_normal_account_sample" rel="external nofollow" download="模板">
          <el-button type="success">下载模板</el-button>
        </a>
        <div slot="tip" class="el-upload__tip">只能上传excel文件</div>
      </el-upload>
      <span slot="footer" class="dialog-footer">
        <el-button @click="closeDialog">取 消</el-button>
        <el-button type="primary" @click="submitUpload()">确定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'FileEdit',
  props: {
    show: {
      type: Boolean,
      default: false
    }
  },
  data () {
    return {
      dialogFormVisible: this.show,
      fileList: []
    }
  },
  watch: {
    show () {
      this.dialogFormVisible = this.show
    }
  },
  methods: {
    modeUpload: function (item) {
    // console.log(item.file);
      this.mode = item.file
    },
    submitUpload () {
      let fd = new FormData()
      let _this = this
      fd.append('file', this.mode)
      this.$axios
        .post('/back/import_normal_account', fd, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }).then(resp => {
          if (resp.data.status_code === 0) {
            this.dialogFormVisible = false
            this.$emit('update:show', false)
            this.$emit('updateAgain')
            _this.dialogFormVisible = false
            this.$message.success('上传成功')
          }
          if (resp.data.status_code === 1) {
            this.$message.error('请上传.xlsx文件')
          }
        })
    },
    closeDialog () {
      this.dialogFormVisible = false
    }
  }
}
</script>

<style scoped>
.el-icon-circle-plus-outline {
  margin: 50px 0 0 20px;
  font-size: 100px;
  float: left;
  cursor: pointer;
}
</style>
