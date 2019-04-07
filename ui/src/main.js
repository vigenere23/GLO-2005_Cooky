import Vue from 'vue'
import Vuetify from 'vuetify'
import App from './App.vue'
import { router } from './js/router'
import { store } from './js/store/index'

require('typeface-roboto')
require('typeface-noto-serif')
require('@fortawesome/fontawesome-free/css/all.css')

Vue.config.productionTip = false
Vue.use(Vuetify)

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
