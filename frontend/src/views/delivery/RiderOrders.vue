<template>
	<Base>
		<template v-slot:main>
			<RiderOrdersContainer>
				<RiderOrder
					v-for="(order, index) in orders"
					:key="index"
					:order="order"
				/>
			</RiderOrdersContainer>
		</template>
	</Base>
</template>

<script>
	import RiderOrdersContainer from '@/components/delivery/RiderOrdersContainer.vue'
	import RiderOrder from '@/components/delivery/RiderOrder.vue'

	import * as types from '@/store/types.js'
	import { mapGetters, mapActions } from 'vuex'

	import '@/assets/css/grid.css'
	import '@/assets/css/delivery.css'

	export default {
		name: 'RiderOrders',
		title () {
			return 'Riders | Orders'
		},
		mounted() {
			this.get_orders()
		},
		components: {
			RiderOrdersContainer,
			RiderOrder
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
