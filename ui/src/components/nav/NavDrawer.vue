<template>
  <div
    id="navigation-drawer"
    :class="{ closed: drawerClosed }"
  >
    <div class="profile">
      <img
        class="profile-picture"
        src="../../../static/default-avatar.png"
      >
      <span class="username">mscupcake352</span>
    </div>
    <Nav :items="items" />
  </div>
</template>

<script>
import { NavItems } from '@/js/items'
import { mapState } from 'vuex'
import Nav from '@/components/nav/Nav'

export default {
  name: 'NavigationDrawer',
  components: {
    Nav
  },
  data () {
    return {
      items: NavItems
    }
  },
  computed: mapState([ 'drawerClosed', 'userId' ])
}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

#navigation-drawer {
  height: 100%;
  width: 240px;
  flex-basis: 240px;
  max-width: calc(100% - 32px);
  padding: 8px;
  border-right: solid 1px $divider-color;
  flex-shrink: 0;
  font-size: 14px;
  font-weight: 500;
  color: $secondary-text-color;
  overflow-y: auto;
  overflow-x: hidden;
  display: flex;
  flex-direction: column;

  .profile {
    height: 56px;
    flex-shrink: 0;
    display: flex;
    align-items: center;

    .profile-picture {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      margin-left: 8px;
      margin-right: 16px;
    }
  }
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
    position: fixed;
    top: 0;
    left: 0;
    z-index: 100;
    background-color: white;
    transition: all 0.3s ease-in-out;
    @include mdElevationElement('nav-drawer');

    &.closed {
      margin-left: -100%;
    }
  }
}
</style>
