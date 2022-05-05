<template>
  <Base>
    <template v-slot:main>
      <div class="row">
        <div class="col s12 m12 l12">
          <div class="header">
            <label class="form-header">Delivery / Orders</label>
          </div>

          <OrdersList :orders="orders" />
        </div>
      </div>
    </template>
  </Base>
</template>

<script>
import * as types from "@/store/types.js";
import { mapGetters, mapActions } from "vuex";

import OrdersList from "@/components/delivery/OrdersList.vue";

export default {
  name: "Orders",
  title() {
    return "Delivery | Orders";
  },
  components: {
    OrdersList,
  },
  mounted() {
    this.get_orders();
  },
  computed: {
    ...mapGetters({
      orders: "get_orders",
    }),
  },
  methods: {
    ...mapActions({
      get_orders: types.GET_ORDERS,
    }),
  },
};
</script>
