<template>
    <Base current_page="Products" page_title="Products">
        <div class="row">
            <div
                class="col s12 m6 l4"
                v-for="(item, index) in products"
                :key="index"
            >
                <Product
                    :item="item"
                    :index="index"
                />
            </div>
        </div>

        <template v-slot:extra>
            <form class="no-border filter-form" @submit.prevent="filter_product_list">
                <div class="row">
                    <div class="col s12 m12 l12">
                        <select
                            v-model="filters.store_name"
                            @change="filter_product_list()"
                            class="appearance-none bg-white text-black"
                        >
                            <option value="*">All stores (default)</option>
                            <option
                                v-for="(store, index) in stores"
                                :key="index"
                            >{{ store.store_name }}</option>
                        </select>
                    </div>

                    <div class="col s12 m12 l12">
                        <input
                            type="text"
                            v-model="filters.product_name"
                            placeholder="search ..."
                            @input="filter_product_list()"
                            class="bg-white text-white w-full input-diff"
                        />
                    </div>
                </div>

                <label>showing {{ products.length }} product(s)</label>
            </form>
        </template>
    </Base>
</template>

<script>
    import Product from '@/components/products/Product.vue'
    import { mapGetters, mapActions } from 'vuex'
    import * as types from '@/store/types.js'

    export default {
        components: {
            Product
        },
        title () {
            return 'Home | Products'
        },
        data () {
            return {
                filters: {
                    store_name: '*',
                    product_name: ''
                }
            }
        },
        mounted () {
            this.filter_product_list()
        },
        computed: {
            ...mapGetters({
                products: 'get_products',
                stores: 'get_stores'
            })
        },
        methods: {
            ...mapActions({
                get_products_request: types.GET_PRODUCT_LIST,
                get_store_list: types.GET_STORE_LIST
            }),
            filter_product_list() {
                var store_name = this.filters.store_name
                var product_name = this.filters.product_name

                if (this.filters.store_name.length == 0) {
                    store_name = '*'
                }

                if (this.filters.product_name.length == 0) {
                    product_name = '*'
                }

                const filters = {
                    store_name,
                    product_name
                }

                this.get_products_request(filters)
                this.get_store_list()
            }
        }
    }
</script>

<style scoped>
    form {
        justify-content: center;
        padding: 0;
    }

    button.filter-button {
        max-width: 220px !important;
        padding: .6em;
        align-self: flex-end;
        background-color: red;
    }

    button.form-filter {
        width: 200px;
        align-self: flex-start;
    }

    button.form-filter:hover {
        background-color: rgba(0, 0, 0, 0.5);
    }

    .input-field {
        padding: 0;
    }

    select, input {
        padding: .6em;
        border-radius: .3em !important;
        margin: .2em 0;
        width: 90% !important;
        float: right;
    }

    .input-diff {
        background-color: white !important;
        color: black !important;
    }

    @media only screen and (max-width: 600px) {
        select {
            width: 90% !important;
        }

        select, input {
            float: left;
        }

        * {
            font-size: auto;
        }
    }
</style>
