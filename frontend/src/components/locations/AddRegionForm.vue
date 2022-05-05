<template>
  <div class="modal" id="add_region_form">
    <div class="modal-tools">
      <button
        type="button"
        @click="close_modal('add_region_form')"
        class="modal-close"
      >
        &times;
      </button>
    </div>

    <div class="modal-content">
      <div class="modal-header">
        <label class="product-preference-title"> Region / Add / </label>
      </div>

      <div class="modal-body pa-1">
        <form @submit.prevent="add_region()" class="px-5">
          <div class="row">
            <div class="col s12 m12 l12">
              <label class="form-header"> Region </label>
            </div>

            <div class="col s12 m12 l12">
              <input type="text" class="w-full" v-model="new_region" />
            </div>

            <div class="col s12 m12 l12">
              <button class="w-full px-1 py-2" type="submit">
                Save Region
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import "@/assets/css/modal.css";
import * as _modal from "@/assets/js/modal.js";

import {
  CREATE_ADMIN_DELIVERY_REGION,
  GET_ADMIN_DELIVERY_REGIONS,
} from "@/store/types.js";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "AddRegionForm",
  data() {
    return {
      new_region: "",
    };
  },
  mounted() {},
  computed: {
    ...mapGetters({
      user: "get_user",
    }),
  },
  methods: {
    close_modal: _modal.close_modal,
    ...mapActions({
      create_region: CREATE_ADMIN_DELIVERY_REGION,
      get_regions: GET_ADMIN_DELIVERY_REGIONS,
    }),
    add_region() {
      const coordinates = {
        latitude: 5.547373458458345,
        longitude: 2.345346457547,
      };

      const payload = {
        region_author: this.user.id,
        region: this.new_region,
        latitude: coordinates.latitude,
        longitude: coordinates.longitude,
      };

      this.create_region(payload);

      this.get_regions();

      this.close_modal("add_region_form");
    },
  },
};
</script>
