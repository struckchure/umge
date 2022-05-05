<template>
  <div class="cart-item row">
    <div class="col s12 m12 l2">
      <div class="cart-img">
        <img class="elevation-2" :src="get_item.product_image" />
      </div>
    </div>

    <div class="col s12 m12 l3">
      <div class="cart-description">
        <p>{{ get_item.product_name }}</p>
        <label>{{ get_item.product_store.store_name }}</label>
      </div>
    </div>

    <div class="col s12 m12 l7">
      <div class="cart-tools flex items-baseline">
        <button
          @click="reduce_qty()"
          class="text-center rounded-2xl bg-gray-700 hover:bg-gray-800"
        >
          <i class="fas fa-minus"></i>
        </button>

        <div class="align-middle">
          <input type="number" :min="1" :max="99" v-model="get_qty" />
        </div>

        <button
          @click="add_qty()"
          class="text-center rounded-2xl bg-gray-700 hover:bg-gray-800"
        >
          <i class="fas fa-plus"></i>
        </button>

        <p class="price">&#8358; {{ get_price }}</p>

        <button class="danger text-center" @click="delete_item">
          <i class="fas fa-trash"></i>
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
import * as types from "@/store/types.js";

export default {
  name: "CarItem",
  props: ["item"],
  data() {
    return {
      get_qty: this.item.cart_item_quantity,
    };
  },
  computed: {
    get_item() {
      return this.item.cart_item;
    },
    qty: {
      get() {
        return this.get_qty;
      },
      set(value) {
        this.get_qty = value;
      },
    },
    get_price() {
      return this.qty * this.get_item.product_price;
    },
  },
  methods: {
    ...mapActions({
      update_cart: types.UPDATE_CART,
      get_cart: types.GET_CART,
    }),
    add_qty() {
      this.get_qty += 1;

      this.update_item();
    },
    reduce_qty() {
      if (this.get_qty > 0) {
        this.get_qty -= 1;

        this.update_item();
      }
    },
    update_item() {
      const payload = {
        cart_items: [
          {
            cart_item: this.get_item.product_slug,
            cart_item_quantity: this.get_qty,
          },
        ],
      };

      this.update_cart(payload);
      this.get_cart();
    },
    delete_item() {
      const payload = {
        cart_items: [
          {
            cart_item: this.get_item.product_slug,
          },
        ],
      };

      this.update_cart(payload);
      this.get_cart();
    },
  },
};
</script>
