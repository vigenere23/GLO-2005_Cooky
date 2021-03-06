<template>
  <div
    class="button"
    :class="{ accent, danger, invert, flat, right, noMargin }"
    :disable="disable"
    @click="emitClick"
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
    danger: {
      type: Boolean,
      default: false
    },
    invert: {
      type: Boolean,
      default: false
    },
    flat: {
      type: Boolean,
      default: false
    },
    disable: {
      type: Boolean,
      default: false
    },
    right: {
      type: Boolean,
      default: false
    },
    noMargin: {
      type: Boolean,
      default: false
    }
  },

  methods: {
    emitClick () {
      if (!this.disable) {
        this.$emit('click')
      }
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
  border-radius: 4px;
  transition: all 0.2s ease-in-out;

  &:not(.noMargin) {
    margin-top: 16px;
  }

  &.right {
    float: right;
  }

  &:not([disable]) {
    cursor: pointer;

    &:hover {
      background-color: darken(white, 3%);
    }

    &:active {
      background-color: darken(white, 5%);
    }

    &.invert {
      color: $primary-color;
    }

    &:not(.accent).flat, &:not(.danger).flat {
      border: $faded-border;
      border-width: 2px;
    }

    &:not(.flat) {
      @include mdElevationElement('raised-button');
    }

    &.danger {
      color: white;
      background-color: #d32c2c;

      &:hover {
        background-color: lighten(#d32c2c, 5%);
      }

      &:active {
        background-color: lighten(#d32c2c, 10%);
      }
    }

    &.accent {
      color: white;
      background-color: $primary-color;

      &:hover {
        background-color: lighten($primary-color, 5%);
      }

      &:active {
        background-color: lighten($primary-color, 10%);
      }
    }
  }

  &[disable] {
    background-color: darken(white, 5%);
    color: $disabled-text-color;
  }

}
</style>
