import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store/index.js'

import Home from '@/views/Home.vue'

import Logout from '@/views/accounts/Logout.vue'
import Login from '@/views/accounts/Login.vue'
import Register from '@/views/accounts/Register.vue'
import Profile from '@/views/accounts/Profile.vue'
import Wallet from '@/views/accounts/Wallet.vue'

import Cart from '@/views/cart/Cart.vue'

import Store from '@/views/store/Store.vue'
import StoreCreate from '@/views/store/StoreCreate.vue'

import AdminHome from '@/views/admin/AdminHome.vue'
import AdminOrders from '@/views/admin/AdminOrders.vue'
import AdminRiders from '@/views/admin/AdminRiders.vue'
import AdminRidersApplications from '@/views/admin/AdminRidersApplications.vue'
import AdminLocations from '@/views/admin/AdminLocations.vue'

import Orders from '@/views/delivery/Orders.vue'
import RiderOrders from '@/views/delivery/RiderOrders.vue'
import RiderTasks from '@/views/delivery/RiderTasks.vue'
import RiderHistory from '@/views/delivery/RiderHistory.vue'


Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/accounts/logout/',
        name: 'Logout',
        component: Logout
    },
    {
        path: '/accounts/login/',
        name: 'Login',
        component: Login
    },
    {
        path: '/accounts/register/',
        name: 'Register',
        component: Register
    },
    {
        path: '/accounts/cart/',
        name: 'Cart',
        component: Cart,
        meta: {
            requiresLogin: true
        }
    },
    {
        path: '/accounts/profile/',
        alias: '/accounts/',
        name: 'Profile',
        component: Profile,
        meta: {
            requiresLogin: true
        }
    },
    {
        path: '/accounts/wallet/',
        name: 'Wallet',
        component: Wallet,
        props: route => ({ query: route.query.q }),
        meta: {
            requiresLogin: true
        }
    },
    {
        path: '/store/new/',
        name: 'StoreCreate',
        component: StoreCreate,
        meta: {
            requiresLogin: true
        }
    },
    {
        path: '/store/:store_slug/',
        name: 'Store',
        component: Store,
        props: true
    },
    {
        path: '/admin/',
        name: 'AdminHome',
        component: AdminHome,
        meta: {
            requiresLogin: true,
            requiresAdmin: true
        }
    },
    {
        path: '/admin/orders/',
        name: 'AdminOrders',
        component: AdminOrders,
        meta: {
            requiresLogin: true,
            requiresAdmin: true
        }
    },
    {
        path: '/admin/riders/',
        name: 'AdminRiders',
        component: AdminRiders,
        meta: {
            requiresLogin: true,
            requiresAdmin: true
        }
    },
    {
        path: '/admin/locations/',
        name: 'AdminLocations',
        component: AdminLocations,
        meta: {
            requiresLogin: true,
            requiresAdmin: true
        }
    },
    {
        path: '/admin/riders/orders/',
        name: 'RiderOrders',
        component: RiderOrders,
        meta: {
            requiresLogin: true,
            requiresStaff: true
        }
    },
    {
        path: '/admin/riders/tasks/',
        name: 'RiderTasks',
        component: RiderTasks,
        meta: {
            requiresLogin: true,
            requiresStaff: true
        }
    },
    {
        path: 'admin/riders/history/',
        name: 'RiderHistory',
        component: RiderHistory,
        meta: {
            requiresLogin: true,
            requiresStaff: true
        }
    },
    {
        path: '/admin/riders/applications/',
        name: 'AdminRidersApplications',
        component: AdminRidersApplications,
        meta: {
            requiresLogin: true,
            requiresAdmin: true
        }
    },
    {
        path: '/delivery/orders/',
        name: 'Orders',
        component: Orders,
        meta: {
            requiresLogin: true
        }
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})


router.beforeEach((to, from, next) => {
    const isAuthenticated = store.getters.is_authenticated
    const isAdmin = store.getters.is_admin
    const isStaff = store.getters.is_staff

    if (to.meta.requiresLogin === true && !isAuthenticated) {
        next({ name: 'Login' })
    } else {
        next()
    }

    if (to.meta.requiresAdmin === true && !isAdmin) {
        next({ name: 'Home' })
    } else {
        next()
    }

    if (to.meta.requiresStaff === true && !isStaff) {
        next({ name: 'Home' })
    } else {
        next()
    }
})

export default router
