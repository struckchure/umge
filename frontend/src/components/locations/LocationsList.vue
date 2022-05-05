<template>
  <div class="overflow-auto">
    <table>
      <thead>
        <tr>
          <td class="sn">#</td>
          <td>Location</td>
          <td>Region</td>
          <td>Date</td>
          <td>Updated</td>
          <td colspan="2">Actions</td>
        </tr>
      </thead>

      <tbody>
        <tr v-for="(location, index) in locations" :key="index">
          <td>{{ index + 1 }}</td>
          <td>{{ location.title }}</td>
          <td>{{ location.location_region.region }}</td>
          <td>{{ location.date | date }}</td>
          <td>{{ location.updated | date }}</td>
          <td colspan="2" class="flex">
            <button class="p-1 w-auto h-auto bg-red-400">
              <i class="fas fa-edit text-sm"></i>
            </button>
            <button class="p-1 w-auto h-auto bg-red-600">
              <i class="fas fa-trash text-sm"></i>
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "LocationsList",
  props: ["locations"],
};
</script>
