<template>
  <el-container>
    <el-aside style="width: 200px;margin-top: 20px">
      <side-menu @indexSelect="listByCategory" ref="sideMenu"></side-menu>
    </el-aside>
    <el-main>
      <leader-r-work-time v-if="this.flag == '0'"></leader-r-work-time>
      <leader-r-work-p-time v-else-if="this.flag == '1'"></leader-r-work-p-time>
    </el-main>
  </el-container>
</template>

<script>
import SideMenu from './Leader_SideMenu'
import LeaderRWorkTime from './Leader_r_workTime'
import LeaderRWorkPTime from './Leader_r_workPTime'
export default {
  name: 'LeaderIndex',
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
