<template>
  <Base current_page="Profile" page_title="Profile">
    <template v-slot:main>
      <div class="row">
        <div class="col s12 m4 m4">
          <UserPreview />
        </div>

        <div class="col s12 m8 m8">
          <UserUpdate />
        </div>
      </div>
    </template>
  </Base>
</template>

<script>
import "@/assets/css/profile.css";
import UserPreview from "@/components/accounts/UserPreview.vue";
import UserUpdate from "@/components/accounts/UserUpdate.vue";

export default {
  name: "Profile",
  title() {
    return "Dashboard | Profile";
  },
  components: {
    UserPreview,
    UserUpdate,
  },
};
</script>
