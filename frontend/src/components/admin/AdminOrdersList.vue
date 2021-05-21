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
                    class="hover:bg-gray-400 hover:text-white cursor-pointer"
                >
                    <td>{{ index + 1 }}</td>
                    <td>{{ order.transaction_id }}</td>
                    <td>
                        <img
                            :src="order.item.cart_item.product_image"
                            alt="order.item.cart_item.product_name"
                            class="w-20 h-10"
                        />
                        <p>
                            {{ order.item.cart_item.product_name }}
                        </p>
                    </td>
                    <td>{{ order.item.cart_item.product_price }}</td>
                    <td>{{ order.date | date }}</td>
                    <td>
                        <label class="w-11 p-2 text-white rounded" :class="order_color(order.status)">
                            <i :class="order_icon(order.status)"></i>
                        </label>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    import { order_color, order_icon } from '@/store/utils.js'

    export default {
        name: 'AdminOrdersList',
        props: [
            'orders'
        ],
        methods: {
            order_color,
            order_icon
        }
    }
</script>
