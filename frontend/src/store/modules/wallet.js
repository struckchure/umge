import api from '@/store/axiosConfig.js'
import * as utils from '@/store/utils.js'
import * as types from '@/store/types.js'

// endpoints

const FUND_WALLET_URL = '/account/wallet/fund/'
const FUND_WALLET_HISTORY_URL = '/account/wallet/history/'
const VERIFY_FUND_URL = '/account/wallet/fund/verify/'

// storage

const storage = new utils.Storage()

const state = {
    fund: {},
    fund_history: []
}

const getters = {
    get_fund(state) {
        return state.fund
    },

    get_fund_history(state) {
        return state.fund_history
    }
}

const mutations = {
    // fund success mutation

    [types.SET_FUND_WALLET_SUCCESS] (state, payload) {
        state.fund = payload
    },

    // fund history mutation

    [types.SET_FUND_WALLET_HISTORY] (state, payload) {
        state.fund_history = payload
    }
}

const actions = {
    // fund user wallet

    async [types.FUND_WALLET] (context, payload) {
        context.commit(types.BUSY_LOADING)

        const csrftoken = utils.getCookie('csrftoken');

        await api({
            method: 'post',
            url: FUND_WALLET_URL,
            data: payload,
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken,
                "Authorization": `Token ${storage.get('token')}`
            }
        })
        .then(
            function(response) {
                context.commit(types.SET_FUND_WALLET_SUCCESS, response.data)
            }
        )
        .catch(
            function(error) {
                const error_payload = {
                    'error': error.response.data.message
                }

                context.commit(types.SET_ERROR, error_payload)
            }
        )

        context.commit(types.DONE_LOADING)
    },

    // fund wallet history

    async [types.GET_WALLET_FUND_HISTORY] (context) {
        context.commit(types.BUSY_LOADING)

        await api({
            method: 'get',
            url: FUND_WALLET_HISTORY_URL,
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Token ${storage.get('token')}`
            }
        })
        .then(
            function(response) {
                context.commit(types.SET_FUND_WALLET_HISTORY, response.data)
            }
        )
        .catch(
            function(error) {
                const error_payload = {
                    error
                }

                context.commit(types.SET_ERROR, error_payload)
            }
        )

        context.commit(types.DONE_LOADING)
    },

    // verify last payment

    async [types.VERIFY_FUND] (context) {
        context.commit(types.BUSY_LOADING)

        await api({
            method: 'get',
            url: VERIFY_FUND_URL,
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Token ${storage.get('token')}`
            }
        })
        .then(
            function(response) {
                context.commit(types.SET_SUCCESS, response.data)
            }
        )
        .catch(
            function(error) {
                context.commit(types.SET_ERROR, error.data)
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
