import api from '@/store/axiosConfig.js'
// import * as utils from '@/store/utils.js'
import * as types from '@/store/types.js'


// endpoints

const CART_UPDATE_URL = '/cart/update/'

const state = {
    error: null,
    cart: []
}

const getters = {
    get_cart (state) {
        return state.cart
    }
}

const mutations = {
    // store list mutation

    [types.SET_CART] (state, payload) {
        state.stores = payload
    },

    // set response error

    [types.SET_ERROR] (state, payload) {
        state.error = payload
    }
}

const actions = {
    // get logged in user cart

    async [types.GET_CART] (context, payload) {
        await api({
            method: 'post',
            url: CART_UPDATE_URL,
            payload: payload
        })
        .then(
            function(response) {
                context.commit(types.SET_CART, response.data)
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
