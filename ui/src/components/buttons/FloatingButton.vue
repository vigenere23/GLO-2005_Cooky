<template>
  <router-link
    :to="link"
    tag="a"
    class="floating-button"
  >
    <span class="material-icons">{{ icon }}</span>
  </router-link>
</template>

<script>
export default {

  name: 'FloatingButton',

  props: {
    icon: {
      type: String,
      default: 'add'
    },
    link: {
      type: String,
      default: ''
    }
  }

}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.floating-button {
  position: fixed;
  bottom: 128px;
  right: 32px;
  border-radius: 50%;
  background-color: $primary-color;
  color: white;
  width: 64px;
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 50;
  @include mdElevationElement('fab');
  transition: all 0.2s ease-in-out;

  &:hover {
    background-color: lighten($primary-color, 5%);
  }

  &:active {
    background-color: lighten($primary-color, 10%);
  }

  span.material-icons {
    font-size: 28px;
  }
}

@media screen and (max-width: $phone-max) {
  .floating-button {
    width: 52px;
    height: 52px;
    bottom: 16px;
    right: 16px;

    span.material-icons {
      font-size: 24px;
    }
  }
}
</style>
