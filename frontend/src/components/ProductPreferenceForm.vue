<template>
	<div class="modal-content">
		<div class="modal-header">
			<label class="product-preference-title">
				Preference / {{ item.product_store.store_name }} / {{ item.product_name }}
			</label>
		</div>

		<div class="modal-body">
			<form class="product-preference" @submit.prevent="add_to_cart()">
				<div class="row">
					<div class="col s12 m12 l12">
						<label class="text-left w-100">Description</label>
						<div class="input-field">
							<textarea
								type="text"
								placeholder="add extra description here ..."
								v-model="description"
								style="color: white !important"
							/>
						</div>
					</div>

					<div class="col s2 m2 l2">
						<label class="text-left w-100">Quantity</label>
						<div class="input-field">
							<input type="number" min="1" v-model="qty"/>
						</div>
					</div>

					<div class="col push-s10 push-m10 push-l10"></div>

					<div class="col s12 m12 l12">
						<div class="product-amount-details">
							<div class="row">
								<div class="col s12 m12 l12 amount-details">
									<label>Price</label>
									<label>&#8358; {{ item.product_price }}</label>
								</div>

								<div
									class="col s12 m12 l12 amount-details"
									v-for="(option, index) in options"
									:key="index"
								>
									<label>{{ option.option_name }}</label>
									<label>&#8358; {{ option.option_price }}</label>
								</div>

								<div
									class="col s12 m12 l12 amount-details"
									style="border-top: 1px solid #eee; padding-top: .5em; margin-top: .5em">
									<label>Total</label>
									<label>&#8358; {{ get_total_amount }}</label>
								</div>
							</div>
						</div>
					</div>

					<div class="col s12 m12 l12 options">
						<div class="row">
							<div
								class="col s6 m6 l6"
								v-for="(option, index) in get_options"
								:key="index"
							>
								<div class="input-field">
									<input
										type="checkbox"
										@change="add_option(option)"
									/>
									<label class="text-left">
										&#8358; {{ option.option_price }} {{ option.option_name }}
									</label>
								</div>
							</div>
						</div>
					</div>

					<div class="col s12 m12 l12">
						<button @submit.prevent="add_to_cart()">Proceed</button>
					</div>
				</div>
			</form>
		</div>
	</div>
</template>

<script>
	import '@/assets/css/product.css'

	export default {
		name: 'ProductPreferenceForm',
		props: [
			'id',
			'item'
		],
		data () {
			return {
				qty: 1,
				description: '',
				options: {},
				total_amount: 0
			}
		},
		computed: {
			get_options () {
				return this.item.product_options
			},
			get_total_amount () {
				var total_amount = this.total_amount + this.item.product_price

				return total_amount
			}
		},
		methods: {
			add_option (option) {
				var option_keys = Object.keys(this.options)
				var key = option.option_slug

				if (option_keys.indexOf(key) > -1) {
					this.total_amount -= option.option_price // deduct option price
					delete this.options[key] // remove option from cart options
				} else {
					this.total_amount += option.option_price // add option price
					this.options[key] = option // add option to cart option
				}
			},
			add_to_cart () {}
		}
	}
</script>
