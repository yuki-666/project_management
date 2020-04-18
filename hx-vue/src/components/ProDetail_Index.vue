<template>
  <div>
    <manager-index v-if="this.flag == 1" ref="managerIndex"></manager-index>
    <worker-index v-else-if="this.flag == 3" ref="workerIndex"></worker-index>
  </div>
</template>

<script>
import ProDetailWorker from './Project_Details_Worker/ProDetail_WorkerIndex'
import ProDetailManager from './Project_Details/ProDetail_ManagerIndex'
export default {
  name: 'ProDetail',
  components: {
    'manager-index': ProDetailManager,
    'worker-index': ProDetailWorker
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
