<template>
  <div class="cart-page">
    <h1>Cart</h1>
    <div
      v-if="cartItems && cartItems.length"
      class="cart-items"
    >
      <CartItem
        v-for="item in cartItems"
        :key="item.id"
        :item="item"
        :quantities="quantities"
        @removeItem="removeItem"
        @updateItemQuantity="updateItemQuantity"
      />
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
import Button from '@/components/buttons/Button'
import NoContent from '@/components/NoContent'
import CartItem from '@/components/cart/CartItem'
import { mapState, mapActions } from 'vuex'
import { API } from '@/js/api/api'

export default {

  name: 'Cart',

  components: {
    Button,
    NoContent,
    CartItem
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
    async updateItemQuantity (ingredientId, newValue) {
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

    .totalcost {
      font-size: 24px;
      text-align: right;
      margin: 16px;
    }
  }
}
</style>
