<template>
	<Base>
		<template v-slot:main>
			<div class="row">
				<div class="col s12 m12 l12">
					<label class="form-header">
						Management / Stores
					</label>
				</div>

				<div class="col s12 m12 l12">
					<AdminStoresList :stores="stores" />
				</div>
			</div>
		</template>
	</Base>
</template>

<script>
	import AdminStoresList from '@/components/admin/AdminStoresList.vue'
	import * as types from '@/store/types.js'
	import { mapGetters, mapActions } from 'vuex'

	export default {
		name: 'AdminStores',
		components: {
			AdminStoresList
		},
		computed: {
			...mapGetters({
				stores: 'get_store_orders'
			})
		},
		methods: {
			...mapActions({
				get_store_orders: types.GET_STORE_ORDERS
			})
		},
		mounted () {
			this.get_store_orders()
		}
	}
</script>
