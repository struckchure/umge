<template>
	<tr>
		<td v-for="(item, index) in items">{{ item }}</td>
	</tr>
</template>

<script>
	export default {
		name: 'TableRow',
		props: [
			'items'
		]
	}
</script>
