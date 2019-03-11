<template>
  <div class="navigation">
    <div
      class="navigation-category"
      v-for="category in items"
      :key="category.name"
    >
      <div class="divider">
        <span>{{ category.name }}</span>
      </div>
      <router-link
        v-for="section in category.items"
        :key="section.text"
        :to="section.link(userId)"
        tag="a"
        class="navigation-item"
        :class="{ current: section.current }"
        @click.native="closeDrawer"
      >
        <span class="material-icons menu-icon">{{ section.icon }}</span>
        <span class="menu-text">{{ section.text }}</span>
      </router-link>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import { LayoutHelper } from '@/js/helpers'

export default {
  name: 'Navigation',
  props: {
    items: {
      type: Array,
      default: () => []
    }
  },
  computed: mapState([ 'userId' ]),
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

.navigation {

  .divider {
    margin: 8px;
    margin-top: 16px;
    font-size: 12px;
    color: $lighter-secondary-text-color;
    text-transform: uppercase;
  }

  .navigation-item {
    display: flex;
    align-items: center;
    height: 40px;
    margin: 4px 0;
    border-radius: 4px;

    &:hover {
      background-color: $grey100;
    }

    &.current {
      color: $primary-color;
      background-color: rgba($primary-color, 0.2);
      font-weight: 500;
    }

    .menu-icon {
      margin-left: 8px;
      margin-right: 24px;
    }

    > * {
      flex-shrink: 0;
    }
  }
}
</style>
