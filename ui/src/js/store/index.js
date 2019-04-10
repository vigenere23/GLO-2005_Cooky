import Vue from 'vue'
import Vuex from 'vuex'
import { layoutModule } from './layout'
import { userModule } from './user'

Vue.use(Vuex)

export const store = new Vuex.Store({
  modules: {
    user: userModule,
    layout: layoutModule
  }
})
