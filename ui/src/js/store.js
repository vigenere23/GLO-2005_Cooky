import Vue from 'vue'
import Vuex from 'vuex'
import { constants } from '@/js/helpers/constants'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    drawerClosed: true,
    screenWith: window.innerWidth,
    userId: '87abdf9nf2903438'
  },
  mutations: {
    openDrawer (state) { state.drawerClosed = false },
    closeDrawer (state) { state.drawerClosed = true },
    toggleDrawer (state) { state.drawerClosed = !state.drawerClosed },
    updateScreenWidth (state, width) { state.screenWith = width }
  },
  getters: {
    isTablet: state => state.screenWith <= constants.tabletWidth,
    isPhone: state => state.screenWith <= constants.phoneWidth
  },
  actions: {

  }
})

export { store }
