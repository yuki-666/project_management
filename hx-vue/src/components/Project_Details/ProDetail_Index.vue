<template>
  <el-container>
    <el-aside style="width: 200px;margin-top: 20px">
      <side-menu @indexSelect="listByCategory" ref="sideMenu"></side-menu>
    </el-aside>
    <el-main>
      <proDetail-info v-show="this.flag == '0'"></proDetail-info>
      <proDetail-function v-show="this.flag == '1'"></proDetail-function>
      <proDetail-person v-show="this.flag == '2'"></proDetail-person>
      <proDetail-auth v-show="this.flag == '3'"></proDetail-auth>
      <proDetail-auManage v-show="this.flag == '4'"></proDetail-auManage>
    </el-main>
  </el-container>
</template>

<script>
import SideMenu from './ProDetail_SideMenu'
import ProDetailINFO from './ProDetail_Info'
import ProDetailPERSON from './ProDetail_Person'
import ProDetailFUNCTION from './ProDetail_Function'
import ProDetailAUTH from './ProDetail_Auth'
import ProDetailAuManage from './ProDetail_AuthManage'
export default {
  name: 'ProDetail',
  components: {
    'side-menu': SideMenu,
    'proDetail-info': ProDetailINFO,
    'proDetail-function': ProDetailFUNCTION,
    'proDetail-person': ProDetailPERSON,
    'proDetail-auth': ProDetailAUTH,
    'proDetail-auManage': ProDetailAuManage
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
      } else if (this.$refs.sideMenu.cid === '1') {
        this.flag = '1'
      } else if (this.$refs.sideMenu.cid === '2') {
        this.flag = '2'
      } else if (this.$refs.sideMenu.cid === '3') {
        this.flag = '3'
      } else {
        this.flag = '4'
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
