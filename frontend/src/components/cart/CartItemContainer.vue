<template>
	<div class="cart-item-container">
		<div class="cart-item-container-title">
			Shopping Cart
			<p>You have {{ items.length }} items in your cart</p>
		</div>
		<CartItem
			v-for="item in items"
			:key="item.id"
			:item="item"
		/>
	</div>
</template>

<script>
	import CartItem from '@/components/cart/CartItem.vue'

	export default {
		name: 'CartItemContainer',
		props: [
			'items'
		],
		computed: {
			get_cart_items () {
				return this.items
			}
		},
		components: {
			CartItem
		}
	}
</script>
