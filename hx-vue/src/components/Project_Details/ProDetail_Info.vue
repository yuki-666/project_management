<template>
  <div>项目信息</div>
</template>

<script>
import SideMenu from './ProDetail_SideMenu'
export default {
  name: 'ProDetailINFO',
  components: {
    'side-menu': SideMenu
  },
  methods: {
    listByCategory () {
      // var _this = this
      // var cid = this.$refs.sideMenu.cid
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
