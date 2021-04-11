import api from '@/store/axiosConfig.js'
import * as utils from '@/store/utils.js'
import * as types from '@/store/types.js'


// endpoints

const LOGIN_URL = '/account/login/'
const REGISTER_URL = 'account/register/'

const storage = new utils.Storage()

const state = {
    error: null,
    user: {},
}

const getters = {
    get_error (state) {
        return state.error
    },
    get_user (state) {
        return state.user
    },
    is_authenticated () {
        if (storage.get('token')) {
            return true
        } else {
            return false
        }
    }
}

const mutations = {
    [types.AUTH_SUCCESS] (state, payload) {
        state.user = payload.user
        storage.set('token', payload.token)
    },
    [types.AUTH_FAILED] (state, payload) {
        storage.remove('token')
        state.error = payload.response
    }
}

const actions = {

    // login action to send request to API

    async [types.AUTH_LOGIN] (context, payload) {
        const csrftoken = utils.getCookie('csrftoken');

        await api({
            method: 'post',
            url: LOGIN_URL,
            data: payload,
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken
            }
        })
        .then(
            function(response) {
                context.commit(types.AUTH_SUCCESS, response.data)
            }
        )
        .catch(
            function(error) {
                context.commit(types.AUTH_FAILED, error)
            }
        )
    },

    // register action to send request to API

    async [types.AUTH_REGISTER] (context, payload) {
        const csrftoken = utils.getCookie('csrftoken');

        await api({
            method: 'post',
            url: REGISTER_URL,
            data: payload,
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken
            }
        })
        .then(
            function(response) {
                context.commit(types.AUTH_SUCCESS, response.data)
            }
        )
        .catch(
            function(error) {
                context.commit(types.AUTH_FAILED, error)
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
