<template>
  <el-container>
    <el-aside style="width: 200px;margin-top: 20px">
      <side-menu @indexSelect="listByCategory" ref="sideMenu"></side-menu>
    </el-aside>
    <el-main>
        hello,Boss
      <boss-r-audit v-if="this.flag == '0'"></boss-r-audit>
    </el-main>
  </el-container>
</template>

<script>
import SideMenu from './Boss_SideMenu'
import BossRAudit from './Boss_r_audit'
export default {
  name: 'BossIndex',
  components: {
    'side-menu': SideMenu,
    'boss-r-audit': BossRAudit
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
