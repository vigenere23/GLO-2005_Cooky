<template>
  <div id="default-layout">
    <DrawerScreen />
    <Header />
    <div id="main">
      <NavigationDrawer />
      <div id="content">
        <slot />
      </div>
    </div>
  </div>
</template>

<script>
import DrawerScreen from '@/components/DrawerScreen'
import Header from '@/components/Header'
import NavigationDrawer from '@/components/NavigationDrawer'

export default {
  name: 'DefaultLayout',
  components: {
    DrawerScreen,
    Header,
    NavigationDrawer
  },
  methods: {
    handleResize () {
      if (this.$store.getters.isSmallScreen(window)) {
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

#default-layout {
  width: 100%;
  height: 100vh;

  #main {
    height: 100%;
    padding-top: 64px;
    display: flex;

    #content {
      padding: 16px;
    }
  }
}

@media screen and (max-width: $tablet-max) {
  #default-layout {
    #main {
      padding-top: 48px;
    }
  }
}
</style>
