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

        <form @submit.prevent="pay_now">
            {{ current_location.coords.latitude }}
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
                    <button style="background-color: #d97706 !important;" type="submit">Pay now</button>
                </div>
            </div>
        </form>
    </div>
</template>

<script>
    import { mapGetters, mapActions, mapMutations } from 'vuex'
    import * as types from '@/store/types.js'

    export default {
        name: 'CarForm',
        props: [
            'cart',
            'user'
        ],
        mounted () {
            this.locateMe();
        },
        data () {
            return {
                payment_method: 'CARD',
                current_location: {},
                gettingLocation: false,
                errorStr:null
            }
        },
        computed: {
            ...mapGetters({
                purchase: 'get_purchase'
            }),
            get_payment_mode_name () {
                let name;

                switch (this.payment_method) {
                    case 'CARD':
                        name = 'card';
                        break;
                    case 'WALLET':
                        name = 'wallet';
                        break;
                }

                return name;
            },
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
            ...mapActions({
                checkout: types.CHECKOUT_CART
            }),
            ...mapMutations({
                set_success: types.SET_SUCCESS
            }),
            async getLocation() {
                return new Promise(
                    (resolve, reject) => {
                    if(!("geolocation" in navigator)) {
                        reject(new Error('Geolocation is not available.'));
                    }

                    navigator.geolocation.getCurrentPosition(
                        pos => {
                            resolve(pos);
                        },
                        err => {
                            reject(err);
                        }
                    );
                });
            },
            async locateMe() {
                this.gettingLocation = true;
                try {
                    this.gettingLocation = false;
                    this.current_location = await this.getLocation();
                } catch(e) {
                    this.gettingLocation = false;
                    this.errorStr = e.message;
                }
            },
            pay_now() {
                const payload = {
                    payment_mode: this.get_payment_mode_name.toUpperCase(),
                    cart_location: {
                        latitude: this.current_location.coords.latitude,
                        longitude: this.current_location.coords.longitude
                    }
                }

                this.checkout(payload)

                if (this.payment_mode == 'C') {
                    const success_payload = {
                        'success': this.purchase.response.data.message
                    }

                    this.set_success(success_payload)

                    setTimeout(
                        () => {
                            var next_url = this.purchase.response.data.authorization_url
                            window.location.replace(next_url)
                        },
                        500
                    )
                }
            },
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
