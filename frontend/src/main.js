import Vue from 'vue'
import App from './App.vue'
import router from "./router/router";
import VueRouter from 'vue-router'
import BootstrapVue from 'bootstrap-vue'
import Vuex from 'vuex'
import store from '../store/store.js';
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-vue/dist/bootstrap-vue.css"

// Install BootstrapVue
Vue.use(BootstrapVue)

Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.use(Vuex)


new Vue({
  render: h => h(App),
  router,
  store
}).$mount('#app')
