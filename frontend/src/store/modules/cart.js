import api from "@/store/axiosConfig.js";
import * as utils from "@/store/utils.js";
import * as types from "@/store/types.js";

// endpoints

const CART_DETAILS_URL = "/cart/details/";
const CART_UPDATE_URL = "/cart/update/";
const BUY_NOW_URL = "/cart/buy-now/";
const CHECKOUT_CART_URL = "/cart/checkout/";

// storage

const storage = new utils.Storage();

const state = {
  cart: {},
  purchase: {},
};

const getters = {
  get_cart(state) {
    return state.cart;
  },
  get_purchase(state) {
    return state.purchase;
  },
};

const mutations = {
  // store list mutation

  [types.SET_CART](state, payload) {
    state.cart = payload;
  },

  // cart purchase success mutation

  [types.SET_CART_PURCHASE_SUCCESS](state, payload) {
    state.purchase = payload;
  },
};

const actions = {
  // get logged in user cart details

  async [types.GET_CART](context) {
    context.commit(types.BUSY_LOADING);

    await api({
      method: "get",
      url: CART_DETAILS_URL,
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${storage.get("token")}`,
      },
    })
      .then(function (response) {
        context.commit(types.SET_CART, response.data);
      })
      .catch(function (error) {
        context.commit(types.SET_ERROR, error.response.data);
      });

    context.commit(types.DONE_LOADING);
  },

  // update logged in user cart

  async [types.UPDATE_CART](context, payload) {
    context.commit(types.BUSY_LOADING);

    // const cart_location = await utils.getLocation();
    // payload.cart_location = cart_location

    const csrftoken = utils.getCookie("csrftoken");

    await api({
      method: "post",
      url: CART_UPDATE_URL,
      data: payload,
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
        Authorization: `Token ${storage.get("token")}`,
      },
    })
      .then(function (response) {
        context.commit(types.SET_CART, response.data);
        context.dispatch(types.GET_CART);
      })
      .catch(function (error) {
        context.commit(types.SET_ERROR, error.response.data);
      });

    context.commit(types.DONE_LOADING);
  },

  // buy single item

  async [types.BUY_NOW](context, payload) {
    context.commit(types.BUSY_LOADING);

    const csrftoken = utils.getCookie("csrftoken");

    // const cart_location = await utils.getLocation();
    // payload.cart_location = {
    //     latitude: cart_location.coords.latitude,
    //     longitude: cart_location.coords.longitude
    // }
    // console.log(payload.cart_location)

    await api({
      method: "post",
      url: BUY_NOW_URL,
      data: payload,
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
        Authorization: `Token ${storage.get("token")}`,
      },
    })
      .then(function (response) {
        context.commit(types.SET_CART_PURCHASE_SUCCESS, response.data);
      })
      .catch(function (error) {
        const error_payload = {
          error: error.response.data.message,
        };

        context.commit(types.SET_ERROR, error_payload);
      });

    context.commit(types.DONE_LOADING);
  },

  // checkout cart

  async [types.CHECKOUT_CART](context, payload) {
    context.commit(types.BUSY_LOADING);

    const csrftoken = utils.getCookie("csrftoken");

    // const cart_location = await utils.getLocation();
    // payload.cart_location = cart_location

    await api({
      method: "post",
      url: CHECKOUT_CART_URL,
      data: payload,
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
        Authorization: `Token ${storage.get("token")}`,
      },
    })
      .then(function (response) {
        context.commit(types.SET_CART_PURCHASE_SUCCESS, response.data);
      })
      .catch(function (error) {
        context.commit(types.SET_ERROR, error.response.data);
      });

    context.commit(types.DONE_LOADING);
  },
};

export default {
  state,
  getters,
  mutations,
  actions,
};
