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
            <p>{{ format_date(user.date) }}</p>

            <br>
            <label class="text-left">Ratings</label>
            <label class="text-left pama-0" style="font-weight: normal;">4.5 / 5</label>
            <p>
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star-half-alt"></i>
            </p>

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

    import { mapGetters } from 'vuex'

    export default {
        name: "UserPreview",
        computed: {
            ...mapGetters({
                user: 'get_user'
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
            format_date (date) {
                var format_date_ = new Date(date)

                return `${format_date_.getDay()}/${format_date_.getMonth()}/${format_date_.getFullYear()}` // day, month year
            }
        }
    }
</script>
