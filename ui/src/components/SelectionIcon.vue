<template>
  <a
    class="material-icons selection-icon"
    :class="{ 'selected': isSelected }"
    @mousedown="updateSelection"
  >
    {{ icon }}
  </a>
</template>

<script>
export default {

  name: 'SelectionIcon',

  props: {
    isSelected: {
      type: Boolean,
      required: true
    }
  },

  computed: {
    icon () {
      return this.isSelected
        ? 'add_circle_outline'
        : 'add_circle'
    }
  },

  methods: {
    updateSelection () {
      this.isSelected
        ? this.$emit('deselection')
        : this.$emit('selection')
    }
  }

}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.selection-icon {
  display: block;
  transition: transform 0.2s ease-in-out;

  &.selected {
    transform: rotate(45deg);
  }
}
</style>
