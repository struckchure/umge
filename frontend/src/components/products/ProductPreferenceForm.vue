<template>
  <div class="modal-content">
    <div class="modal-header">
      <label class="product-preference-title">
        {{ get_title }} / {{ item.product_store.store_name }} /
        {{ item.product_name }}
      </label>
    </div>

    <div class="modal-body">
      <form class="product-preference" @submit.prevent="add_to_cart">
        <div class="row">
          <div v-if="buy_now === 'buy'" class="col s12 m12 l12">
            <label class="text-left w-100">Payment mode</label>
            <small>You're using {{ get_payment_mode_name }} payment</small
            ><br />
            <div class="relative">
              <select
                v-model="payment_mode"
                class="
                  block
                  appearance-none
                  w-full
                  bg-gray-200
                  border border-gray-200
                  text-gray-700
                  py-3
                  px-4
                  pr-8
                  rounded
                  leading-tight
                  focus:outline-none focus:bg-white
                "
              >
                <option value="W">Wallet</option>
                <option value="C">Card</option>
              </select>
              <div
                class="
                  pointer-events-none
                  absolute
                  inset-y-0
                  right-0
                  flex
                  items-center
                  px-2
                  text-gray-700
                "
              >
                <i class="fas fa-angle-down"></i>
              </div>
            </div>
          </div>

          <div class="col s12 m12 l12">
            <label class="text-left w-100">Description</label>
            <div class="input-field">
              <textarea
                class="h-full"
                type="text"
                placeholder="add extra description here ..."
                v-model="description"
                style="color: white !important"
              />
            </div>
          </div>

          <div class="col s2 m2 l2">
            <label class="text-left w-100">Quantity</label>
            <div class="input-field">
              <input
                type="number"
                minlength="1"
                maxlength="2"
                min="1"
                max="99"
                v-model="qty"
              />
            </div>
          </div>

          <div class="col push-s10 push-m10 push-l10"></div>

          <div class="col s12 m12 l12">
            <div class="product-amount-details">
              <div class="row">
                <div class="col s12 m12 l12 amount-details">
                  <label>Price</label>
                  <label>&#8358; {{ item.product_price }} X {{ qty }}</label>
                </div>

                <div
                  class="col s12 m12 l12 amount-details"
                  v-for="(option, index) in options"
                  :key="index"
                >
                  <label>{{ option.option_name }}</label>
                  <label>&#8358; {{ option.option_price }}</label>
                </div>

                <div
                  class="col s12 m12 l12 amount-details"
                  style="
                    border-top: 1px solid #eee;
                    padding-top: 0.5em;
                    margin-top: 0.5em;
                  "
                >
                  <label>Total</label>
                  <label>&#8358; {{ get_total_amount }}</label>
                </div>
              </div>
            </div>
          </div>

          <div class="col s12 m12 l12 options">
            <div class="row">
              <div
                class="col s6 m6 l6"
                v-for="(option, index) in get_options"
                :key="index"
              >
                <div class="input-field">
                  <input type="checkbox" @change="add_option(option)" />
                  <label class="text-left">
                    &#8358; {{ option.option_price }} {{ option.option_name }}
                  </label>
                </div>
              </div>
            </div>
          </div>

          <div class="col s12 m12 l12">
            <button type="submit">Proceed</button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import "@/assets/css/product.css";

import { mapActions, mapGetters, mapMutations } from "vuex";
import * as types from "@/store/types.js";
import { close_modal } from "@/assets/js/modal.js";

export default {
  name: "ProductPreferenceForm",
  props: ["product_id", "item", "buy_now"],
  data() {
    return {
      qty: 1,
      description: "",
      options: {},
      total_amount: 0,
      payment_mode: "C",
      current_location: {},
    };
  },
  computed: {
    ...mapGetters({
      error: "get_error",
      purchase: "get_purchase",
    }),
    get_options() {
      return this.item.product_options;
    },
    get_total_amount() {
      var total_amount = this.total_amount + this.item.product_price;

      return total_amount * this.qty;
    },
    get_title() {
      let title;

      switch (this.buy_now) {
        case "buy":
          title = "Buy";
          break;
        case "cart":
          title = "Cart";
          break;
      }
      return title;
    },
    get_payment_mode_name() {
      let name;

      switch (this.payment_mode) {
        case "C":
          name = "card";
          break;
        case "W":
          name = "wallet";
          break;
      }
      return name;
    },
  },
  methods: {
    ...mapActions({
      update_cart: types.UPDATE_CART,
      buy_item: types.BUY_NOW,
      get_cart: types.GET_CART,
    }),
    ...mapMutations({
      set_success: types.SET_SUCCESS,
    }),
    add_option(option) {
      var option_keys = Object.keys(this.options);
      var key = option.option_slug;

      if (option_keys.indexOf(key) > -1) {
        this.total_amount -= option.option_price; // deduct option price
        delete this.options[key]; // remove option from cart options
      } else {
        this.total_amount += option.option_price; // add option price
        this.options[key] = option; // add option to cart option
      }
    },
    add_to_cart() {
      let payload;

      var options = [];
      // var keys = Object.keys(this.options)

      // for (var i = 0; i < keys.length; i++) {
      //  var option = this.options[keys[i]]
      //  options.unshift(option.option_slug)
      // }

      var cart_items = [
        {
          cart_item: this.item.product_slug,
          cart_item_quantity: this.qty,
          cart_item_description: this.description,
          cart_item_options: options,
        },
      ];

      switch (this.buy_now) {
        case "buy":
          payload = {
            cart_item: this.item.product_slug,
            cart_item_quantity: this.qty,
            cart_item_description: this.description,
            cart_item_options: options,
            payment_mode: this.get_payment_mode_name.toUpperCase(),
            cart_location: this.current_location,
          };

          this.buy_item(payload);
          break;
        case "cart":
          payload = {
            cart_items,
            cart_location: this.current_location,
          };

          this.update_cart(payload);
          break;
      }

      if (this.payment_mode == "C" && this.purchase.response) {
        const success_payload = {
          success: this.purchase.response.data.message,
        };

        this.set_success(success_payload);
        setTimeout(() => {
          var next_url = this.purchase.response.data.authorization_url;
          window.location.replace(next_url);
        }, 500);
      }

      this.close_modal(this.product_id);
    },
    close_modal(product_id) {
      close_modal(product_id);
    },
  },
};
</script>
