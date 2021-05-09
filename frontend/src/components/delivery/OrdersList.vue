<template>
    <div class="overflow">
        <table>
            <thead>
                <tr>
                    <td class="sn">#</td>
                    <td>Reference</td>
                    <td>Product</td>
                    <td>Price</td>
                    <td>Date</td>
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
                    <td class="flex flex-row flex-h-center">
                        <img
                            :src="order.item.cart_item.product_image"
                            :alt="order.item.cart_item.product_name"
                        />
                        <span>
                            {{ order.item.cart_item.product_name }}
                        </span>
                    </td>
                    <td>{{ order.item.cart_item.product_price }}</td>
                    <td>{{ order.date | date }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    export default {
        name: 'OrdersList',
        props: [
            'orders'
        ]
    }
</script>
