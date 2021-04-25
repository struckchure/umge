<template>
	<div class="overflow">
		<table>
			<thead>
				<tr>
					<td>Username</td>
					<td>E-Mail</td>
					<td>Details</td>
					<td>Date joined</td>
				</tr>
			</thead>
			<tbody>
				<tr
					v-for="(rider, index) in riders"
					:key="index"
				>
					<td>{{ rider.username }}</td>
					<td>{{ rider.email }}</td>
					<td>
						<router-link
							to="/"
						>
							<button class="btn btn-small ma-0">
								<i class="fas fa-eye"></i>
							</button>
						</router-link>
					</td>
					<td>{{ format_date(rider.date) }}</td>
				</tr>
			</tbody>
		</table>
	</div>
</template>

<script>
	import '@/assets/css/table.css'

	export default {
		name: 'AdminRidersList',
        props: [
            'riders'
        ],
		methods: {
			format_date (value) {
				var date = new Date(value)
				return `${date.getDay()}/${date.getMonth()}/${date.getFullYear()}`
			}
		}
	}
</script>
