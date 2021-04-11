import Vuex from 'vuex'
import Vue from 'vue'

import accounts from '@/store/modules/accounts.js'
import stores from '@/store/modules/stores.js'
Vue.use(Vuex)

const store = new Vuex.Store(
	{
		modules: {
			accounts,
			stores
		} 
	}
)

export default store
