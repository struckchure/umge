<template>
	<Base>
		<template v-slot:main>
			<div class="row">
				<div class="col s12 m12 l7">
					<CartItemContainer
						:items="cart_items"
					/>
				</div>

				<div class="col s12 m12 l5">
					<CartForm
						:cart="cart"
						:user="user"
					/>
				</div>
			</div>
		</template>
	</Base>
</template>

<script>
	import '@/assets/css/cart.css'
	import CartForm from '@/components/cart/CartForm.vue'
	import CartItemContainer from '@/components/cart/CartItemContainer.vue'

	import * as types from '@/store/types.js'
	import { mapGetters, mapActions } from 'vuex'

	export default {
		name: 'Cart',
		title () {
			return 'Dashboard | Cart'
		},
		components: {
			CartForm,
			CartItemContainer
		},
		mounted () {
			this.get_cart()
		},
		computed: {
			...mapGetters({
				cart: 'get_cart',
				user: 'get_user'
			}),
			cart_items () {
				return this.cart.cart_items
			}
		},
		methods: {
			...mapActions({
				get_cart: types.GET_CART
			})
		}
	}
</script>
