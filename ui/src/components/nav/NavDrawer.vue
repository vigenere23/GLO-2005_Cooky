<template>
  <div
    id="navigation-drawer"
    :class="{ closed: drawerClosed }"
  >
    <Nav :items="navItems" />
  </div>
</template>

<script>
import { navItems } from '@/data/navItems'
import Nav from '@/components/nav/Nav'
import { mapState } from 'vuex'

export default {
  name: 'NavigationDrawer',
  components: {
    Nav
  },
  data () {
    return {
      navItems: navItems
    }
  },
  computed: {
    ...mapState('layout', ['drawerClosed']),
    isCurrent () {
      return this.$route.path === this.link
    }
  }
}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

#navigation-drawer {
  position: fixed;
  height: 100%;
  width: $nav-drawer-width;
  max-width: calc(100% - 32px);
  padding: 8px;
  border-right: solid 1px $divider-color;
  font-size: 14px;
  font-weight: 500;
  color: $secondary-text-color;
  background-color: white;
  overflow-y: auto;
  overflow-x: hidden;
  display: flex;
  flex-direction: column;
  z-index: 40;
}

@media screen and (min-width: $desktop-min) {
  #navigation-drawer {
    transition: all 0.2s ease-in-out;

    &.closed {
      width: 0;
      flex-basis: 0;
      padding: 8px 0;
      border-color: transparent;
    }
  }
}

@media screen and (max-width: $tablet-max) {
  #navigation-drawer {
    padding: 8px;
    top: 0;
    left: 0;
    z-index: 100;
    transition: all 0.3s ease-in-out;
    @include mdElevationElement('nav-drawer');

    &.closed {
      margin-left: -100%;
    }
  }
}
</style>
