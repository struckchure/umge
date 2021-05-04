<template>
    <Base>
        <template v-slot:main>
            <div class="row">
                <div class="col s12 m6 l6">
                    <div class="w-full bg-gray-100 my-1 rounded-3xl p-8 my-3">
                        <label class="text-right italic">Your balance</label>
                        <p class="wallet-preview-balance text-right">
                            &#8358; {{ user.wallet.wallet_balance }}
                        </p>
                    </div>

                    <ItemListContainer class="bg-gray-100 h-80 overflow-hide-scroll overflow-auto w-full rounded-3xl pt-0 py-8 px-6">
                        <WalletHistory
                            v-for="history in histories"
                            :key="history.id"
                            :history="history"
                        />
                    </ItemListContainer>
                </div>

                <div class="col s12 m6 l6">
                    <div class="w-full bg-gray-100 my-1 rounded-3xl p-8 my-3">
                        <div class="form-header">
                            Fund wallet
                        </div>

                        <form @submit.prevent="fund_wallet">
                            <div class="row">
                                <div class="col s12 m12 l12">
                                    <label class="text-left font-extrabold">Amount</label>
                                    <div class="w-full">
                                        <input
                                            type="number"
                                            class="w-inherit rounded bg-gray-400 p-2 px-4"
                                            min="100"
                                            v-model="amount"
                                        />
                                    </div>
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
    import { mapGetters, mapActions, mapMutations } from 'vuex'

    import '@/assets/css/grid.css'
    import '@/assets/css/wallet.css'

    import WalletHistory from '@/components/accounts/WalletHistory.vue'

    export default {
        name: 'Wallet',
        props: [
            'reference'
        ],
        components: {
            WalletHistory
        },
        title () {
            return 'Dashboard | Wallet'
        },
        data () {
            return {
                amount: 100
            }
        },
        mounted () {
            this.get_user()
            this.get_fund_history()
        },
        computed: {
            ...mapGetters({
                user: 'get_user',
                error: 'get_error',
                fund: 'get_fund',
                histories: 'get_fund_history'
            }),
            get_reference() {
                return this.$route.query.reference
            }
        },
        methods: {
            ...mapActions({
                get_user: types.GET_USER,
                fund_user_wallet: types.FUND_WALLET,
                get_fund_history: types.GET_WALLET_FUND_HISTORY
            }),
            ...mapMutations({
                set_success: types.SET_SUCCESS
            }),
            fund_wallet () {
                const payload = {
                    amount: this.amount
                }

                this.fund_user_wallet(payload)

                const success_payload = {
                    'success': this.fund[2].message
                }

                this.set_success(success_payload)
                setTimeout(
                    () => {
                        var next_url = this.fund[2].data.authorization_url
                        window.location.replace(next_url)
                    },
                    3000
                )
            }
        }
    }
</script>
