import Vue from 'vue'
import App from './App.vue'
import router from './js/router'
import store from './js/store'

require('typeface-roboto')
require('typeface-merriweather')

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
