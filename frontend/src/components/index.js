import Vue from "vue";

import Base from "@/layouts/Base.vue";
import ItemListContainer from "@/components/common/ItemListContainer.vue";

// components declarations

const components = {
  Base,
  ItemListContainer,
};

Object.entries(components).forEach(([name, component]) =>
  Vue.component(name, component)
);
