<template>
	<Base>
		<template v-slot:main>
			<label class="form-header">
				Management / Users
			</label>

			<AdminUsersList />
		</template>
	</Base>
</template>

<script>
	import AdminUsersList from '@/components/admin/AdminUsersList.vue'

	export default {
		name: 'AdminHome',
		title () {
			return 'UMGE | Management'
		},
		components: {
			AdminUsersList
		}
	}
</script>
