import Vuex from 'vuex'
import Vue from 'vue'

import common from '@/store/modules/common.js'
import accounts from '@/store/modules/accounts.js'
import stores from '@/store/modules/stores.js'
import cart from '@/store/modules/cart.js'
import products from '@/store/modules/products.js'
import delivery from '@/store/modules/delivery.js'
import wallet from '@/store/modules/wallet.js'

Vue.use(Vuex)

const store = new Vuex.Store(
	{
		modules: {
			common,
			accounts,
			stores,
			cart,
			products,
			delivery,
			wallet
		}
	}
)

export default store
