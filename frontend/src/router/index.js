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

import Orders from '@/views/delivery/Orders.vue'

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
})

export default router
