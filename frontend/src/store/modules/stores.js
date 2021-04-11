import api from '@/store/axiosConfig.js'
// import * as utils from '@/store/utils.js'
import * as types from '@/store/types.js'


// endpoints

const STORE_LIST_URL = '/store/list/'
const PRODUCT_LIST_URL = '/product/list/'

const state = {
    error: null,
    stores: [],
    products: []
}

const getters = {
    get_stores (state) {
        return state.stores
    },
    get_products (state) {
        return state.products
    }
}

const mutations = {
    // store list mutation

    [types.SET_STORE_LIST] (state, payload) {
        state.stores = payload
    },

    // product list mutation

    [types.SET_PRODUCT_LIST] (state, payload) {
        state.products = payload
    },

    // set error response

    [types.SET_ERROR] (state, payload) {
        state.error = payload
    }
}

const actions = {
    // get list of all stores
    // action to send request to API

    async [types.GET_STORE_LIST] (context) {
        await api({
            method: 'get',
            url: STORE_LIST_URL
        })
        .then(
            function(response) {
                context.commit(types.SET_STORE_LIST, response.data)
            }
        )
        .catch(
            function(error) {
                context.commit(types.SET_ERROR, error)
            }
        )
    },

    // get list of all products
    // action to send request to API

    async [types.GET_PRODUCT_LIST] (context, {store_name, product_name}) {
        await api({
            method: 'get',
            url: `${PRODUCT_LIST_URL}${store_name}/${product_name}`
        })
        .then(
            function(response) {
                context.commit(types.SET_PRODUCT_LIST, response.data)
            }
        )
        .catch(
            function(error) {
                context.commit(types.SET_ERROR, error)
            }
        )
    }
}

export default {
    state,
    getters,
    mutations,
    actions
}
