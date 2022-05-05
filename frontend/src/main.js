import Vue from "vue";

// styles

import "@/assets/css/all.css";
import "@/assets/css/modal.css";
import "@/assets/css/tailwind.css";
import "@/assets/css/style.css";
import "@/assets/css/layouts.css";
import "@/assets/css/custom-ui.css";
import "@/assets/css/grid.css";

// js stuffs

import App from "@/App.vue";
import router from "@/router";
import store from "@/store";
import "@/components";
import "@/filters";
import "@/mixins";

Vue.config.productionTip = false;

const app = new Vue({
  router,
  store,
  render: (h) => h(App),
});
app.$mount("#app");
