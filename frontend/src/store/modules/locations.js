import * as types from '@/store/types.js'
import api from '@/store/axiosConfig.js'
import * as utils from '@/store/utils.js'


const storage = new utils.Storage();

const LOCATIONS_URL = '/locations/'

const state = {
    locations: []
}

const getters = {
    get_locations (state) {
        return state.locations
    }
}

const mutations = {
    [types.SET_ADMIN_DELIVERY_LOCATIONS] (state, payload) {
        state.locations = payload
    }
}

const actions = {
    async [types.GET_ADMIN_DELIVERY_LOCATIONS] (context) {
        context.commit(types.BUSY_LOADING)

        await api({
            method: 'get',
            url: LOCATIONS_URL,
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Token ${storage.get('token')}`
            }
        })
        .then(
            function (response) {
                context.commit(types.SET_ADMIN_DELIVERY_LOCATIONS, response.data)
            }
        )
        .catch(
            function (error) {
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
