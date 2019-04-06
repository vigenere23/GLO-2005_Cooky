import Vue from 'vue'
import App from './App.vue'
import { router } from './js/router'
import { store } from './js/store/index'

require('typeface-roboto')
require('typeface-noto-serif')
require('@fortawesome/fontawesome-free/css/all.css')

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
