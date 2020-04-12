<template>
  <el-container>
    <el-aside style="width: 200px;margin-top: 20px">
      <side-menu @indexSelect="listByCategory" ref="sideMenu"></side-menu>
    </el-aside>
    <el-main>
      <my-project v-if="this.flag == '0'"></my-project>
      <manager-new v-else-if="this.flag == '1'"></manager-new>
    </el-main>
  </el-container>
</template>

<script>
import SideMenu from './manager_SideMenu'
import MyProject from './my_project'
export default {
  name: 'ManagerIndex',
  components: {
    'side-menu': SideMenu,
    'my-project': MyProject
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
