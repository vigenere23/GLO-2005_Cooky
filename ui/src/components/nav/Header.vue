<template>
  <div id="header">
    <a
      class="material-icons hamburger"
      @mousedown="toggleDrawer"
    >menu</a>
    <router-link
      class="project-name"
      to="/"
      tag="a"
    >
      <span>Cooky <i class="fas fa-cookie-bite">&nbsp;</i></span>
    </router-link>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'

export default {

  name: 'Header',

  methods: mapMutations('layout', ['toggleDrawer'])

}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

#header {
  height: 64px;
  width: 100%;
  padding: 0 16px;
  position: fixed;
  top: 0;
  display: flex;
  align-items: center;
  background-color: $primary-color;
  color: white;
  z-index: 50;
  @include mdElevationElement('app-bar');

  .hamburger {
    padding: 8px;
  }

  .project-name {
    font-size: 20px;
    font-weight: 500;
    margin-left: 16px;
  }
}

@media screen and (max-width: $tablet-max) {
  #header {
    height: 48px;
    padding: 0 8px;
  }
}
</style>
