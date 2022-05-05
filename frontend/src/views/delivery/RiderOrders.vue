<template>
  <Base>
    <template v-slot:main>
      <div class="row">
        <div class="col s12 m12 l12">
          <div class="header">
            <label class="form-header"> Riders / Requests </label>
          </div>

          <RiderOrderList :orders="orders" />
        </div>
      </div>
    </template>
  </Base>
</template>

<script>
import RiderOrderList from "@/components/delivery/RiderOrderList.vue";

import * as types from "@/store/types.js";
import { mapGetters, mapActions } from "vuex";

import "@/assets/css/grid.css";
import "@/assets/css/delivery.css";

export default {
  name: "RiderOrders",
  title() {
    return "Riders | Orders";
  },
  mounted() {
    this.get_admin_orders();
  },
  components: {
    RiderOrderList,
  },
  computed: {
    ...mapGetters({
      orders: "get_admin_orders",
    }),
  },
  methods: {
    ...mapActions({
      get_admin_orders: types.GET_ORDERS,
    }),
  },
};
</script>
