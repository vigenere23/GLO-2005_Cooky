<template>
  <div class="default-layout">
    <Toaster />
    <DrawerScreen />
    <Header />
    <div class="main">
      <NavDrawer v-if="userId" />
      <div
        class="wrapper"
        :class="{ 'drawer-closed': !userId || drawerClosed }"
      >
        <div class="content">
          <slot />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Toaster from '@/components/toaster/Toaster'
import DrawerScreen from '@/components/nav/DrawerScreen'
import Header from '@/components/nav/Header'
import NavDrawer from '@/components/nav/NavDrawer'
import { mapState, mapMutations, mapGetters } from 'vuex'

export default {

  name: 'DefaultLayout',

  components: {
    Toaster,
    DrawerScreen,
    Header,
    NavDrawer
  },

  computed: {
    ...mapState('layout', ['drawerClosed']),
    ...mapState('user', ['userId']),
    ...mapGetters('layout', ['isTablet'])
  },

  methods: {
    ...mapMutations('layout', [
      'updateScreenWidth',
      'closeDrawer',
      'openDrawer'
    ]),
    handleResize () {
      this.updateScreenWidth(window.innerWidth)

      if (this.isTablet) {
        this.closeDrawer()
      } else {
        this.openDrawer()
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
  min-height: 100vh;
  background-color: #fafafa;

  .main {
    min-height: 100%;
    padding-top: $header-height;

    .wrapper {
      width: 100%;
      min-height: 100%;
      padding-left: $nav-drawer-width;
      transition: padding-left 0.2s ease-in-out;

      &.drawer-closed {
        padding-left: 0;
      }

      .content {
        padding: 32px;
        min-height: 100%;
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
