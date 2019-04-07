<template>
  <div
    class="button"
    :class="{ accent: accent, invert: invert }"
    @click="$emit('click')"
  >
    <slot>Submit</slot>
  </div>
</template>

<script>
export default {

  name: 'Button',

  props: {
    accent: {
      type: Boolean,
      default: false
    },
    invert: {
      type: Boolean,
      default: false
    }
  }

}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.button {
  padding: 12px 16px;
  margin: 4px;
  width: max-content;
  font-size: 16px;
  font-weight: 500;
  background-color: white;
  border: $faded-border;
  border-radius: 4px;
  cursor: pointer;
  @include mdElevationElement('raised-button');
  transition: all 0.2s ease-in-out;

  &:hover {
    background-color: $grey100;
  }

  &:active {
    background-color: $grey200;
  }

  &.invert {
    color: $primary-color;
  }

  &.accent {
    background-color: $primary-color;
    color: white;

    &:hover {
      background-color: rgba($primary-color, 0.9);
    }

    &:active {
      background-color: rgba($primary-color, 0.8);
    }
  }
}
</style>
