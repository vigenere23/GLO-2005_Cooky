<template>
  <div class="cart-item">
    <div class="left">
      <span class="ingredient">
        {{ item.name }}
      </span>
    </div>
    <div class="center">
      <span>{{ item.quantity }}</span>
      <Dropdown
        class="multiplier"
        v-if="quantities"
        :items="quantities"
        :initial-item="item.multiplier"
        @input="emitUpdateItemQuantity"
      />
      <span class="subcost">
        {{ item.subCost }} $
      </span>
    </div>
    <div class="right">
      <span
        class="material-icons remove"
        @click="emitRemoveItem"
      >close</span>
    </div>
  </div>
</template>

<script>
import Dropdown from '@/components/inputs/Dropdown'

export default {

  name: 'CartItem',

  components: {
    Dropdown
  },

  props: {
    item: {
      type: Object,
      required: true
    },
    quantities: {
      type: Array,
      required: true
    }
  },

  methods: {
    emitUpdateItemQuantity (newValue) {
      this.$emit('updateItemQuantity', this.item.id_Ingredient, newValue)
    },
    emitRemoveItem () {
      this.$el.remove()
      this.$emit('removeItem', this.item.id_Ingredient)
    }
  }

}
</script>

<style lang="scss">
.cart-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 16px;

  > * > * {
    margin: 8px;
  }

  .left {
    flex-grow: 1;
  }

  .center {
    display: flex;
    align-items: center;
    flex-shrink: 0;

    > * {
      flex-shrink: 0;
    }

    .multiplier {
      padding: 0;
      flex-basis: 54px;
    }
  }

  .right {
    flex-shrink: 0;
    margin-left: 16px;

    .remove {
      cursor: pointer;
    }
  }
}
</style>
