<template>
  <el-container>
    <el-aside style="width: 200px;margin-top: 20px">
      <side-menu @indexSelect="listByCategory" ref="sideMenu"></side-menu>
    </el-aside>
    <el-main>
        hello,worker
      <!-- <manager-r-audit v-show="this.$refs.sideMenu.cid == 0"></manager-r-audit>
      <manager-r-audit v-show="this.$refs.sideMenu.cid == 1"></manager-r-audit> -->
      <worker-r-audit v-show="this.flag == '0'"></worker-r-audit>
      <!-- <manager-r-work-time v-show="this.flag == '1'"></manager-r-work-time> -->
    </el-main>
  </el-container>
</template>

<script>
import SideMenu from './Worker_SideMenu'
import WorkerRAudit from './Worker_r_workPTime'
// import ManagerRWorkTime from './Manager_r_workTime'
export default {
  name: 'ManagerIndex',
  components: {
    'side-menu': SideMenu,
    'worker-r-audit': WorkerRAudit
    // 'manager-r-work-time': ManagerRWorkTime
  },
  data () {
    return {
      flag: 0
    }
  },
  methods: {
    listByCategory () {
      console.log('hhhh')
      console.log(this.$refs.sideMenu.cid)
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
