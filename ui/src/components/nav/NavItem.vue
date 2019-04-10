<template>
  <router-link
    class="nav-item"
    :to="link"
    :class="{ 'nav-item_current': isCurrent }"
    @click.native="tryCloseDrawer"
  >
    <span
      v-if="icon"
      class="material-icons nav-item_icon"
    >
      {{ icon }}
    </span>
    <slot class="nav-item_text" />
  </router-link>
</template>

<script>
import { mapMutations, mapGetters } from 'vuex'

export default {
  name: 'NavItem',
  props: {
    icon: {
      type: String,
      default: ''
    },
    link: {
      type: String,
      default: '/'
    }
  },
  computed: {
    ...mapGetters('layout', ['isTablet']),
    isCurrent () {
      return this.$route.path === this.link
    }
  },
  methods: {
    ...mapMutations('layout', ['closeDrawer']),
    tryCloseDrawer () {
      if (this.isTablet) {
        this.closeDrawer()
      }
    }
  }
}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.nav-item {
  display: flex;
  align-items: center;
  height: 40px;
  margin: 4px 0;
  border-radius: 4px;

  &:hover {
    background-color: $grey100;
  }

  &:active {
    background-color: $grey200;
  }

  &.nav-item_current {
    color: $primary-color;
    background-color: rgba($primary-color, 0.1);
    font-weight: 500;

    &:active {
      background-color: rgba($primary-color, 0.2);
    }
  }

  .nav-item_icon {
    margin-left: 8px;
    margin-right: 24px;
  }

  > * {
    flex-shrink: 0;
  }
}
</style>
