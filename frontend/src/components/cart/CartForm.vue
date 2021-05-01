<template>
	<div class="cart-form">
		<div class="cart-form-header">
			<p class="title">Payment method</p>
			<div class="rounded-full user-image">
				<img src="@/assets/img/bg-1.jpg" class="rounded-full">
			</div>
		</div>

		<div class="payment-method">
			<button class="bg-yellow-600" @click="choose_payment_method()">Pay with {{ alternate_method }}</button>
		</div>

		<form @submit.prevent="pay_now()">
			<div class="row">
				<div class="col s12 m12 l12 input-field">
					<input type="email" v-model="user.email" placeholder="email" :disabled="disable_card" />
				</div>

				<div class="col s12 m12 l12 input-field">
					<input type="number" readonly placeholder="amount" v-model="total" :disabled="disable_card" />
				</div>

				<div class="col s12 m12 l12">
					<div class="divider"></div>
				</div>

				<div class="col s12 m12 l12">
					<div class="pricing">
						<div class="price-item">
							<label>Sub total</label>
							<label>&#8358; {{ subtotal }}</label>
						</div>

						<div class="price-item">
							<label>Delivery</label>
							<label>&#8358; {{ delivery_price }}</label>
						</div>

						<div class="price-item">
							<label>Total</label>
							<label>&#8358; {{ total }}</label>
						</div>
					</div>
				</div>

				<div class="col s12 m12 l12">
					<button class="bg-yellow-600" type="submit">Pay now</button>
				</div>
			</div>
		</form>
	</div>
</template>

<script>
	export default {
		name: 'CarForm',
		props: [
			'cart',
			'user'
		],
		data () {
			return {
				payment_method: 'CARD'
			}
		},
		computed: {
			subtotal () {
				var _subtotal = this.cart.cart_total_balance

				return _subtotal
			},
			delivery_price () {
				return this.cart.cart_delivery_charges
			},
			total () {
				return this.subtotal + this.delivery_price
			},
			disable_card() {
				if (this.payment_method === 'CARD') {
					return false
				} else {
					return true
				}
			},
			alternate_method () {
				var method = this.payment_method

				switch (this.payment_method) {
					case 'CARD':
						method = 'WALLET'
						break;
					case 'WALLET':
						method = 'CARD'
						break;
				}

				return method.toLowerCase()
			}
		},
		methods: {
			pay_now () {},
			choose_payment_method () {
				switch (this.payment_method) {
					case 'CARD':
						this.payment_method = 'WALLET'
						break;
					case 'WALLET':
						this.payment_method = 'CARD'
						break;
				}
			}
		}
	}
</script>
