<template>
  <div>
    xxh
    <boss-index v-show="this.flag == 0" ref="bossIndex"></boss-index>
    <manager-index v-show="this.flag == 1" ref="managerIndex"></manager-index>
  </div>
</template>

<script>
import store from '../../store'
import ManagerIndex from './Manager_Audit/Manager_index'
import BossIndex from './Boss_Audit/Boss_index'
export default {
  name: 'MyAuidt',
  components: {
    'manager-index': ManagerIndex,
    'boss-index': BossIndex
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
