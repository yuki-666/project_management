<template>
  <el-container>
    <el-aside style="width: 200px;margin-top: 20px">
      <side-menu @indexSelect="listByCategory" ref="sideMenu"></side-menu>
    </el-aside>
    <el-main>
      <proDetail-info v-if="this.flag == '0'"></proDetail-info>
      <proDetail-function v-else-if="this.flag == '1'"></proDetail-function>
      <proDetail-person v-else-if="this.flag == '2'"></proDetail-person>
      <proDetail-auth v-else-if="this.flag == '3'"></proDetail-auth>
      <proDetail-auManage v-else-if="this.flag == '4'"></proDetail-auManage>
      <proDetail-flaw v-else-if="this.flag == '5'"></proDetail-flaw>
      <proDetail-risk v-else-if="this.flag == '6'"></proDetail-risk>
      <equipment v-else-if="this.flag == '7'"></equipment>
    </el-main>
  </el-container>
</template>

<script>
import SideMenu from './ProDetail_ManagerSideMenu'
import ProDetailINFO from './ProDetail_INFO/ProDetail_Info'
import ProDetailPERSON from './ProDetail_PERSON/ProDetail_Person'
import ProDetailFUNCTION from './ProDetail_FUNCTION/ProDetail_Function'
import ProDetailAUTH from './ProDetail_AUTHORITY/ProDetail_Auth'
import ProDetailAuManage from './ProDetail_AUTHORITY/ProDetail_AuthManage'
import Equipment from './ProDetail_EQUIPMENT/ProDetail_Equipment'
import ProFLAW from './ProDetail_FLAW/ProDetail_Flaw'
import ProRisk from './ProDetail_RISK/ProDetail_Risk'
export default {
  name: 'ProDetailManager',
  components: {
    'side-menu': SideMenu,
    'proDetail-info': ProDetailINFO,
    'proDetail-function': ProDetailFUNCTION,
    'proDetail-person': ProDetailPERSON,
    'proDetail-auth': ProDetailAUTH,
    'proDetail-auManage': ProDetailAuManage,
    'proDetail-flaw': ProFLAW,
    'proDetail-risk': ProRisk,
    'equipment': Equipment
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
      } else if (this.$refs.sideMenu.cid === '4') {
        this.flag = '4'
      } else if (this.$refs.sideMenu.cid === '5') {
        this.flag = '5'
      } else if (this.$refs.sideMenu.cid === '6') {
        this.flag = '6'
      } else {
        this.flag = '7'
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
