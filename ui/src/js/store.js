import Vue from 'vue'
import Vuex from 'vuex'
import { constants } from '@/js/constants'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    drawerClosed: true
  },
  mutations: {
    openDrawer (state) { state.drawerClosed = false },
    closeDrawer (state) { state.drawerClosed = true },
    toggleDrawer (state) { state.drawerClosed = !state.drawerClosed }
  },
  actions: {

  },
  getters: {
    isSmallScreen: state => window => window.innerWidth <= constants.tabletWidth
  }
})
