<template>
  <div class="cart-page">
    <h1>Cart</h1>
    <div
      v-if="cartItems"
      class="cart-items"
    >
      <div
        v-for="item in cartItems"
        :key="item.id"
        class="cart-item"
      >
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
            @input="(newValue) => updateQuantity(item.id_Ingredient, newValue)"
          />
          <span class="subcost">
            {{ item.subCost }} $
          </span>
        </div>
        <div class="right">
          <span
            class="material-icons remove"
            @click="removeItem(item.id_Ingredient)"
          >close</span>
        </div>
      </div>
      <div class="totalcost">
        Total : {{ cart.totalCost }} $
      </div>
      <Button
        accent
        right
        @click="command"
      >
        Command
      </Button>
    </div>
    <NoContent v-else />
  </div>
</template>

<script>
import Dropdown from '@/components/inputs/Dropdown'
import Button from '@/components/buttons/Button'
import NoContent from '@/components/NoContent'
import { mapState, mapActions } from 'vuex'
import { API } from '@/js/api/api'

export default {

  name: 'Cart',

  components: {
    Dropdown,
    Button,
    NoContent
  },

  computed: mapState('user', ['cart', 'cartItems']),

  data () {
    return {
      quantities: null
    }
  },

  mounted () {
    this.quantities = this.getQuantities()
  },

  methods: {
    getQuantities () {
      const quantities = []
      for (let i = 1; i < 100; i++) {
        quantities.push(i)
      }
      return quantities
    },
    command () {
      return true
    },
    async updateQuantity (ingredientId, newValue) {
      await API.modifyCartItemQuantity(this.cart.id, ingredientId, newValue)
      this.loadCart(true)
    },
    async removeItem (ingredientId) {
      await API.removeCartItem(this.cart.id, ingredientId)
      this.loadCart(true)
    },
    ...mapActions('user', ['loadCart'])
  }

}
</script>

<style lang="scss">
.cart-page {
  .cart-items {
    width: 100%;
    max-width: 500px;
    margin: auto;

    .cart-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 16px;

      > * > * {
        margin: 8px;
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
        flex-basis: 32px;

        .remove {
          cursor: pointer;
        }
      }

    }

    .totalcost {
      font-size: 24px;
      text-align: right;
      margin: 16px;
    }
  }
}
</style>
