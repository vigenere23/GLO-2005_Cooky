<template>
  <div
    class="dropdown"
    :class="{ disabled }"
  >
    <span class="label">
      {{ label }}
    </span>
    <div
      class="selected-item"
      @click="toggle"
    >
      <span>{{ itemText(selectedItem) }}</span>
    </div>
    <div
      class="dropdown-items"
      v-if="opened"
    >
      <div
        class="dropdown-item"
        v-for="(item, i) in items"
        :key="item.id || i"
        @click="selectItem(item)"
      >
        <span>{{ itemText(item) }}</span>
      </div>
    </div>
  </div>
</template>

<script>
export default {

  name: 'Dropdown',

  props: {
    textAttribute: {
      type: String,
      default: 'text'
    },
    items: {
      type: Array,
      required: true
    },
    disabled: {
      type: Boolean,
      default: false
    },
    label: {
      type: String,
      default: ' '
    },
    initialItem: {
      type: [Object, String, Number],
      default: null
    }
  },

  data () {
    return {
      selectedItem: this.initialItem,
      opened: false
    }
  },

  watch: {
    'disabled': 'close',
    'items': 'ensureValid'
  },

  methods: {
    selectItem (item) {
      this.selectedItem = item
      this.$emit('input', this.selectedItem)
      this.close()
    },
    close () {
      this.opened = false
    },
    toggle () {
      if (!this.disabled) {
        this.opened = !this.opened
      }
    },
    itemText (item) {
      return item !== null
        ? item[this.textAttribute] !== undefined
          ? item[this.textAttribute]
          : item
        : ''
    },
    ensureValid () {
      if (this.items.indexOf(this.selectedItem) === -1) {
        this.selectedItem = null
      }
    }
  },

  mounted () {
    if (this.initialItem && this.selectedItem) {
      setTimeout(() => {
        this.$emit('input', this.selectedItem)
      }, Math.random() * 6000)
    }
  }

}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.dropdown {
  width: 100%;
  position: relative;
  padding-top: 20px;

  .label {
    display: block;
    position: absolute;
    top: 0;
    z-index: 10;
  }

  &.disabled {
    .selected-item {
      background-color: darken(white, 5%);
      cursor: initial;
    }

    .label {
      color: $disabled-text-color;
    }
  }
}

.dropdown-items {
  width: 100%;
  border-radius: 4px;
  height: auto;
  max-height: 200px;
  overflow-x: hidden;
  overflow-y: auto;
  position: absolute;
  top: 100%;
  z-index: 20;
  background-color: white;
  @include mdElevation(4);
}

.dropdown-item, .selected-item {
  padding: 16px;
  cursor: pointer;

  &:hover {
    background-color: darken(white, 3%);
  }

  &:active {
    background-color: darken(white, 5%);
  }
}

.selected-item {
  display: block;
  width: 100%;
  height: 56px;
  font-family: 'Roboto';
  font-size: 16px;
  line-height: 1.2em;
  min-height: 2px;
  border-radius: 4px;
  border: $faded-border;
  border-width: 2px;
  background-color: white;
}
</style>
