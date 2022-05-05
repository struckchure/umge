import api from "@/store/axiosConfig.js";
import * as utils from "@/store/utils.js";
import * as types from "@/store/types.js";

// endpoints

const ORDERS_URL = "/delivery/orders/";
const ADMIN_ORDERS_URL = "/delivery/admin/orders/";
const RIDER_TASKS_URL = "/delivery/riders/tasks/";
const RIDER_ORDERS_URL = "/delivery/riders/orders/";

// storage

const storage = new utils.Storage();

const state = {
  orders: [],
  admin_orders: [],
  tasks: [],
  task_finished: {},
};

const getters = {
  get_orders(state) {
    return state.orders;
  },

  get_admin_orders(state) {
    return state.admin_orders;
  },

  get_tasks(state) {
    return state.tasks;
  },

  get_task_finished(state) {
    return state.task_finished;
  },
};

const mutations = {
  // orders list mutation

  [types.SET_ORDERS](state, payload) {
    state.orders = payload;
  },

  // admin orders list mutation

  [types.SET_ADMIN_ORDERS](state, payload) {
    state.admin_orders = payload;
  },

  // set rider tasks

  [types.SET_RIDER_TASKS](state, payload) {
    state.tasks = payload;
  },

  // success mutation to update rider tasks finished

  [types.SET_FINISH_RIDER_TASK](state, payload) {
    state.task_finished = payload;
  },
};

const actions = {
  // get orders for user

  async [types.GET_ORDERS](context) {
    context.commit(types.BUSY_LOADING);

    await api({
      method: "get",
      url: ORDERS_URL,
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${storage.get("token")}`,
      },
    })
      .then(function (response) {
        context.commit(types.SET_ORDERS, response.data);
      })
      .catch(function (error) {
        context.commit(types.SET_ERROR, error.response.data);
      });

    context.commit(types.DONE_LOADING);
  },

  // get orders for admin

  async [types.GET_ADMIN_ORDERS](context) {
    context.commit(types.BUSY_LOADING);

    await api({
      method: "get",
      url: ADMIN_ORDERS_URL,
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${storage.get("token")}`,
      },
    })
      .then(function (response) {
        context.commit(types.SET_ADMIN_ORDERS, response.data);
      })
      .catch(function (error) {
        context.commit(types.SET_ERROR, error.response.data);
      });

    context.commit(types.DONE_LOADING);
  },

  // accept delivery(collection of orders)

  async [types.RIDER_ACCEPT_DELIVERY](context, payload) {
    context.commit(types.BUSY_LOADING);

    await api({
      method: "get",
      url: `${RIDER_ORDERS_URL}${payload.username}/accept/`,
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${storage.get("token")}`,
      },
    })
      .then(function (response) {
        context.commit(types.SET_SUCCESS, response.data);
      })
      .catch(function (error) {
        context.commit(types.SET_ERROR, error.data);
      });

    context.commit(types.DONE_LOADING);
  },

  // get rider tasks

  async [types.GET_RIDER_TASKS](context, delivery_status = "PS") {
    context.commit(types.BUSY_LOADING);

    await api({
      method: "get",
      url: `${RIDER_TASKS_URL}${delivery_status}`,
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${storage.get("token")}`,
      },
    })
      .then(function (response) {
        context.commit(types.SET_RIDER_TASKS, response.data);
      })
      .catch(function (error) {
        context.commit(types.SET_ERROR, error.data);
      });

    context.commit(types.DONE_LOADING);
  },

  // endpoint to notify when delivery / task is done

  async [types.FINISH_RIDER_TASK](context, payload) {
    context.commit(types.BUSY_LOADING);

    await api({
      method: "get",
      url: `${RIDER_TASKS_URL}${payload.slug}/finish/`,
      headers: {
        "Content-Type": "application/json",
        Authorization: `Token ${storage.get("token")}`,
      },
    })
      .then(function (response) {
        context.commit(types.SET_FINISH_RIDER_TASK, response.data);

        const message = {
          message:
            "Congratulations !!! on finishing your task, you can now accept a new order",
        };

        context.commit(types.SET_SUCCESS, message);
      })
      .catch(function (error) {
        context.commit(types.SET_ERROR, error.data);
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
