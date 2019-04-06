<template>
  <a
    class="material-icons selection-icon"
    :class="{ 'selected': isSelected }"
    @click="updateSelection"
  >
    {{ icon }}
  </a>
</template>

<script>
export default {

  name: 'SelectionIcon',

  props: {
    selected: {
      type: Object,
      required: true
    },
    deselected: {
      type: Object,
      required: true
    },
    initiallySelected: {
      type: Function,
      required: true
    },
    payload: {
      type: Object,
      required: true
    }
  },

  data () {
    return {
      isSelected: this.initiallySelected(this.payload)
    }
  },

  computed: {
    icon () {
      return this.isSelected
        ? this.selected.icon
        : this.deselected.icon
    }
  },

  methods: {
    updateSelection () {
      if (this.isSelected && this.deselected.action(this.payload)) {
        this.isSelected = false
      } else if (!this.isSelected && this.selected.action(this.payload)) {
        this.isSelected = true
      }
    }
  }

}
</script>

<style lang="scss">
.selection-icon {
  transform: all 2s ease-in-out;

  &.selected {
    transform: rotate(90deg);
  }
}
</style>
