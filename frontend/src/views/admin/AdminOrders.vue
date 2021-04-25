<template>
	<Base>
		<template v-slot:main>
			<label class="form-header">
				Management / Orders
			</label>

			<div class="row">
				<div class="col s12 m12 l12">
					<AdminOrdersList :orders="orders" />
				</div>
			</div>
		</template>
	</Base>
</template>

<script>
	import * as types from '@/store/types.js'
    import { mapGetters, mapActions } from 'vuex'

    import AdminOrdersList from '@/components/admin/AdminOrdersList.vue'

	export default {
		name: 'AdminOrders',
		components: {
            AdminOrdersList
        },
		mounted () {
            this.get_orders()
        },
        computed: {
            ...mapGetters({
                orders: 'get_orders'
            })
        },
        methods: {
            ...mapActions({
                get_orders: types.GET_ORDERS
            })
        }
	}
</script>
