<template>
    <Base>
        <template v-slot:main>
            <div class="row">
                <div class="col s12 m12 l12">
                    <AdminRidersList :riders="riders" />
                </div>
            </div>
        </template>
    </Base>
</template>

<script>
    import * as types from '@/store/types.js'
    import { mapGetters, mapActions } from 'vuex'

    import AdminRidersList from '@/components/admin/AdminRidersList.vue'

    export default {
        name: "AdminRiders",
        title () {
            return 'UMGE | Managment | Riders'
        },
        components: {
            AdminRidersList
        },
        mounted () {
            this.get_riders()
        },
        computed: {
            ...mapGetters({
                riders: 'get_riders'
            })
        },
        methods: {
            ...mapActions({
                get_riders: types.GET_ADMIN_RIDERS_LIST
            })
        }
    }
</script>
