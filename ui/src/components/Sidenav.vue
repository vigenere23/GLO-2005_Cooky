<template>
  <div
    id="sidenav"
    :class="{ closed: drawerClosed }"
  >
    <ul>
      <li class="profile">
        <img
          class="profile-picture"
          src="../../static/default-avatar.png"
        >
        <span class="username">mscupcake352</span>
      </li>
      <li
        v-for="(item, i) in items"
        :key="i"
      >
        <router-link
          v-if="item.type === 'item'"
          :to="item.link"
          tag="a"
          :class="{ current: item.current }"
        >
          <span class="material-icons menu-icon">{{ item.icon }}</span>
          <span class="menu-text">{{ item.text }}</span>
        </router-link>
        <div
          v-else-if="item.type === 'divider'"
          class="divider"
        >
          <span>{{ item.text }}</span>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import { EventBus } from '@/js/eventbus'
import { NavItems } from '@/js/items'
import { mapState } from 'vuex'

export default {
  name: 'SideNav',
  data () {
    return {
      closed: false,
      items: NavItems
    }
  },
  methods: {
    toggleMenu () {
      this.closed = !this.closed
    }
  },
  mounted () {
    EventBus.$on('toggleMenu', this.toggleMenu)
  },
  computed: mapState([ 'drawerClosed' ])
}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

#sidenav {
  height: 100%;
  width: 240px;
  flex-basis: 240px;
  max-width: calc(100% - 32px);
  padding: 8px;
  border-right: solid 1px $divider-color;
  flex-shrink: 0;
  font-size: 14px;
  font-weight: 500;
  color: $secondary-text-color;
  overflow-y: auto;
  display: flex;

  ul {
    padding: 0;
    margin: 0;
    list-style: none;
    flex-shrink: 0;
    flex-basis: 100%;

    li {
      .divider {
        margin: 8px;
        margin-top: 16px;

        span {
          font-size: 12px;
          color: $lighter-secondary-text-color;
          text-transform: uppercase;
        }
      }

      &.profile {
        height: 56px;
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

      a {
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
      }
    }
  }
}

@media screen and (min-width: $desktop-min) {
  #sidenav {
    transition: all 0.2s ease-in-out;

    &.closed {
      width: 0;
      flex-basis: 0;
      padding: 8px 0;
      border-color: transparent;
    }
  }
}

@media screen and (max-width: $tablet-max) {
  #sidenav {
    padding: 8px;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 100;
    background-color: white;
    transition: all 0.3s ease-in-out;
    @include mdElevationElement('nav-drawer');

    &.closed {
      margin-left: -100%;
    }
  }
}
</style>
