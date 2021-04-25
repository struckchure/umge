import api from '@/store/axiosConfig.js'
import * as utils from '@/store/utils.js'
import * as types from '@/store/types.js'


// endpoints

const PRODUCT_CREATE_URL = '/product/create/'

// storage

const storage = new utils.Storage()

const state = {
    product: {}
}

const getters = {
    get_product (state) {
        return state.product
    }
}

const mutations = {

    // set success response

    [types.CREATE_PRODUCT_SUCCESS] (state, payload) {
        state.product = payload
    },

    // set error response

    [types.CREATE_PRODUCT_FAILED] (state, payload) {
        state.error = payload
    }
}

const actions = {
    // create new store

    async[types.CREATE_PRODUCT] (context, payload) {
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
            url: PRODUCT_CREATE_URL,
            headers: {
                'Content-Type': 'multipart/form-data',
                "X-CSRFToken": csrftoken,
                'Authorization': `Token ${storage.get('token')}`
            },
            data: form_data
        })
        .then(
            function (response) {
                context.commit(types.CREATE_PRODUCT_SUCCESS, response.data)
            }
        )
        .catch(
            function (error) {
                context.commit(types.CREATE_PRODUCT_FAILED, error.response.data)
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
