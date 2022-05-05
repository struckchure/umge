<template>
  <div class="overflow-auto">
    <table>
      <thead>
        <tr>
          <td class="sn">#</td>
          <td>Transaction ID</td>
          <td>Amount</td>
          <td>Date</td>
          <td>Status</td>
        </tr>
      </thead>

      <tbody>
        <tr v-for="(history, index) in histories" :key="index">
          <td>{{ index + 1 }}</td>
          <td>{{ history.reference }}</td>
          <td class="font-bold">&#8358; {{ history.amount }}</td>
          <td>{{ history.date | date }}</td>
          <td>
            <label
              class="w-full p-2 text-white rounded"
              :class="get_status_class(history.status)"
            >
              {{ get_status_text(history.status) }}
            </label>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "WalletHistoryList",
  props: ["histories"],
  methods: {
    get_status_class(status) {
      let status_class;

      switch (status) {
        case "U":
          status_class = "bg-yellow-500";
          break;
        case "V":
          status_class = "bg-green-500";
          break;
        case "C":
          status_class = "bg-red-500";
          break;
      }

      return [status_class];
    },
    get_status_text(status) {
      let status_text;

      switch (status) {
        case "U":
          status_text = "Unverified";
          break;
        case "V":
          status_text = "Verified";
          break;
        case "C":
          status_text = "Cancelled";
          break;
      }

      return status_text;
    },
  },
};
</script>
