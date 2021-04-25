<template>
    <div></div>
</template>

<script>
    import * as types from '@/store/types.js'
    import { mapActions } from 'vuex'

    export default {
        name: 'Logout',
        title () {
            return 'Logout'
        },
        mounted () {
            this.logout_user()
        },
        methods: {
            ...mapActions({
                logout: types.AUTH_LOGOUT
            }),
            logout_user () {
                this.logout()
                setTimeout(
                    () => {
                        this.$router.push({ name: 'Login' })
                    },
                    100
                )
            }
        }
    }
</script>
