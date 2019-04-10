<template>
  <div
    id="drawer-screen"
    @mousedown="closeDrawer"
    :class="{ show }"
  />
</template>

<script>
import { mapState, mapMutations, mapGetters } from 'vuex'

export default {

  name: 'DrawerScreen',

  methods: mapMutations('layout', ['closeDrawer']),

  computed: {
    ...mapState('layout', ['drawerClosed']),
    ...mapGetters('layout', ['isTablet']),
    show () {
      return !this.drawerClosed && this.isTablet
    }
  }

}
</script>

<style lang="scss">
#drawer-screen {
  width: 100%;
  height: 100%;
  position: fixed;
  z-index: 90;
  visibility: hidden;
  transition: background-color 0.3s ease-in-out, visibility 0s linear 0.3s;

  &.show {
    visibility: visible;
    background-color: rgba(0, 0, 0, 0.3);
    transition: background-color 0.3s ease-in-out, visibility 0s linear;
  }
}
</style>
