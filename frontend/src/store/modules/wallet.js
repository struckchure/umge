import api from '@/store/axiosConfig.js'
import * as utils from '@/store/utils.js'
import * as types from '@/store/types.js'

// endpoints

const FUND_WALLET_URL = '/accounts/wallet/fund/'

// storage

const storage = new utils.Storage()

const state = {}

const getters = {}

const mutations = {}

const actions = {
    // buy single item

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

                context.commit(types.SET_FUND_WALLET_FAILED, error_payload)
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
