<template>
  <div>
    <manager-index v-if="this.flag == 1" ref="managerIndex"></manager-index>
     <no-manager-index v-else ref="NoManagerIndex"></no-manager-index>
  </div>
</template>

<script>
// import store from '../../store'
import NoManagerIndex from './NoManager/NoManager_index'
import ManagerIndex from './Manager/manager_index'
export default {
  name: 'ProjectManagement',
  components: {
    'manager-index': ManagerIndex,
    'no-manager-index': NoManagerIndex
  },
  data () {
    return {
      flag: -1
    }
  },
  methods: {},
  created () {
    // eslint-disable-next-line eqeqeq
    if (this.$store.getters.career == 1) {
      this.flag = 1
    // eslint-disable-next-line eqeqeq
    } else {
      this.flag = 2
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
