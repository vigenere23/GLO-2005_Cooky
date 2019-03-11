<template>
  <router-link
    class="nav-item"
    :to="link"
    tag="a"
    :class="{ 'nav-item__current': isCurrent }"
    @click.native="closeDrawer"
  >
    <span
      v-if="icon"
      class="material-icons nav-item__icon"
    >
      {{ icon }}
    </span>
    <span class="nav-item__text">{{ text }}</span>
  </router-link>
</template>

<script>
import { LayoutHelper } from '@/js/helpers'

export default {
  name: 'NavItem',
  props: {
    text: {
      type: String,
      required: true
    },
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
    isCurrent () {
      return this.$route.path === this.link
    }
  },
  methods: {
    closeDrawer () {
      if (LayoutHelper.isSmallScreen()) {
        this.$store.commit('closeDrawer')
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

  &.nav-item__current {
    color: $primary-color;
    background-color: rgba($primary-color, 0.2);
    font-weight: 500;
  }

  .nav-item__icon {
    margin-left: 8px;
    margin-right: 24px;
  }

  > * {
    flex-shrink: 0;
  }
}
</style>
