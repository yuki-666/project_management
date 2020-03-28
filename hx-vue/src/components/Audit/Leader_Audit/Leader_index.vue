<template>
  <el-container>
    <el-aside style="width: 200px;margin-top: 20px">
      <side-menu @indexSelect="listByCategory" ref="sideMenu"></side-menu>
    </el-aside>
    <el-main>
      <!-- <manager-r-audit v-show="this.$refs.sideMenu.cid == 0"></manager-r-audit>
      <manager-r-audit v-show="this.$refs.sideMenu.cid == 1"></manager-r-audit> -->
      <leader-r-work-time v-show="this.flag == '0'"></leader-r-work-time>
      <leader-r-work-p-time v-show="this.flag == '1'"></leader-r-work-p-time>
    </el-main>
  </el-container>
</template>

<script>
import SideMenu from './Leader_SideMenu'
import LeaderRWorkTime from './Leader_r_workTime'
import LeaderRWorkPTime from './Leader_r_workPTime'
export default {
  name: 'ManagerIndex',
  components: {
    'side-menu': SideMenu,
    'leader-r-work-time': LeaderRWorkTime,
    'leader-r-work-p-time': LeaderRWorkPTime
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
