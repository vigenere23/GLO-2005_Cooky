import { constants } from '@/js/helpers/constants'

export const layoutModule = {

  namespaced: true,

  state: {
    drawerClosed: true,
    screenWith: window.innerWidth
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

}
