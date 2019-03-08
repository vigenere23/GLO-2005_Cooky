<template>
  <div id="sidenav" />
</template>

<script>
import { EventBus } from '@/eventbus'

export default {
  name: 'SideNav',
  data () {
    return {
      menuOpened: false
    }
  },
  methods: {
    toggleMenu () {
      this.menuOpened = !this.menuOpened
    }
  },
  mounted () {
    EventBus.$on('toggleMenu', this.toggleMenu)
  }
}
</script>

<style lang="scss">

</style>
