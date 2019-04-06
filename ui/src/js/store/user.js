export const userModule = {

  namespaced: true,

  state: {
    cart: [],
    userId: '87abdf9nf2903438',
    avatar: ''
  },

  getters: {
    cartContains: (state) => (id) => {
      return state.cart.indexOf(id) !== -1
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
