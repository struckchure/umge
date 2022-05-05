<template>
  <AccountBase>
    <div class="row flex-left-v">
      <div class="col s12 m12 l12">
        <p class="form-title">Create Account</p>
      </div>

      <div class="col s12 m12">
        <div class="social-links">
          <a href="#">
            <button class="social">
              <i class="fab fa-google"></i>
            </button>
          </a>

          <a href="#">
            <button class="social">
              <i class="fab fa-facebook-f"></i>
            </button>
          </a>

          <a href="#">
            <button class="social">
              <i class="fab fa-twitter"></i>
            </button>
          </a>
        </div>
      </div>

      <div class="col s12 m12 l12">
        <form @submit.prevent="register">
          <div class="auth-field flex flex-row">
            <i class="fas fa-user"></i>
            <input
              type="text"
              placeholder="Username"
              v-model="username"
              required
              maxlength="15"
            />
          </div>

          <div class="auth-field flex flex-row">
            <i class="fas fa-envelope"></i>
            <input
              type="email"
              placeholder="Email"
              v-model="email"
              required
              maxlength="50"
            />
          </div>

          <div class="auth-field flex flex-row">
            <i class="fas fa-lock"></i>
            <input
              type="password"
              placeholder="Password"
              v-model="password"
              required
              maxlength="20"
            />
          </div>

          <button>Sign Up</button>
        </form>
      </div>

      <div class="col s12 m12 l12">
        <div class="account-options">
          <label
            >Already have an account ?
            <router-link to="/accounts/login/">login</router-link></label
          >
        </div>
      </div>

      <div class="col s12 m12 l12">
        <div class="disp-flex-bottom">
          <router-link to="/">
            <button>Return to home</button>
          </router-link>
        </div>
      </div>
    </div>
  </AccountBase>
</template>

<script>
import AccountBase from "@/layouts/AccountBase.vue";
import { mapGetters, mapActions } from "vuex";
import * as types from "@/store/types.js";

export default {
  name: "Register",
  components: {
    AccountBase,
  },
  title() {
    return "Register";
  },
  data() {
    return {
      username: "",
      email: "",
      password: "",
    };
  },
  computed: {
    ...mapGetters(["is_authenticated"]),
  },
  methods: {
    ...mapActions({
      register_user: types.AUTH_REGISTER,
    }),
    register() {
      const payload = {
        username: this.username,
        email: this.email,
        password: this.password,
      };

      this.register_user(payload);

      if (this.is_authenticated == true) {
        return this.$router.push({ name: "Login" });
      }
    },
  },
};
</script>
