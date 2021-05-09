<template>
	<div>
		<table>
			<thead>
				<tr>
					<td>#</td>
					<td>Transaction ID</td>
					<td>Location</td>
					<td>Action</td>
				</tr>
			</thead>

			<tbody>
				<tr v-for="(order, index) in orders" :key="index">
					<td>{{ index + 1 }}</td>
					<td>{{ order.transaction_id }}</td>
					<td>School</td>
					<td>
						<button class="btn-small w-20 bg-red-500 hover:red-400">Accept</button>
					</td>
				</tr>
			</tbody>
		</table>
	</div>
<!-- 	<div class="rider-order">
		<div class="order-image pa-1">
			<img :src="order.item.cart_item.product_image"/>
		</div>

		<div class="order w-30">
			<div class="">
				<p class="text-wrap">
					{{ order.transaction_id }}
				</p>
			</div>

			<div class="order-tool">
				<button class="success">Accept</button>
				<button class="primary">Details</button>
			</div>
		</div>

		<div class="order-description w-100">
			<p class="text-center">
				{{ order.item.cart_item.product_name }}
			</p>

			<label class="text-center form-header">
				&#8358; {{ order.item.cart_item.product_price }}
			</label>

			<label>
				qty: {{ order.item.cart_item_quantity }}
			</label>
		</div>
	</div> -->
</template>

<script>
	export default {
		name: 'RiderOrder',
		props: [
			'orders'
		]
	}
</script>