import api from '@/store/axiosConfig.js'
import * as utils from '@/store/utils.js'
import * as types from '@/store/types.js'


// endpoints

const STORE_URL = '/store/'
const STORE_CREATE_URL = '/store/create/'
const STORE_LIST_URL = '/store/list/'
const STORE_ORDERS_URL = '/store/orders/'
const PRODUCT_LIST_URL = '/product/list/'

// storage

const storage = new utils.Storage()

const state = {
    store: {},
    store_products: [],
    store_orders: [],
    all_stores: [],
    products: []
}

const getters = {
    get_store (state) {
        return state.store
    },
    get_store_products (state) {
        return state.store_products
    },
    get_stores (state) {
        return state.all_stores
    },
    get_products (state) {
        return state.products
    },
    get_store_orders(state) {
        return state.store_orders
    }
}

const mutations = {
    // store details mutation

    [types.SET_STORE] (state, payload) {
        state.store = payload
    },

    // store products mutation

    [types.SET_STORE_PRODUCTS] (state, payload) {
        state.store_products = payload
    },

    // store list mutation

    [types.SET_STORE_LIST] (state, payload) {
        state.all_stores = payload
    },

    // product list mutation

    [types.SET_PRODUCT_LIST] (state, payload) {
        state.products = payload
    },

    // store orders mutation

    [types.SET_STORE_ORDERS] (state, payload) {
        state.store_orders = payload
    }
}

const actions = {
    // create new store

    async [types.CREATE_STORE] (context, payload) {
        context.commit(types.BUSY_LOADING)

        const csrftoken = utils.getCookie('csrftoken');

        var form_data = new FormData()

        var keys = Object.keys(payload)

        for (var i = 0; i < keys.length; i++) {
            var key = keys[i]
            var value = payload[key]
            form_data.append(key, value)
        }

        await api({
            method: 'post',
            url: STORE_CREATE_URL,
            headers: {
                'Content-Type': 'multipart/form-data',
                "X-CSRFToken": csrftoken,
                'Authorization': `Token ${storage.get('token')}`
            },
            data: form_data
        })
        .then(
            function (response) {
                context.commit(types.SET_STORE, response.data)
            }
        )
        .catch(
            function (error) {
                context.commit(types.SET_ERROR, error.response.data)
            }
        )

        context.commit(types.DONE_LOADING)
    },

    // get store details

    async [types.GET_STORE] (context, store_slug) {
        context.commit(types.BUSY_LOADING)

        await api({
            method: 'get',
            url: `${STORE_URL}${store_slug}/details/`
        })
        .then(
            function (response) {
                context.commit(types.SET_STORE, response.data)
            }
        )
        .catch(
            function (error) {
                context.commit(types.SET_ERROR, error.response.data)
            }
        )

        context.commit(types.DONE_LOADING)
    },

    // get store prodcuts

    async [types.GET_STORE_PRODUCTS] (context, store_slug) {
        context.commit(types.BUSY_LOADING)

        await api({
            method: 'get',
            url: `${STORE_URL}${store_slug}/products/`
        })
        .then(
            function (response) {
                context.commit(types.SET_STORE_PRODUCTS, response.data)
            }
        )
        .catch(
            function (error) {
                context.commit(types.SET_ERROR, error.response.data)
            }
        )

        context.commit(types.DONE_LOADING)
    },

    // get list of all stores
    // action to send request to API

    async [types.GET_STORE_LIST] (context) {
        context.commit(types.BUSY_LOADING)

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
                context.commit(types.SET_ERROR, error.response.data)
            }
        )

        context.commit(types.DONE_LOADING)
    },

    // get list of all products
    // action to send request to API

    async [types.GET_PRODUCT_LIST] (context, {store_name, product_name}) {
        context.commit(types.BUSY_LOADING)

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
                context.commit(types.SET_ERROR, error.response.data)
            }
        )

        context.commit(types.DONE_LOADING)
    },

    // get all stores + orders

    async [types.GET_STORE_ORDERS] (context) {
        context.commit(types.BUSY_LOADING)

        await api({
            method: 'get',
            url: STORE_ORDERS_URL,
            headers: {
                'Authorization': `Token ${storage.get('token')}`
            }
        })
        .then(
            function(response) {
                context.commit(types.SET_STORE_ORDERS, response.data)
            }
        )
        .catch(
            function(error) {
                context.commit(types.SET_ERROR, error.response.data)
            }
        )

        context.commit(types.DONE_LOADING)
    }
}

export default {
    state,
    getters,
    mutations,
    actions
}
