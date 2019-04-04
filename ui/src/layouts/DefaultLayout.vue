<template>
  <div class="default-layout">
    <DrawerScreen />
    <Header />
    <div class="main">
      <NavDrawer />
      <div
        class="wrapper"
        :class="{ 'drawer-closed': drawerClosed }"
      >
        <div class="content">
          <slot />
        </div>
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
  computed: {
    drawerClosed () {
      return this.$store.state.drawerClosed
    }
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
  background-color: #fafafa;

  .main {
    height: 100%;
    padding-top: $header-height;

    .wrapper {
      width: 100%;
      height: 100%;
      padding-left: $nav-drawer-width;
      transition: padding-left 0.2s ease-in-out;

      &.drawer-closed {
        padding-left: 0;
      }

      .content {
        padding: 32px;
        width: 100%;
        max-width: 1000px;
        margin: auto;
      }
    }
  }
}

@media screen and (max-width: $tablet-max) {
  .default-layout {
    .main {
      padding-top: $header-height-small;

      .wrapper {
        padding-left: 0;

        .content {
          padding: 20px;
        }
      }
    }
  }
}

@media screen and (max-width: $phone-max) {
  .default-layout {
    .main {
      .wrapper {
        .content {
          padding: 16px;
        }
      }
    }
  }
}
</style>
