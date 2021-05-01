<template>
	<Base>
		<template v-slot:main>
			<div class="row">
				<div class="col s12 m12 l12">
					<label class="form-header">
						Management / Users
					</label>

					<AdminUsersList />
				</div>
			</div>
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
