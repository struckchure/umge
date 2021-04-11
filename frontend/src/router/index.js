import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '@/views/Home.vue'

import Login from '@/views/accounts/Login.vue'
import Register from '@/views/accounts/Register.vue'
import Cart from '@/views/accounts/Cart.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
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
        component: Cart
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
