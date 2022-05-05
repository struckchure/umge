<template>
  <table>
    <thead>
      <tr>
        <td>#</td>
        <td>Reciepient</td>
        <td>Items</td>
        <td>Location</td>
        <td>Date</td>
        <td>Updated (Delivery time)</td>
        <td>Status</td>
        <td v-if="enable_read == true">Action</td>
      </tr>
    </thead>

    <tbody>
      <tr v-for="(task, index) in tasks" :key="index">
        <td>{{ index + 1 }}</td>
        <td class="font-bold">{{ task.reciepient.username }}</td>
        <td>{{ task.items.length }}</td>
        <td>{{ task.location.title }}</td>
        <td>{{ task.date | date }}</td>
        <td>{{ task.updated | date }}</td>
        <td>
          <label
            class="w-11 p-2 text-white rounded"
            :class="order_color(task.status)"
          >
            <i :class="order_icon(task.status)"></i>
          </label>
        </td>
        <td v-if="enable_read == true">
          <button
            class="px-3 py-1 bg-green-900 hover:bg-green-800 w-auto"
            @click="finishTask(task)"
          >
            Done
            <span class="mx-2 p-1 rounded-full bg-red-500 w-auto text-sm">
              <i class="fas fa-check"></i>
            </span>
          </button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script>
import { order_color, order_icon } from "@/store/utils.js";
import { FINISH_RIDER_TASK, GET_RIDER_TASKS } from "@/store/types.js";
import { mapActions } from "vuex";

export default {
  name: "RiderTasksList",
  props: ["tasks", "enable_read"],
  methods: {
    ...mapActions({
      finish_rider_task: FINISH_RIDER_TASK,
      get_tasks: GET_RIDER_TASKS,
    }),
    order_color,
    order_icon,
    finishTask(task) {
      const payload = {
        slug: task.slug,
      };

      this.finish_rider_task(payload);

      this.get_tasks();
    },
  },
};
</script>
