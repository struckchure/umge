import api from "@/store/axiosConfig.js";
import * as utils from "@/store/utils.js";
import * as types from "@/store/types.js";
import store from "@/store/index.js";

// endpoints

const LOGOUT_URL = "/account/logout/";
const LOGIN_URL = "/account/login/";
const REGISTER_URL = "account/register/";
const USER_UPDATE_URL = "/account/update/";
const ADMIN_USERS_LIST_URL = "/account/admin/users/";
const ADMIN_RIDERS_LIST_URL = "/account/admin/riders/";
const PAYMENT_VERIFICATION_URL = "/payment/vefify/";

const storage = new utils.Storage();

const state = {
  user: {},
  payment: {},
  admin_users_list: [],
  admin_riders_list: [],
};

const getters = {
  get_user(state) {
    return state.user;
  },
  get_admin_users_list(state) {
    return state.admin_users_list;
  },
  get_admin_riders_list(state) {
    return state.admin_riders_list;
  },
  is_authenticated(state) {
    if (storage.get("token")) {
      return true;
    } else {
      state.user = {};
      return false;
    }
  },
  is_admin(state) {
    if (storage.get("token") && state.user.username) {
      if (state.user.is_superuser === true) {
        return true;
      } else {
        return false;
      }
    } else {
      return false;
    }
  },
  is_staff(state) {
    if (storage.get("token") && state.user.username) {
      if (state.user.is_staff === true) {
        return true;
      } else {
        return false;
      }
    } else {
      return false;
    }
  },
};

const mutations = {
  // login / register success mutation

  [types.AUTH_SUCCESS](state, payload) {
    state.user = payload;
    storage.set("token", payload.token);
    store.commit(types.CLEAR_ERROR);
  },

  // login / register failed mutation

  [types.AUTH_FAILED](state, payload) {
    store.commit(types.SET_ERROR, payload);
  },

  // logout success mutation

  [types.AUTH_KILL_SESSION](state, payload) {
    storage.remove("token");
    store.commit(types.SET_ERROR, payload);
  },

  // set user mutation

  [types.SET_USER](state, payload) {
    store.commit(types.CLEAR_ERROR);
    state.user = payload;
  },

  // get all users for admin mutation

  [types.SET_ADMIN_USERS_LIST](state, payload) {
    store.commit(types.CLEAR_ERROR);
    state.admin_users_list = payload;
  },

  // get all riders for admin mutation

  [types.SET_ADMIN_RIDERS_LIST](state, payload) {
    store.commit(types.CLEAR_ERROR);
    state.admin_riders_list = payload;
  },

  // success verification

  [types.VERIFICATION_SUCCESS](state, payload) {
    store.commit(types.CLEAR_ERROR);
    state.payment = payload;
  },

  // failed verification

  [types.VERIFICATION_FAILED](state, payload) {
    store.commit(types.SET_ERROR, payload);
    state.payment = {};
  },
};

const actions = {
  // logout user by removing token + API logout

  async [types.AUTH_LOGOUT](context) {
    context.commit(types.BUSY_LOADING);

    const csrftoken = utils.getCookie("csrftoken");

    await api({
      method: "get",
      url: LOGOUT_URL,
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
    })
      .then(function (response) {
        context.commit(types.AUTH_KILL_SESSION, response.data);
      })
      .catch(function (error) {
        context.commit(types.AUTH_FAILED, error.response.data);
      });
    context.commit(types.DONE_LOADING);
  },

  // login action to send request to API

  async [types.AUTH_LOGIN](context, payload) {
    context.commit(types.BUSY_LOADING);

    const csrftoken = utils.getCookie("csrftoken");

    await api({
      method: "post",
      url: LOGIN_URL,
      data: payload,
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
    })
      .then(function (response) {
        context.commit(types.AUTH_SUCCESS, response.data);
      })
      .catch(function (error) {
        context.commit(types.AUTH_FAILED, error.response.data);
      });

    context.commit(types.DONE_LOADING);
  },

  // register action to send request to API

  async [types.AUTH_REGISTER](context, payload) {
    context.commit(types.BUSY_LOADING);

    const csrftoken = utils.getCookie("csrftoken");

    await api({
      method: "post",
      url: REGISTER_URL,
      data: payload,
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
      },
    })
      .then(function (response) {
        context.commit(types.AUTH_SUCCESS, response.data);
      })
      .catch(function (error) {
        context.commit(types.AUTH_FAILED, error.response.data);
      });

    context.commit(types.DONE_LOADING);
  },

  // get user using token

  async [types.GET_USER](context) {
    context.commit(types.BUSY_LOADING);

    await api({
      method: "get",
      url: "/account/",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${storage.get("token")}`,
      },
    })
      .then(function (response) {
        context.commit(types.SET_USER, response.data);
        context.dispatch(types.GET_CART);
      })
      .catch(function (error) {
        context.commit(types.AUTH_FAILED, error.response.data);
      });

    context.commit(types.DONE_LOADING);
  },

  // get users list for admin

  async [types.GET_ADMIN_USERS_LIST](context) {
    context.commit(types.BUSY_LOADING);

    const csrftoken = utils.getCookie("csrftoken");

    await api({
      method: "get",
      url: ADMIN_USERS_LIST_URL,
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
        Authorization: `Token ${storage.get("token")}`,
      },
    })
      .then(function (response) {
        context.commit(types.SET_ADMIN_USERS_LIST, response.data);
      })
      .catch(function (error) {
        store.commit(types.SET_ERROR, error.response.data);
      });

    context.commit(types.DONE_LOADING);
  },

  // get riders list for admin

  async [types.GET_ADMIN_RIDERS_LIST](context) {
    context.commit(types.BUSY_LOADING);

    const csrftoken = utils.getCookie("csrftoken");

    await api({
      method: "get",
      url: ADMIN_RIDERS_LIST_URL,
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
        Authorization: `Token ${storage.get("token")}`,
      },
    })
      .then(function (response) {
        context.commit(types.SET_ADMIN_RIDERS_LIST, response.data);
      })
      .catch(function (error) {
        store.commit(types.SET_ERROR, error.response.data);
      });

    context.commit(types.DONE_LOADING);
  },

  // update user details

  async [types.AUTH_UPDATE_USER](context, payload) {
    context.commit(types.BUSY_LOADING);

    const csrftoken = utils.getCookie("csrftoken");

    await api({
      method: "post",
      url: USER_UPDATE_URL,
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken,
        Authorization: `Token ${storage.get("token")}`,
      },
      data: payload,
    })
      .then(function (response) {
        context.commit(types.SET_USER, response.data);
      })
      .catch(function (error) {
        context.commit(types.AUTH_FAILED, error.response.data);
      });

    context.commit(types.DONE_LOADING);
  },

  // verify payment

  async [types.VERIFY_PAYMENT](context) {
    context.commit(types.BUSY_LOADING);

    await api({
      method: "get",
      url: PAYMENT_VERIFICATION_URL,
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${storage.get("token")}`,
      },
    })
      .then(function (response) {
        context.commit(types.VERIFICATION_SUCCESS, response.data);
      })
      .catch(function (error) {
        context.commit(types.VERIFICATION_FAILED, error.response.data);
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
