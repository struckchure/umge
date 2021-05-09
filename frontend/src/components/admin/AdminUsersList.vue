<template>
	<div class="overflow">
		<table>
			<thead>
				<tr>
					<td>#</td>
					<td>Username</td>
					<td>E-Mail</td>
					<td>Details</td>
					<td>Date joined</td>
				</tr>
			</thead>
			<tbody>
				<tr
					v-for="(user, index) in users"
					:key="index"
					class="hover:bg-gray-400 hover:text-white cursor-pointer"
				>
					<td class="sn">{{ index + 1 }}</td>
					<td>{{ user.username }}</td>
					<td>{{ user.email }}</td>
					<td>
						<router-link
							to="/"
						>
							<button class="bg-red-400 btn btn-small ma-0">
								<i class="fas fa-eye"></i>
							</button>
						</router-link>
					</td>
					<td>{{ user.date | date }}</td>
				</tr>
			</tbody>
		</table>
	</div>
</template>

<script>
	import * as types from '@/store/types.js'
	import { mapGetters, mapActions } from 'vuex'

	import '@/assets/css/table.css'

	export default {
		name: 'AdminUsersList',
		mounted () {
			this.get_users()
		},
		computed: {
			...mapGetters({
				users: 'get_admin_users_list'
			})
		},
		methods: {
			...mapActions({
				get_users: types.GET_ADMIN_USERS_LIST
			})
		}
	}
</script>
