<template>
  <div>
    xxh
    <manager-index ref="managerIndex"></manager-index>
  </div>
</template>

<script>
import ManagerIndex from './Manager_Audit/Manager_index'
export default {
  name: 'MyAuidt',
  components: {
    'manager-index': ManagerIndex
  },
  data () {
    return {
      flag: 0
    }
  },
  methods: {},
  created () {
    this.flag = 0
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
