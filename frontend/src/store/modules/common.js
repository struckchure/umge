import * as types from "@/store/types.js";

const state = {
  error: null,
  success: null,
  is_loading: false,
};

const getters = {
  get_error(state) {
    return state.error;
  },
  get_success(state) {
    return state.success;
  },
  get_is_loading(state) {
    return state.is_loading;
  },
};

const mutations = {
  // success mutation

  [types.SET_SUCCESS](state, payload) {
    state.success = payload;
  },

  // clear succes mutation

  [types.CLEAR_SUCCESS](state) {
    state.success = null;
  },

  // error mutation

  [types.SET_ERROR](state, payload) {
    state.error = payload;
  },

  // clear error

  [types.CLEAR_ERROR](state) {
    state.error = null;
  },

  // done loading mutation

  [types.DONE_LOADING](state) {
    state.is_loading = false;
  },

  // still loading mutation

  [types.BUSY_LOADING](state) {
    state.is_loading = true;
  },
};

const actions = {};

export default {
  state,
  getters,
  mutations,
  actions,
};
