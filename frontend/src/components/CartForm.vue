<template>
	<div class="cart-form">
		<div class="cart-form-header">
			<p class="title">Payment method</p>
			<div class="user-image">
				<img src="@/assets/img/bg-1.jpg">
			</div>
		</div>

		<div class="payment-method">
			<button @click="choose_payment_method()">Pay with {{ alternate_method }}</button>
		</div>

		<form @submit.prevent="pay_now()">
			<div class="row">
				<div class="col s12 m12 l12 input-field">
					<input type="text" placeholder="cardholder" :disabled="disable_card" />
				</div>

				<div class="col s12 m12 l12 input-field">
					<input type="number" placeholder="XXXX **** XX" :disabled="disable_card" />
				</div>

				<div class="col s12 m12 l12 input-field">
					<input type="number" placeholder="MM/YY" :disabled="disable_card" />
				</div>

				<div class="col s12 m12 l12 input-field">
					<input type="number" placeholder="CVV" :disabled="disable_card" />
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
					<button>Pay now</button>
				</div>
			</div>
		</form>
	</div>
</template>

<script>
	export default {
		name: 'CarForm',
		data () {
			return {
				payment_method: 'card',
				delivery_price: 50,
			}
		},
		computed: {
			subtotal () {
				return 1000
			},
			total () {
				return this.subtotal + this.delivery_price
			},
			disable_card() {
				if (this.payment_method === 'card') {
					return false
				} else {
					return true
				}
			},
			alternate_method () {
				var method = this.payment_method

				switch (this.payment_method) {
					case 'card':
						method = 'wallet'
						break;
					case 'wallet':
						method = 'card'
						break;
				}

				return method
			}
		},
		methods: {
			pay_now () {},
			choose_payment_method () {
				switch (this.payment_method) {
					case 'card':
						this.payment_method = 'wallet'
						break;
					case 'wallet':
						this.payment_method = 'card'
						break;
				}
			}
		}
	}
</script>
