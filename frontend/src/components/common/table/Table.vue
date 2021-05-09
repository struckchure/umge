<template>
	<div class="overflow">
		<table>
			<template name="headers">
				<TableHeader :headers="headers" />
			</template>
			
			<template name="body">
				<TableBody>
					<TableRow
						v-for="(item, index) in items"
						:items="item"
					/>
				</TableBody>
			</template>
		</table>
	</div>
</template>

<script>
	import '@/assets/css/table.css'

	import TableHeader from '@/components/table/TableHeader.vue'
	import TableBody from '@/components/table/TableBody.vue'
	import TableRow from '@/components/table/TableRow.vue'

	export default {
		name: 'Table',
		props: [
			'headers',
			'items'
		]
	}
</script>
