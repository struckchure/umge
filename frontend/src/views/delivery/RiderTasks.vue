<template>
  <Base>
    <template v-slot:main>
      <div class="row">
        <div class="col s12 m12 l12">
          <div class="header">
            <label class="form-header">Rider / Tasks</label>
          </div>
        </div>

        <div class="col s12 m12 l12">
          <RiderTasksList :enable_read="true" :tasks="tasks" />
        </div>
      </div>
    </template>
  </Base>
</template>

<script>
import RiderTasksList from "@/components/delivery/RiderTasksList.vue";
import * as types from "@/store/types.js";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "RiderTasks",
  components: {
    RiderTasksList,
  },
  title() {
    return "Rider | Tasks";
  },
  mounted() {
    this.get_tasks();
  },
  computed: {
    ...mapGetters({
      tasks: "get_tasks",
    }),
  },
  methods: {
    ...mapActions({
      get_tasks: types.GET_RIDER_TASKS,
    }),
  },
};
</script>
