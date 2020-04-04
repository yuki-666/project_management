<template>
  <el-container>
    <el-aside style="width: 200px;margin-top: 20px">
      <side-menu @indexSelect="listByCategory" ref="sideMenu"></side-menu>
    </el-aside>
    <el-main>
        hello,worker
      <worker-r-audit v-if="this.flag == '0'"></worker-r-audit>
    </el-main>
  </el-container>
</template>

<script>
import SideMenu from './Worker_SideMenu'
import WorkerRAudit from './Worker_r_workPTime'
export default {
  name: 'WorkerIndex',
  components: {
    'side-menu': SideMenu,
    'worker-r-audit': WorkerRAudit
  },
  data () {
    return {
      flag: 0
    }
  },
  methods: {
    listByCategory () {
      this.flag = '0'
      // eslint-disable-next-line eqeqeq
      if (this.$refs.sideMenu.cid == '0') {
        this.flag = '0'
      } else {
        this.flag = '1'
      }
    }
  }
}
</script>

<style scoped>
.books-area {
  width: 990px;
  margin-left: auto;
  margin-right: auto;
}
</style>
