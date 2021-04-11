<template>
    <div class="product">
        <div class="modal" :id="product_id">
            <div class="modal-tools">
                <button @click="close_modal(product_id)" class="modal-close">&times;</button>
            </div>
            <ProductPreferenceForm :item="item" />
        </div>

        <div class="product-tools">
            <button @click="show_modal(product_id)">
                Buy now
            </button>

            <button @click="show_modal(product_id)">
                <i class="fas fa-cart-plus  "></i>
            </button>
        </div>

        <div class="product-image">
            <img class="elevation-3" :src="item.product_image">
        </div>

        <div class="product-details">
            <label class="store">{{ item.product_store.store_name }}</label>
            <p class="product-description">{{ item.product_name }}</p>
            <label class="product-price">&#8358; {{ item.product_price }}</label>
        </div>
    </div>
</template>

<script>
    import ProductPreferenceForm from '@/components/ProductPreferenceForm.vue'

    import '@/assets/css/modal.css'
    import * as _modal from '@/assets/js/modal.js'

    export default {
        name: 'Product',
        props: [
            'item', 'index'
        ],
        mounted() {},
        components: {
            ProductPreferenceForm
        },
        data () {
            return {}
        },
        computed: {
            product_id () {
                return this.index
            }
        },
        methods: {
            show_modal: _modal.show_modal,
            close_modal: _modal.close_modal
        }
    }
</script>
