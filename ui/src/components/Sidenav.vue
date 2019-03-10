<template>
  <div
    id="sidenav"
    :class="{ opened }"
  >
    <ul>
      <li>
        <router-link
          class="profile"
          to="/users"
          tag="a"
        >
          <img
            class="profile-picture"
            src="../../static/default-avatar.png"
          >
          <span class="username">mscupcake352</span>
        </router-link>
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

export default {
  name: 'SideNav',
  data () {
    return {
      opened: false,
      items: NavItems
    }
  },
  methods: {
    toggleMenu () {
      this.opened = !this.opened
    }
  },
  mounted () {
    EventBus.$on('toggleMenu', this.toggleMenu)
  }
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

  ul {
    padding: 0;
    margin: 0;
    list-style: none;

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

        &.profile {
          height: 56px;

          .profile-picture {
            width: 38px;
            height: 38px;
            border-radius: 50%;
            margin-left: 8px;
            margin-right: 16px;
          }
        }

        .menu-icon {
          margin-left: 8px;
          margin-right: 24px;
        }
      }
    }
  }
}

@media screen and (max-width: 800px) {
  #sidenav {
    padding: 8px;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 100;
    background-color: white;
    @include mdElevationElement('nav-drawer');
  }
}
</style>
