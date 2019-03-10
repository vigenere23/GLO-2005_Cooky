<template>
  <div id="header">
    <a
      class="material-icons hamburger"
      @click="toggleMenu"
    >menu</a>
    <span class="project-name">Project</span>
  </div>
</template>

<script>
import { EventBus } from '@/js/eventbus'

export default {
  name: 'Header',
  methods: {
    toggleMenu () {
      EventBus.$emit('toggleMenu')
    }
  }
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
