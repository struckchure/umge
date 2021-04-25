<template>
    <div class="user-update">
        <label class="form-header">Personal Details</label>
        <form @submit.prevent="update_profile()">
            <div class="row">
                <div class="col s12 m12 l12">
                    <label class="form-label text-left">Full name</label>
                </div>

                <div class="col s12 m6 l6">
                    <input
                        type="text"
                        placeholder="First name"
                        v-model="user.first_name"
                        maxlength="20"
                    />
                </div>

                <div class="col s12 m6 l6">
                    <input
                        type="text"
                        placeholder="Last name"
                        v-model="user.last_name"
                        maxlength="20"
                    />
                </div>

                <div class="col s12 m12 l12">
                    <label class="form-label text-left">Username</label>
                </div>

                <div class="col s12 m12 l12">
                    <input
                        type="text"
                        placeholder="username"
                        v-model="user.username"
                        required
                        maxlength="25"
                    />
                </div>

                <div class="col s12 m12 l12">
                    <label class="form-label text-left">E-Mail</label>
                </div>

                <div class="col s12 m12 l12">
                    <input
                        type="email"
                        placeholder="e-mail"
                        v-model="user.email"
                        maxlength="40"
                    />
                </div>

                <div class="col s12 m12 l12">
                    <label class="form-label text-left">Phone number</label>
                </div>

                <div class="col s3 m2 l2">
                    <input
                        type="number"
                        placeholder="Phone number"
                        v-model="country_code"
                        readonly
                    />
                </div>

                <div class="col s9 m10 l10">
                    <input
                        type="number"
                        placeholder="Phone number"
                        maxlength="15"
                    />
                </div>

                <div class="col s12 m12 l12">
                    <label class="form-label text-left">Password</label>
                </div>

                <div class="col s12 m12 l12">
                    <input
                        type="password"
                        placeholder="Current password"
                        v-model="current_password"
                        required
                        minlength="5"
                        maxlength="15"
                    />
                </div>

                <div class="col s12 m6 l6">
                    <input
                        type="password"
                        placeholder="New password"
                        v-model="new_password"
                        minlength="5"
                        maxlength="15"
                    />
                </div>

                <div class="col s12 m6 l6">
                    <input
                        type="password"
                        placeholder="Confirm password"
                        v-model="confirm_password"
                        minlength="5"
                        maxlength="15"
                    />
                </div>
            </div>

            <button type="submit">Save changes</button>
        </form>
    </div>
</template>

<script>
    import '@/assets/css/profile.css'

    import { mapGetters, mapActions } from 'vuex'
    import * as types from '@/store/types.js'

    export default {
        name: 'UserUpdate',
        computed: {
            ...mapGetters({
                user: 'get_user',
                error: 'get_error'
            })
        },
        data () {
            return {
                country_code: '+234',
                current_password: '',
                new_password: '',
                confirm_password: ''
            }
        },
        methods: {
            ...mapActions({
                update_user: types.AUTH_UPDATE_USER,
                validate_user: types.AUTH_LOGIN
            }),
            update_profile () {
                var user_cred = {
                    username: this.user.username,
                    password: this.current_password
                }

                this.validate_user(user_cred)

                if (this.error == null) {
                    var payload = {
                        first_name: this.user.first_name,
                        last_name: this.user.last_name,
                        email: this.user.email,
                        username: this.user.username,
                        current_password: this.current_password,
                        new_password: this.new_password,
                        confirm_password: this.confirm_password
                    }

                    this.update_user(payload)
                }
            }
        }
    }
</script>
