<template>
    <div class="user-preview">
        <div class="user">
            <div class="user-preview-image">
                <img src="@/assets/img/user.jpg">
            </div>

            <div class="user-fullname">
                <p>{{ get_full_name }}</p>
            </div>

            <div class="user-email text-wrap">
                <label>{{ user.email }}</label>
            </div>
        </div>

        <div class="extra-details">
            <label class="text-left">Date Joined</label>
            <p>{{ user.date | date }}</p>

            <br>
            <label class="text-left">Delivery location</label>

            <form @submit.prevent="user_user_location()">
                <div class="row">
                    <div class="col s12 m12 l12">
                        <label class="form-header">
                            Location
                        </label>
                    </div>

                    <div class="col s12 m12 l12">
                        <select
                            class="rounded rounded-r-none m-0 p-2 w-full appearance-none leading-tight w-full"
                            v-model="user_delivery_location"
                            required
                        >
                            <option value="" disabled>select location</option>
                            <option
                                v-for="(location, index) in locations"
                                :key="index"
                                :value="location.id"
                            >
                                {{ location.title }}
                            </option>
                        </select>
                    </div>

                    <div class="col s12 m12 l12">
                        <button type="submit" class="h-auto p-1">
                            <span class="w-auto px-4">
                                <i class="fas fa-save"></i>
                            </span>
                            save
                        </button>
                    </div>
                </div>
            </form>

            <br>
            <label class="text-left">My Store(s)</label>

            <ul v-if="user.stores.length > 0">
                <li class="list-dec-none">
                    <router-link
                        v-for="(store, index) in user.stores"
                        :key="index"
                        :to="{
                            name: 'Store',
                            params: {
                                store_slug: store.store_slug
                            }
                        }"
                    >
                        <button class="text-left p-button">{{ store.store_name }}</button>
                    </router-link>
                </li>
            </ul>

            <div v-else>
                <label><i>you don't own any store yet</i></label>
            </div>

            <router-link :to="{ name: 'StoreCreate' }">
                <button class="p-button">
                    <i class="fas fa-store" style="padding-right: .3em"></i>
                    Create store
                </button>
            </router-link>
        </div>
    </div>
</template>

<script>
    import '@/assets/css/profile.css'

    import * as types from '@/store/types.js'
    import { mapGetters, mapActions } from 'vuex'

    export default {
        name: "UserPreview",
        data () {
            return {
                user_delivery_location: ''
            }
        },
        mounted () {
            this.get_locations()
        },
        computed: {
            ...mapGetters({
                user: 'get_user',
                locations: 'get_locations'
            }),
            get_full_name () {
                if (this.user.username) {
                    if (this.user.first_name.length > 0 && this.user.last_name.length > 0) {
                        return `${this.user.first_name} ${this.user.last_name}`
                    } else {
                        return this.user.username
                    }
                } else {
                    return 'loading ...'
                }
            }
        },
        methods: {
            ...mapActions({
                get_locations: types.GET_ADMIN_DELIVERY_LOCATIONS,
                update_location: types.USER_LOCATION_UPDATE
            }),
            user_user_location () {
                const payload = {
                    cart_location: this.user_delivery_location
                }

                this.update_location(payload)

                this.get_locations()
            }
        }
    }
</script>
