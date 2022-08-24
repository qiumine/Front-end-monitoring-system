<template>
  <div class="dashboard-container">
    <div class="dashboard-text">队伍: {{ name }}</div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Dashboard',
  computed: {
    ...mapGetters([
      'name'
    ])
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
    margin: 30px;
    display: flex;
    justify-content: center;
  }
  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}
</style>
