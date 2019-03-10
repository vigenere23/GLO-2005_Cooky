<template>
  <div id="default-layout">
    <Header />
    <div id="main">
      <Sidenav />
      <div id="content">
        <slot />
      </div>
    </div>
  </div>
</template>

<script>
import Header from '@/components/Header'
import Sidenav from '@/components/Sidenav'

export default {
  name: 'DefaultLayout',
  components: {
    Header,
    Sidenav
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
