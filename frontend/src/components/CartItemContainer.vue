<template>
	<div class="cart-item-container">
		<div class="cart-item-container-title">
			Shopping Cart
			<p>You have {{ items.length }} items in your cart</p>
		</div>
		<CartItem
			v-for="item in items"
			:key="item.name"
			:item="item"
		/>
	</div>
</template>

<script>
	import '@/assets/css/cart.css'
	import CartItem from '@/components/CartItem.vue'

	export default {
		name: 'CartItemContainer',
		props: [
			'items'
		],
		components: {
			CartItem
		}
	}
</script>
