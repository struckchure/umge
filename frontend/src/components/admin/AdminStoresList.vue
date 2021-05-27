<template>
	<div>
		<table>
			<thead>
				<tr>
					<td class="sn">#</td>
					<td>Store</td>
					<td>Orders</td>
					<td>Balance</td>
					<td>Date</td>
					<td>Updated</td>
				</tr>
			</thead>

			<tbody>
				<tr
					v-for="(store, index) in stores"
					:key="index"
				>
					<td>{{ index + 1 }}</td>
					<td>{{ store.store_name }}</td>
					<td>{{ store.store_orders.length }}</td>
					<td class="font-bold">&#8358; {{ store.store_balance }}</td>
					<td>{{ store.date | date }}</td>
					<td>{{ store.updated | date }}</td>
				</tr>
			</tbody>
		</table>
	</div>
</template>

<script>
	export default {
		name: 'AdminStoresList',
		props: [
			'stores'
		]
	}
</script>
