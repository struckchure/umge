import api from '@/store/axiosConfig.js'
import * as utils from '@/store/utils.js'
import * as types from '@/store/types.js'

// endpoints

const FUND_WALLET_URL = '/account/wallet/fund/'

// storage

const storage = new utils.Storage()

const state = {
    fund: {}
}

const getters = {
    get_fund(state) {
        return state.fund
    }
}

const mutations = {
    // fund success mutation

    [types.SET_FUND_WALLET_SUCCESS] (state, payload) {
        state.fund = payload
    },

    // fund failed mutation

    // [types.SET_FUND_WALLET_FAILED] (state, payload) {}
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
    }
}

export default {
    state,
    getters,
    mutations,
    actions
}
