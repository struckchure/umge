<template>
	<div class="rider-order">
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
	</div>
</template>

<script>
	export default {
		name: 'RiderOrder',
		props: [
			'order'
		]
	}
</script>