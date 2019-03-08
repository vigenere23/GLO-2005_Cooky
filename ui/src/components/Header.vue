<template>
  <div id="header">
    <a
      class="material-icons hamburger"
      @click="toggleMenu"
    >menu</a>
  </div>
</template>

<script>
import { EventBus } from '@/eventbus'

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
  width: 100%;
  height: 64px;
  padding: 0 16px;
  display: flex;
  align-items: center;
  @include mdElevationElement('app-bar');

  .hamburger {
    padding: 8px;
  }
}
</style>
