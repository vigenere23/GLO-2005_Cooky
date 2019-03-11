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
      <NavItem
        v-for="section in category.items"
        :key="section.text"
        :text="section.text"
        :icon="section.icon"
        :link="section.link(userId)"
      />
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import NavItem from '@/components/NavItem'

export default {
  name: 'Navigation',
  components: {
    NavItem
  },
  props: {
    items: {
      type: Array,
      default: () => []
    }
  },
  computed: mapState([ 'userId' ])
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
}
</style>
