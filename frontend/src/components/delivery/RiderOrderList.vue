<template>
	<div class="overflow">
		<RiderOrderDetails
			:order="current_order"
		/>

		<table>
			<thead>
				<tr>
					<td class="w-3">#</td>
					<td>Items</td>
					<td>Location</td>
					<td class="w-10">Action</td>
				</tr>
			</thead>

			<tbody>
				<tr
					v-for="(order, index) in orders"
					:key="index"
					class="hover:bg-gray-400 hover:text-white cursor-pointer h-8 p-1"
				>
					<td>{{ index + 1 }}</td>
					<td>{{ order.orders.length }} available for delivery</td>
					<td>School</td>
					<td>
						<button
							@click="check_details(order)"
							class="text-sm m-0 px-5 w-auto md:w-auto bg-red-500 hover:red-400"
						>
							Accept
							<i class="fas fa-check mx-2"></i>
						</button>
					</td>
				</tr>
			</tbody>
		</table>
	</div>
</template>

<script>
	import RiderOrderDetails from '@/components/delivery/RiderOrderDetails.vue'

	export default {
		name: 'RiderOrder',
		props: [
			'orders'
		],
		components: {
			RiderOrderDetails
		},
		data () {
			return {
				current_order: {}
			}
		},
		methods: {
			check_details (order) {
				this.current_order = order
			}
		}
	}
</script>
