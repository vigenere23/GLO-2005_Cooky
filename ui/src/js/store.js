import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    drawerClosed: true
  },
  mutations: {
    openDrawer () { this.drawerClosed = false },
    closeDrawer () { this.drawerClosed = true },
    toggleDrawer () { this.drawerClosed = !this.drawerClosed }
  },
  actions: {

  }
})
