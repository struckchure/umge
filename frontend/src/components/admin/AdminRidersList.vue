<template>
  <div class="overflow">
    <table>
      <thead>
        <tr>
          <td>Username</td>
          <td>E-Mail</td>
          <td>Details</td>
          <td>Date joined</td>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(rider, index) in riders"
          :key="index"
          class="hover:bg-gray-400 hover:text-white cursor-pointer"
        >
          <td>{{ rider.username }}</td>
          <td>{{ rider.email }}</td>
          <td>
            <router-link to="/">
              <button class="btn btn-small ma-0">
                <i class="fas fa-eye"></i>
              </button>
            </router-link>
          </td>
          <td>{{ rider.date | date }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import "@/assets/css/table.css";

export default {
  name: "AdminRidersList",
  props: ["riders"],
};
</script>
