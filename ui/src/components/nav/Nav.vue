<template>
  <div class="navigation">
    <NavItem
      class="profile"
      :link="`/users/${userId}`"
    >
      <img
        class="profile-picture"
        :src="avatar()"
      >
      <span class="username">mscupcake352</span>
    </NavItem>
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
        :icon="section.icon"
        :link="section.link"
      >
        {{ section.text }}
      </NavItem>
    </div>
  </div>
</template>

<script>
import NavItem from '@/components/nav/NavItem'
import { mapState, mapGetters } from 'vuex'

export default {

  name: 'Nav',

  components: {
    NavItem
  },

  props: {
    items: {
      type: Array,
      default: () => []
    }
  },

  computed: {
    ...mapState('user', ['userId']),
    ...mapGetters('user', ['avatar'])
  }

}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.navigation {

  .profile {
    height: 56px;
    flex-shrink: 0;
    display: flex;
    align-items: center;

    .profile-picture {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      margin-left: 8px;
      margin-right: 16px;
    }
  }

  .divider {
    margin: 8px;
    margin-top: 16px;
    font-size: 12px;
    color: $lighter-secondary-text-color;
    text-transform: uppercase;
  }
}
</style>
