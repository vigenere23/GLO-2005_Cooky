<template>
  <div class="default-layout">
    <DrawerScreen />
    <Header />
    <div class="main">
      <NavDrawer />
      <div class="content">
        <slot />
      </div>
    </div>
  </div>
</template>

<script>
import DrawerScreen from '@/components/DrawerScreen'
import Header from '@/components/Header'
import NavDrawer from '@/components/NavDrawer'
import { LayoutHelper } from '@/js/helpers'

export default {
  name: 'DefaultLayout',
  components: {
    DrawerScreen,
    Header,
    NavDrawer
  },
  methods: {
    handleResize () {
      if (LayoutHelper.isSmallScreen()) {
        this.$store.commit('closeDrawer')
      } else {
        this.$store.commit('openDrawer')
      }
    }
  },
  mounted () {
    window.addEventListener('resize', this.handleResize)
    this.handleResize()
  }
}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.default-layout {
  width: 100%;
  height: 100vh;

  .main {
    height: 100%;
    padding-top: 64px;
    display: flex;

    .content {
      padding: 16px;
    }
  }
}

@media screen and (max-width: $tablet-max) {
  .default-layout {
    .main {
      padding-top: 48px;
    }
  }
}
</style>
