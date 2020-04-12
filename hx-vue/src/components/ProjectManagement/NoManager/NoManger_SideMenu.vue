<template>
  <el-menu
    class="categories"
    default-active="0"
    @select="handleSelect"
    active-text-color="red"
  >
    <el-menu-item index="0">
      <i class="el-icon-menu"></i>
      <span slot="title">我参与的项目</span>
    </el-menu-item>
  </el-menu>
</template>

<script>
export default {
  name: 'SideMenu',
  data () {
    return {
      cid: ''
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      this.cid = key
      this.$emit('indexSelect')
    }
  }
}
</script>

<style scoped>
.categories {
  position: fixed;
  margin-left: 20px;
  top: 100px;
  width: 150px
  /* left: -600px;
  top: 100px;
  width: 150px; */
}
</style>
