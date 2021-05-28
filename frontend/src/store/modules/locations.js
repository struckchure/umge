import * as types from '@/store/types.js'
import api from '@/store/axiosConfig.js'
import * as utils from '@/store/utils.js'


const storage = new utils.Storage();

const LOCATIONS_URL = '/locations/'
const LOCATIONS_CREATE_URL = '/locations/create/'
const REGIONS_URL = '/locations/regions/'
const REGIONS_CREATE_URL = '/locations/regions/create/'
const USER_LOCATION_UPDATE_URL = '/locations/update-pickup-location/'

const state = {
    locations: [],
    regions: [],
    location: {},
    region: {}
}

const getters = {
    get_locations (state) {
        return state.locations
    },

    get_regions (state) {
        return state.regions
    },

    get_location (state) {
        return state.location
    },

    get_region (state) {
        return state.region
    }
}

const mutations = {
    [types.SET_ADMIN_DELIVERY_LOCATIONS] (state, payload) {
        state.locations = payload
    },

    [types.SET_ADMIN_DELIVERY_REGIONS] (state, payload) {
        state.regions = payload
    },

    [types.SET_REGION_SUCCESS] (state, payload) {
        state.region = payload
    },

    [types.SET_LOCATION_SUCCESS] (state, payload) {
        state.location = payload
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
    },

    async [types.GET_ADMIN_DELIVERY_REGIONS] (context) {
        context.commit(types.BUSY_LOADING)

        await api({
            method: 'get',
            url: REGIONS_URL,
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Token ${storage.get('token')}`
            }
        })
        .then(
            function (response) {
                context.commit(types.SET_ADMIN_DELIVERY_REGIONS, response.data)
            }
        )
        .catch(
            function (error) {
                context.commit(types.SET_ERROR, error.data)
            }
        )

        context.commit(types.DONE_LOADING)
    },

    async [types.CREATE_ADMIN_DELIVERY_LOCATION] (context, payload) {
        context.commit(types.BUSY_LOADING)

        const csrftoken = utils.getCookie('csrftoken');

        await api({
            method: 'post',
            url: LOCATIONS_CREATE_URL,
            data: payload,
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken,
                "Authorization": `Token ${storage.get('token')}`
            }
        })
        .then(
            function (response) {
                context.commit(types.SET_LOCATION_SUCCESS, response.data)
            }
        )
        .catch(
            function (error) {
                context.commit(types.SET_ERROR, error.data)
            }
        )

        context.commit(types.DONE_LOADING)
    },

    async [types.CREATE_ADMIN_DELIVERY_REGION] (context, payload) {
        context.commit(types.BUSY_LOADING)

        const csrftoken = utils.getCookie('csrftoken');

        await api({
            method: 'post',
            url: REGIONS_CREATE_URL,
            data: payload,
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken,
                "Authorization": `Token ${storage.get('token')}`
            }
        })
        .then(
            function (response) {
                context.commit(types.SET_REGION_SUCCESS, response.data)
            }
        )
        .catch(
            function (error) {
                context.commit(types.SET_ERROR, error.data)
            }
        )

        context.commit(types.DONE_LOADING)
    },

    async [types.USER_LOCATION_UPDATE] (context, payload) {
        context.commit(types.BUSY_LOADING)

        const csrftoken = utils.getCookie('csrftoken');

        await api({
            method: 'post',
            url: USER_LOCATION_UPDATE_URL,
            data: payload,
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken,
                "Authorization": `Token ${storage.get('token')}`
            }
        })
        .then(
            function (response) {
                const success_message = {
                    'success': 'Location update was successfull !!!'
                }

                context.commit(types.SET_ERROR, success_message)
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
