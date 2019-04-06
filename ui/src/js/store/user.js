export const userModule = {

  namespaced: true,

  state: {
    cart: [],
    userId: '87abdf9nf2903438'
  },

  getters: {
    cartContains: (state) => (id) => {
      return state.cart.indexOf(id) !== -1
    }
  },

  mutations: {
    clear (state) {
      state.userId = null
      state.cart.clear()
    },
    addCartItem (state, id) {
      if (state.cart.indexOf(id) === -1) {
        state.cart.push(id)
      }
    },
    removeCartItem (state, id) {
      const indexToRemove = state.cart.indexOf(id)
      if (indexToRemove !== -1) {
        state.cart.splice(indexToRemove, 1)
      }
    }
  }

}
