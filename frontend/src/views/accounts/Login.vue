<template>
    <AccountBase>
        <div class="row flex-left-v">
            <div class="col s12 m12 l12">
                <p class="form-title">Get strapped in ...</p>
            </div>

            <div class="col s12 m12 l12">
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
                <form @submit.prevent="login">
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
                        <i class="fas fa-lock"></i>
                        <input
                            type="password"
                            placeholder="Password"
                            v-model="password"
                            required
                            maxlength="20"
                        />
                    </div>

                    <button>Sign In</button>
                </form>
            </div>

            <div class="col s12 m12 l12">
                <div class="account-options">
                    <label>New here ?<router-link to="/accounts/register/">register</router-link></label>
                </div>
            </div>

            <div class="col s12 m12 l12">
                <div class="disp-flex-bottom">
                    <router-link to="/">
                        <button id="submit_button">Return to home</button>
                    </router-link>
                </div>
            </div>
        </div>
    </AccountBase>
</template>


<script>
    import AccountBase from '@/layouts/AccountBase.vue'
    import { mapGetters, mapActions } from 'vuex'
    import * as types from '@/store/types.js'

    export default {
        name: 'Login',
        components: {
            AccountBase
        },
        title () {
            return 'Login'
        },
        data () {
            return {
                username: '',
                password: ''
            }
        },
        computed: {
            ...mapGetters({
                is_authenticated: 'is_authenticated',
                error: 'get_error'
            })
        },
        methods: {
            ...mapActions({
                'login_user': types.AUTH_LOGIN
            }),
            login () {
                var submit_button = document.getElementById('submit_button')
                submit_button.disabled = true

                const payload = {
                    username: this.username,
                    password: this.password
                }

                this.login_user(payload)

                if (this.is_authenticated === true) {
                    this.$router.push({ name: 'Home' })
                }
            }
        }
    }
</script>
