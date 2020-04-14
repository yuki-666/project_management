<template>
  <div>
    <kbs-nav-menu></kbs-nav-menu>
    <router-view />
  </div>
</template>

<script>
import kbsNavMenu from './../common/kbsNavMenu'
export default {
  name: 'Home',
  components: { 'kbs-nav-menu': kbsNavMenu }
}
</script>

<style scoped></style>
