<template>
    <el-menu
      :default-active="'/back/accounter'"
      router
      mode="horizontal"
      background-color="white"
      text-color="#222"
      active-text-color="red"
      style="min-width: 1300px">
      <el-menu-item v-for="(item,i) in navList" :key="i" :index="item.name">
        {{ item.navItem }}
      </el-menu-item>
    </el-menu>
</template>

<script>
export default {
  name: 'BackHome',
  data () {
    return {
      navList: [
        {name: '/back/accounter', navItem: '管理员账号'},
        {name: '/back/worker', navItem: '员工信息'}
      ]
    }
  }
}
</script>

<style scoped>
  a{
    text-decoration: none;
  }

  span {
    pointer-events: none;
  }
</style>
