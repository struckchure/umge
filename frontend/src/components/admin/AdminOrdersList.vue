<template>
    <div class="overflow h-screen">
        <table>
            <thead>
                <tr>
                    <td class="sn">#</td>
                    <td>Reference</td>
                    <td>Product</td>
                    <td>Price</td>
                    <td>Date</td>
                    <td>Status</td>
                </tr>
            </thead>

            <tbody>
                <tr
                    v-for="(order, index) in orders"
                    :key="index"
                >
                    <td>{{ index + 1 }}</td>
                    <td>{{ order.transaction_id }}</td>
                    <td class="flex flex-row flex-h-center">
                        <img
                            :src="order.item.cart_item.product_image"
                            alt="order.item.cart_item.product_name"
                        />
                        <span>
                            {{ order.item.cart_item.product_name }}
                        </span>
                    </td>
                    <td>{{ order.item.cart_item.product_price }}</td>
                    <td>{{ order.date | date }}</td>
                    <td>
                        <button :class="order_color(order.status)">
                            <i :class="order_icon(order.status)"></i>
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    export default {
        name: 'AdminOrdersList',
        props: [
            'orders'
        ],
        methods: {
            order_color (status) {
                var classes = [];

                classes.unshift('btn-small')

                var PENDING_COLOR = 'primary'
                var PROCESSING_COLOR = 'warning'
                var DONE_COLOR = 'success'
                var CANCELLED_COLOR = 'danger'

                switch (status) {
                    case 'PD':
                        classes.unshift(PENDING_COLOR)
                        break;
                    case 'PS':
                        classes.unshift(PROCESSING_COLOR)
                        break;
                    case 'DN':
                        classes.unshift(DONE_COLOR)
                        break;
                    case 'CD':
                        classes.unshift(CANCELLED_COLOR)
                        break;
                }

                return classes
            },
            order_icon (status) {
                var classes = [];

                classes.unshift('fas')

                var PENDING_ICON = 'fa-stop'
                var PROCESSING_ICON = 'fa-spinner'
                var DONE_ICON = 'fa-check'
                var CANCELLED_ICON = 'fa-times-circle'

                switch (status) {
                    case 'PD':
                        classes.unshift(PENDING_ICON)
                        break;
                    case 'PS':
                        classes.unshift(PROCESSING_ICON)
                        break;
                    case 'DN':
                        classes.unshift(DONE_ICON)
                        break;
                    case 'CD':
                        classes.unshift(CANCELLED_ICON)
                        break;
                }

                return classes
            }
        }
    }
</script>
