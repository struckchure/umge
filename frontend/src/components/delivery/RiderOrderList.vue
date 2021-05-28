<template>
	<div class="overflow">
		<table>
			<thead>
				<tr>
					<td class="w-3">#</td>
					<td>Items</td>
					<td>Status</td>
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
					<td>{{ order.transaction_id }} available for delivery to {{ order.user.username }}</td>
					<td>
                        <label class="w-11 p-2 text-white rounded" :class="order_color(order.status)">
                            <i :class="order_icon(order.status)"></i>
                        </label>
                    </td>
					<td>{{ order.location }}</td>
					<td>
						<button
							@click="rider_accept_order(order)"
							class="text-sm m-0 px-5 w-auto md:w-auto bg-red-500 hover:red-400"
							v-if="order.status == 'PD'"
						>
							Accept
							<i class="fas fa-check mx-2"></i>
						</button>

						<button
							class="text-sm m-0 px-5 w-auto md:w-auto bg-green-500 hover:green-400"
							v-else
						>
							Accepted
							<i class="fas fa-check mx-2"></i>
						</button>
					</td>
				</tr>
			</tbody>
		</table>
	</div>
</template>

<script>
	import { mapActions } from 'vuex'
	import * as types from '@/store/types.js'
	import { order_color, order_icon } from '@/store/utils.js'

	export default {
		name: 'RiderOrder',
		props: [
			'orders'
		],
		methods: {
			...mapActions({
				'accept_order': types.RIDER_ACCEPT_DELIVERY
			}),
			rider_accept_order (order) {
				const payload = {
					username: order.user.username
				}
				this.accept_order(payload)
			},
			order_color,
			order_icon
		}
	}
</script>
