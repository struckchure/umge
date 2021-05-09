<template>
	<thead>
		<tr>
			<td v-for="(header, index) in headers">{{ header }}</td>
		</tr>
	</thead>
</template>

<script>
	export default {
		name: 'TableHeader',
		props: [
			'headers'
		]
	}
</script>
