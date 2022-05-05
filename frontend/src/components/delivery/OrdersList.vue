<template>
  <div class="overflow">
    <table>
      <thead>
        <tr>
          <td class="sn">#</td>
          <td>Reference</td>
          <td>Product</td>
          <td>Status</td>
          <td>Price</td>
          <td>Date</td>
        </tr>
      </thead>

      <tbody>
        <tr
          v-for="(order, index) in orders"
          :key="index"
          class="hover:bg-gray-400 hover:text-white cursor-pointer h-auto"
        >
          <td>{{ index + 1 }}</td>
          <td>{{ order.transaction_id }}</td>
          <td class="row">
            <img
              :src="order.item.cart_item.product_image"
              :alt="order.item.cart_item.product_name"
              class="col s2 w-5 h-7"
            />
            <p class="col s10">
              {{ order.item.cart_item.product_name }}
            </p>
          </td>
          <td>
            <label
              class="w-11 p-2 text-white rounded"
              :class="order_color(order.status)"
            >
              <i :class="order_icon(order.status)"></i>
            </label>
          </td>
          <td>{{ order.item.cart_item.product_price }}</td>
          <td>{{ order.date | date }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import { order_color, order_icon } from "@/store/utils.js";

export default {
  name: "OrdersList",
  props: ["orders"],
  methods: {
    order_color,
    order_icon,
  },
};
</script>
