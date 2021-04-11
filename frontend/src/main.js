import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import '@/assets/css/all.css'
import '@/assets/css/modal.css'
import '@/assets/css/layouts.css'
import '@/assets/css/grid.css'
import '@/assets/css/custom-ui.css'
import '@/assets/css/style.css'

import "@/components/components.js"
import titleMixin from "@/titleMixin.js"

Vue.mixin(titleMixin)
Vue.config.productionTip = false

new Vue(
	{
		router,
		store,
		render: h => h(App)
	}
).$mount('#app')
