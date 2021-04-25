<template>
	<div class="row">
		<div
			class="col s12 m12 l4"
			v-for="(product, index) in products"
			:key="index"
		>
			<StoreProduct
				:item="product"
				:index="index"
			/>
		</div>
	</div>
</template>

<script>
	import StoreProduct from '@/components/store/StoreProduct.vue'

	import { mapGetters, mapActions } from 'vuex'
	import * as types from '@/store/types.js'

	export default {
		name: 'StoreProductList',
		props: [
			'store_slug'
		],
		components: {
			StoreProduct
		},
		mounted () {
			this.get_store_products(this.store_slug)
		},
		computed: {
			...mapGetters({
				products: 'get_store_products'
			})
		},
		methods: {
			...mapActions({
				get_store_products: types.GET_STORE_PRODUCTS
			})
		}
	}
</script>
