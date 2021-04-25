<template>
    <Base>
        <template v-slot:main>
            <div class="row">
                <div class="col s12 m4 m4">
                    <div class="wallet-preview">
                        <p class="wallet-preview-balance text-right">
                            &#8358; {{ user.wallet.wallet_balance }}
                        </p>

                        <div class="extra-details">
                            <label class="text-left">Cards</label>
                            <br>
                            <div class="wallet-card">
                                <p class="text-right">
                                    **** 345627
                                </p>
                                <label class="text-right">
                                    John Doe
                                </label>

                                <div class="divider"></div>

                                <div class="flex flex-center">
                                    <button class="success btn-small flex-1">
                                        <i class="fas fa-edit"></i>
                                    </button>
                                    <button class="danger btn-small flex-1">
                                        <i class="fas fa-trash"></i>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col s12 m8 m8">
                    <div class="wallet-update">
                        <div class="form-header">
                            Fund wallet
                        </div>

                        <form @submit.prevent="fund_wallet()">
                            <div class="row">
                                <div class="col s12 m12 l12">
                                    <label class="form-label text-left">Card number</label>
                                </div>

                                <div class="col s12 m12 l12">
                                    <input
                                        type="number"
                                        placeholder="XXXX **** XXXX"
                                        required
                                    />
                                </div>

                                <div class="col s12 m12 l12">
                                    <label class="form-label text-left">Card details</label>
                                </div>

                                <div class="col s12 m4 l4">
                                    <input
                                        type="number"
                                        placeholder="CVV"
                                        max="3"
                                        required
                                    />
                                </div>

                                <div class="col s12 l4 l4">
                                    <input
                                        type="number"
                                        placeholder="MM / YY"
                                        required
                                    />
                                </div>

                                <div class="col s12 m12 l12">
                                    <label class="form-label text-left">Card holder</label>
                                </div>

                                <div class="col s12 m12 l12">
                                    <input
                                        type="number"
                                        placeholder="John Doe"
                                        required
                                    />
                                </div>

                                <div class="col s12 m12 l12">
                                    <label class="form-label text-left">Amount</label>
                                </div>

                                <div class="col s12 m12 l12">
                                    <input
                                        type="number"
                                        placeholder="1000"
                                        min="100"
                                        required
                                    />
                                </div>
                            </div>

                            <button type="submit">Pay now</button>
                        </form>
                    </div>
                </div>
            </div>
        </template>
    </Base>
</template>

<script>
    import * as types from '@/store/types.js'
    import { mapGetters, mapActions } from 'vuex'

    import '@/assets/css/grid.css'
    import '@/assets/css/wallet.css'

    export default {
        name: 'Wallet',
        title () {
            return 'Dashboard | Wallet'
        },
        mounted () {
            this.get_user()
        },
        computed: {
            ...mapGetters({
                user: 'get_user'
            })
        },
        methods: {
            ...mapActions({
                get_user: types.GET_USER
            }),
            fund_wallet () {}
        }
    }
</script>