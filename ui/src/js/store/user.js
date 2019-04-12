import { API } from '@/js/api/api'

export const userModule = {

  namespaced: true,

  state: {
    cartItems: null,
    cartId: null,
    userId: '1',
    avatar: ''
  },

  getters: {
    cartContains: (state) => (id) => {
      return state.cartItems.indexOf(id) !== -1
    },
    avatar: (state) => (user) => {
      if (user) {
        return user.avatar || `${process.env.BASE_URL}images/default-avatar.png`
      }
      return state.avatar || `${process.env.BASE_URL}images/default-avatar.png`
    }
  },

  mutations: {
    clear (state) {
      state.userId = null
      state.cartId = null
      state.cartItems = null
      state.avatar = null
    },
    set (state, cartItems) {
      state.cartItems = []
      for (const cartItem of cartItems) {
        state.cartItems.push(cartItem.id_Ingredient)
      }
    }
  },

  actions: {
    async loadCart (context, force) {
      if (force || !context.state.cartId) {
        const cart = await API.getUserCart(context.state.userId)
        if (cart && !cart.error) {
          context.state.cartId = cart.id
        }
      }
      if (context.state.cartId) {
        const cartItems = await API.getCartItems(context.state.cartId)
        if (cartItems && !cartItems.error) {
          context.commit('set', cartItems)
        }
      }
    },
    async addCartItem (context, ingredientId) {
      if (context.state.cartId) {
        await API.addCartItem(context.state.cartId, ingredientId)
        context.dispatch('loadCart')
      }
    },
    async removeCartItem (context, ingredientId) {
      if (context.state.cartId) {
        await API.removeCartItem(context.state.cartId, ingredientId)
        context.dispatch('loadCart')
      }
    }
  }

}
