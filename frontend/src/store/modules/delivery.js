import api from '@/store/axiosConfig.js'
import * as utils from '@/store/utils.js'
import * as types from '@/store/types.js'

// endpoints

const ORDERS_URL = '/delivery/orders/'

// storage

const storage = new utils.Storage()

const state = {
    orders: {}
}

const getters = {
    get_orders (state) {
        return state.orders
    }
}

const mutations = {

    // orders list mutation

    [types.SET_ORDERS] (state, payload) {
        state.orders = payload
    }
}

const actions = {
    // get orders for user

    async [types.GET_ORDERS] (context) {
        context.commit(types.BUSY_LOADING)

        await api({
            method: 'get',
            url: ORDERS_URL,
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Token ${storage.get('token')}`
            }
        })
        .then(
            function(response) {
                context.commit(types.SET_ORDERS, response.data)
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
