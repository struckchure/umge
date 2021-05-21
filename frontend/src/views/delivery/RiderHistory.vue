<template>
	<Base>
		<template v-slot:main>
			<RiderTasksList :enable_read="false" :tasks="tasks" />
		</template>
	</Base>
</template>

<script>
	import { GET_RIDER_TASKS } from '@/store/types.js'
	import { mapActions, mapGetters } from 'vuex'

	import RiderTasksList from '@/components/delivery/RiderTasksList.vue'

	export default {
		name: 'Rider | Tasks | All',
		components: {
			RiderTasksList
		},
		computed: {
			...mapGetters({
				tasks: 'get_tasks'
			})
		},
		methods: {
			...mapActions({
				get_rider_tasks: GET_RIDER_TASKS
			})
		},
		mounted () {
			this.get_rider_tasks('*')
		}
	}
</script>
