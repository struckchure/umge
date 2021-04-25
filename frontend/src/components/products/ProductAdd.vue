<template>
    <div class="modal-content">
        <div class="modal-header">
            <label class="product-preference-title">
                Product / Add /
            </label>
        </div>

        <div class="modal-body pa-1">
            <form class="product-preference" @submit.prevent="add_product" enctype="multipart/form-data">
                <div class="row">
                    <div class="col s12 m12 l12">
                        <label class="form-header text-left">Product name</label>
                    </div>

                    <div class="col s12 m12 l12">
                        <input type="text" v-model="product_name" required maxlength="70" placeholder="product name" />
                    </div>

                    <div class="col s12 m12 l12">
                        <label class="form-header text-left">Product image</label>
                    </div>

                    <div class="col s12 m12 l12">
                        <input type="file" ref="product_image" required @change="handleUpload" />
                    </div>

                    <div class="col s12 m12 l12">
                        <label class="form-header text-left">Product price</label>
                    </div>

                    <div class="col s12 m12 l12">
                        <input type="number" v-model="product_price" required maxlength="5" placeholder="product price" />
                    </div>

                    <div class="col s10 m10 l10">
                        <label class="form-header text-left">Product options</label>
                    </div>

                    <div class="col s2 m2 l2">
                        <button type="normal" @click="add_option" class="btn btn-small">
                            <i class="fas fa-plus"></i>
                        </button>
                    </div>

                    <div class="col s12 m12 l12">
                        <div class="row">
                            <div
                                class="col s12 m12 l12"
                                v-for="(option, index) in product_options"
                                :key="index"
                            >
                                <div class="disp-flex-v space-between">
                                    <input type="checkbox" class="pa-1 small" />
                                    <input type="text" class="pa-1 small" v-model="option.option_name" />
                                    <input type="number" class="pa-1 small" v-model="option.option_price" />
                                    <button class="btn-small danger">
                                        <i class="fas fa-trash"></i>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="col s12 m12 l12">
                        <button type="submit">Save Product</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
    import '@/assets/css/product.css'

    import * as types from '@/store/types.js'
    import { mapGetters, mapActions } from 'vuex'

    export default {
        name: 'ProductAdd',
        props: [
            'store_slug'
        ],
        data () {
            return {
                product_name: '',
                product_image: '',
                product_price: '',
                product_options: [
                    {
                        option_name: 'option 1',
                        option_price: 100
                    }
                ]
            }
        },
        mounted () {
            this.get_store(this.store_slug)
        },
        computed: {
            ...mapGetters({
                error: 'get_error' ,
                store: 'get_store'
            }),
            get_options () {
                return this.product_options
            },
            get_store_id () {
                return this.store.id
            }
        },
        methods: {
            ...mapActions({
                create_product: types.CREATE_PRODUCT,
                get_store: types.GET_STORE,
                get_store_products: types.GET_STORE_PRODUCTS
            }),
            add_product() {
                const payload = {
                    product_store: this.get_store_id,
                    product_name: this.product_name,
                    product_image: this.product_image,
                    product_price: this.product_price,
                    // product_options: this.product_options
                }

                this.create_product(payload)
                this.get_store_products(this.store.store_slug)
            },
            add_option () {
                const option = {}

                this.options.add(option)
            },
            handleUpload (event) {
                this.product_image = event.target.files[0]
            }
        }
    }
</script>
