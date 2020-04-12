<template>
  <el-container>
    <el-aside style="width: 200px;margin-top: 20px">
      <side-menu @indexSelect="listByCategory" ref="sideMenu"></side-menu>
    </el-aside>
    <el-main>
      <!-- <manager-r-audit v-show="this.$refs.sideMenu.cid == 0"></manager-r-audit>
      <manager-r-audit v-show="this.$refs.sideMenu.cid == 1"></manager-r-audit> -->
      <proDetail-info v-show="this.flag == '0'"></proDetail-info>
      <proDetail-person v-show="this.flag == '1'"></proDetail-person>
      <proDetail-function v-show="this.flag == '2'"></proDetail-function>
      <proDetail-auth v-show="this.flag == '3'"></proDetail-auth>
    </el-main>
  </el-container>
</template>

<script>
import SideMenu from './ProDetail_SideMenu'
import ProDetailINFO from './ProDetail_Info'
import ProDetailPERSON from './ProDetail_Person'
import ProDetailFUNCTION from './ProDetail_Function'
import ProDetailAUTH from './ProDetail_Auth'
export default {
  name: 'ProDetail',
  components: {
    'side-menu': SideMenu,
    'proDetail-info': ProDetailINFO,
    'proDetail-person': ProDetailPERSON,
    'proDetail-function': ProDetailFUNCTION,
    'proDetail-auth': ProDetailAUTH
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
      // if(this.$refs.sideMenu.cid==0){

      // }
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
