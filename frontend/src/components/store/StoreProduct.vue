<template>
  <Product :item="item" :index="index">
    <template v-slot:tools>
      <div class="flex space-around">
        <button class="success btn-small flex-1 text-center">
          <i class="fas fa-edit"></i>
        </button>

        <button class="danger btn-small flex-1 text-center">
          <i class="fas fa-trash"></i>
        </button>
      </div>
    </template>
  </Product>
</template>

<script>
import Product from "@/components/products/Product.vue";

export default {
  name: "StoreProduct",
  props: ["item", "index"],
  components: {
    Product,
  },
};
</script>
