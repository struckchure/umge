<template>
    <div class="pama-0">
        <aside class="overflow overflow-hide-scroll">
            <router-link
                :to="{ name: 'Home' }"
                title="UMGE"
            >
                <img src="@/assets/logo.png" class="logo">
            </router-link>

            <label class="sidebar-divider">
                <i class="fas fa-user"></i>
                <span>Account</span>
            </label>

            <router-link :to="{ name: 'Home' }">
                <button class="active">
                    <i class="fas fa-home"></i>
                    <span>Home</span>
                </button>
            </router-link>

            <router-link :to="{ name: 'Profile' }">
                <button>
                    <i class="fas fa-user"></i>
                    <span>Profile</span>
                </button>
            </router-link>

            <router-link :to="{ name: 'Wallet' }">
                <button>
                    <i class="fas fa-wallet"></i>
                    <span>Wallet</span>
                </button>
            </router-link>

            <router-link :to="{ name: 'Orders' }">
                <button>
                    <i class="fas fa-history"></i>
                    <span>Orders</span>
                </button>
            </router-link>

            <div class="pama-0" v-if="is_admin == true">
                <label class="sidebar-divider">
                    <i class="fas fa-user-tie"></i>
                    <span>Management</span>
                </label>

                <router-link
                    :to="{ name: 'AdminHome' }">
                    <button>
                        <i class="fas fa-tachometer-alt"></i>
                        <span>Dashboard</span>
                    </button>
                </router-link>

                <router-link
                    :to="{ name: 'AdminHome' }">
                    <button>
                        <i class="fas fa-store"></i>
                        <span>Stores</span>
                    </button>
                </router-link>

                <router-link
                    :to="{ name: 'AdminOrders' }">
                    <button>
                        <i class="fas fa-history"></i>
                        <span>Orders</span>
                    </button>
                </router-link>

                <router-link
                    :to="{ name: 'AdminRiders' }">
                    <button>
                        <i class="fas fa-biking"></i>
                        <span>Riders</span>
                    </button>
                </router-link>

                <router-link
                    :to="{ name: 'AdminRidersApplications' }">
                    <button>
                        <i class="fas fa-ticket-alt"></i>
                        <span>Applications</span>
                    </button>
                </router-link>

                <router-link
                    :to="{ name: 'AdminLocations' }"
                >
                    <button>
                        <i class="fas fa-map-marker-alt"></i>
                        <span>Locations</span>
                    </button>
                </router-link>
            </div>

            <div class="pama-0" v-if="is_staff == true">
                <label class="sidebar-divider">
                    <i class="fas fa-biking"></i>
                    <span>Riders</span>
                </label>

                <router-link
                    :to="{ name: 'RiderOrders' }">
                    <button>
                        <i class="fas fa-history"></i>
                        <span>Orders</span>
                    </button>
                </router-link> 

                <router-link
                    :to="{ name: 'RiderTasks' }">
                    <button>
                        <i class="fas fa-bookmark"></i>
                        <span>Tasks</span>
                    </button>
                </router-link>

                <router-link
                    :to="{ name: 'RiderHistory' }">
                    <button>
                        <i class="fas fa-tasks"></i>
                        <span>History</span>
                    </button>
                </router-link>                
            </div>

            <label class="sidebar-divider">
                <span>
                    {{ '' }}
                </span>
            </label>

            <router-link
                v-if="is_authenticated == true"
                :to="{ name: 'Logout' }">
                <button>
                    <i class="fas fa-sign-out-alt"></i>
                    <span>Logout</span>
                </button>
            </router-link>

            <router-link
                v-else
                :to="{ name: 'Login' }"
            >
                <button>
                    <i class="fas fa-sign-in-alt"></i>
                    <span>Login</span>
                </button>
            </router-link>
        </aside>

        <main class="h-screen overflow-auto">
            <div class="navbar">
                <div class="brand-name"></div>

                <div class="pama-0" v-if="is_authenticated == true">
                    <div class="cart w-auto mx-1 md:mx-16">
                        <p class="wallet-balance w-auto">
                            &#8358; {{ user.wallet.wallet_balance }}
                        </p>

                        <div class="flex center">
                            <router-link :to="{ name: 'Cart' }">
                                <button class="fntz-8 pa-1 flex-h-center flex-1 btn-small bg-red-500">
                                    <i class="fas fa-shopping-cart"></i>
                                </button>
                            </router-link>
                            <label class="w-12">{{ user.cart.cart_items.length }}</label>
                        </div>
                    </div>
                </div>
                <router-link
                    v-else
                    :to="{ name: 'Login' }"
                >
                    <button class="btn-small w-100 fntz-10">
                        <i class="fas fa-sign-in-alt pa-lr-1"></i>
                        <span>Login</span>
                    </button>
                </router-link>
            </div>

            <div class="main-container">
                <slot name="main">
                    <div class="entry-card">
                        <div class="row">
                            <div class="col s12 m12 l12">
                                <slot name="breadcrumb">
                                    <div class="breadcrumb">
                                        <p class="page-title">{{ page_title }}</p>

                                        <div class="breadcrumb-extra">
                                            <slot name="extra"></slot>
                                        </div>
                                    </div>
                                </slot>
                            </div>

                            <div class="col s12 m12 l12 my-3">
                                <slot></slot>
                            </div>
                        </div>
                    </div>
                </slot>
            </div>
        </main>

        <ErrorModal />
        <Loader />
    </div>
</template>

<script>
    import { mapGetters, mapActions } from 'vuex'
    import * as types from '@/store/types.js'

    import ErrorModal from '@/components/common/ErrorModal.vue'
    import Loader from '@/components/common/Loader.vue'

    export default {
        name: 'Base',
        props: [
            'current_page',
            'page_title'
        ],
        components: {
            ErrorModal,
            Loader
        },
        mounted () {
            if (this.is_authenticated === true) {
                this.get_user()
            }
        },
        computed: {
            ...mapGetters({
                user: 'get_user',
                is_authenticated: 'is_authenticated',
                is_admin: 'is_admin',
                is_staff: 'is_staff'
            })
        },
        methods: {
            ...mapActions({
                get_user: types.GET_USER
            })
        }
    }
</script>
