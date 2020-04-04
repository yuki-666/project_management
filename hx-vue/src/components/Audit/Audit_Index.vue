<template>
  <div>
    xxh
    <boss-index v-if="this.flag == 0" ref="bossIndex"></boss-index>
    <manager-index v-else-if="this.flag == 1" ref="managerIndex"></manager-index>
    <leader-index v-else-if="this.flag == 2" ref="leaderIndex"></leader-index>
    <worker-index v-else-if="this.flag == 3" ref="workerIndex"></worker-index>
  </div>
</template>

<script>
// import store from '../../store'
import ManagerIndex from './Manager_Audit/Manager_index'
import BossIndex from './Boss_Audit/Boss_index'
import LeaderIndex from './Leader_Audit/Leader_index'
import WorkerIndex from './Worker_Audit/Worker_index'
export default {
  name: 'MyAuidt',
  components: {
    'manager-index': ManagerIndex,
    'boss-index': BossIndex,
    'leader-index': LeaderIndex,
    'worker-index': WorkerIndex
  },
  data () {
    return {
      flag: -1
    }
  },
  methods: {},
  created () {
    // eslint-disable-next-line eqeqeq
    if (this.$store.getters.career == 0) {
      this.flag = 0
    // eslint-disable-next-line eqeqeq
    } else if (this.$store.getters.career == 1) {
      this.flag = 1
    // eslint-disable-next-line eqeqeq
    } else if (this.$store.getters.career == 2) {
      this.flag = 2
    // eslint-disable-next-line eqeqeq
    } else if (this.$store.getters.career == 3) {
      this.flag = 3
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
