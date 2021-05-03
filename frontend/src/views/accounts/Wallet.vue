<template>
    <Base>
        <template v-slot:main>
            <div class="row">
                <div class="col s12 m4 m4">
                    <div class="w-full bg-gray-100 my-1 rounded-3xl p-8 my-3">
                        <p class="wallet-preview-balance text-right">
                            &#8358; {{ user.wallet.wallet_balance }}
                        </p>
                    </div>

                    <div class="bg-gray-100 w-full h-full rounded-3xl p-8 overflow-auto">
                        <p>
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
                            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
                            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
                            consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
                            cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
                            proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                        </p>
                    </div>
                </div>

                <div class="col s12 m8 m8">
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

    export default {
        name: 'Wallet',
        props: [
            'reference'
        ],
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
        },
        computed: {
            ...mapGetters({
                user: 'get_user',
                fund: 'get_fund',
                error: 'get_error'
            }),
            get_reference() {
                return this.$route.query.reference
            }
        },
        methods: {
            ...mapActions({
                get_user: types.GET_USER,
                fund_user_wallet: types.FUND_WALLET
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
