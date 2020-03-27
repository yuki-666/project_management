<template>
  <div>
    xxh
    <boss-index v-show="this.flag == 0" ref="bossIndex"></boss-index>
    <manager-index v-show="this.flag == 1" ref="managerIndex"></manager-index>
    <!-- <leader-index v-show="this.flag == 2" ref="leaderIndex"></leader-index> -->
    <worker-index v-show="this.flag == 3" ref="workerIndex"></worker-index>
  </div>
</template>

<script>
import store from '../../store'
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
    console.log(store.getters.uid)
    console.log(this.$store.getters.uid)
    console.log('hhhhh' + this.$store.getters.career)
    if (this.$store.getters.career === 0) {
      console.log('onde')
      this.flag = 0
    } else if (this.$store.getters.career === 1) {
      this.flag = 1
    } else if (this.$store.getters.career === 2) {
      this.flag = 2
    } else if (this.$store.getters.career === 3) {
      this.flag = 3
    }
    console.log('try')
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
