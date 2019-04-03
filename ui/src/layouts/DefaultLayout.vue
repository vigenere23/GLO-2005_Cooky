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
import DrawerScreen from '@/components/nav/DrawerScreen'
import Header from '@/components/nav/Header'
import NavDrawer from '@/components/nav/NavDrawer'

export default {
  name: 'DefaultLayout',
  components: {
    DrawerScreen,
    Header,
    NavDrawer
  },
  methods: {
    handleResize () {
      this.$store.commit('updateScreenWidth', window.innerWidth)

      if (this.$store.getters.isTablet) {
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
      width: 100%;
      overflow-y: auto;
      background-color: #fafafa;
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
