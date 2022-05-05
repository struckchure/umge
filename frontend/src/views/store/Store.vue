<template>
  <Base>
    <template v-slot:breadcrumb>
      <div class="flex flex-h-center disp-flex-h">
        <div class="store-image">
          <img :src="store.store_image" />
        </div>

        <div class="store-name">
          <p>
            {{ store.store_name }}
          </p>
        </div>

        <div class="store-description">
          <p>
            {{ store.store_description }}
          </p>
        </div>
      </div>

      <div v-if="is_store_owner" class="store-tools">
        <button class="btn-small" @click="show_modal('add_product')">
          <i class="fas fa-plus"></i>
        </button>
      </div>

      <div class="modal" id="add_product">
        <div class="modal-tools">
          <button @click="close_modal('add_product')" class="modal-close">
            &times;
          </button>
        </div>
        <ProductAdd :store_slug="store_slug" />
      </div>

      <StoreProductList :store_slug="store_slug" />
    </template>
  </Base>
</template>

<script>
import "@/assets/css/store.css";
import StoreProductList from "@/components/store/StoreProductList.vue";
import ProductAdd from "@/components/products/ProductAdd.vue";

import { mapGetters, mapActions } from "vuex";
import * as types from "@/store/types.js";
import * as _modal from "@/assets/js/modal.js";

export default {
  name: `Store`,
  props: ["store_slug"],
  components: {
    StoreProductList,
    ProductAdd,
  },
  title() {
    return "Store";
  },
  mounted() {
    this.get_user();
    this.get_store(this.store_slug);
  },
  computed: {
    ...mapGetters({
      store: "get_store",
      user: "get_user",
      is_authenticated: "is_authenticated",
    }),
    is_store_owner() {
      if (this.is_authenticated) {
        if (this.user.id === this.store.store_owner.id) {
          return true;
        } else {
          return false;
        }
      } else {
        return false;
      }
    },
  },
  methods: {
    ...mapActions({
      get_store: types.GET_STORE,
      get_user: types.GET_USER,
    }),
    show_modal: _modal.show_modal,
    close_modal: _modal.close_modal,
  },
};
</script>
