<template>
	<Base>
		<template v-slot:main>
			<div class="row">
				<div class="col s12 m12 l12">
					<label class="form-header">Locations / </label>
				</div>

				<div class="col s12 m12 l12">
					<div class="row">
						<div class="col s12 m8 l8">
							<LocationsList :locations="locations" />
						</div>

						<div class="col s12 m4 l4">
							<form class="border-0">
								<div class="row">
									<div class="col s12 m12 l12">
										<label class="form-header">Add Current location</label>
									</div>
								</div>

								<div class="row">
									<div class="col s12 m12 l12">
										<label class="form-header">Region</label>
									</div>

									<div class="col s10 m10 l10 flex">
										<select class="rounded rounded-r-none m-0 p-2 w-full appearance-none leading-tight w-full">
											<option>h</option>
										</select>

										<button class="rounded-l-none m-0 p-2 bg-red-700">
											<i class="fas fa-plus"></i>
										</button>
									</div>
								</div>

								<div class="row">
									<div class="col s12 m12 l12">
										<label class="form-header">Location</label>
									</div>

									<div class="col s12 m12 l12">
										<input type="text" class="p-2 bg-white" />
									</div>
								</div>

								<div class="row">
									<div class="col s12 m12 l12">
										<button class="w-auto h-auto bg-red-700 p-2 px-5">save</button>
									</div>
								</div>
							</form>
						</div>
					</div>
				</div>
			</div>
		</template>
	</Base>
</template>

<script>
	import LocationsList from '@/components/locations/LocationsList.vue'
	import * as types from '@/store/types.js'
	import { mapGetters, mapActions } from 'vuex'

	export default {
		name: 'AdminLocation',
		components: {
			LocationsList
		},
		mounted () {
			this.get_locations()
		},
		computed: {
			...mapGetters({
				locations: 'get_locations'
			})
		},
		methods: {
			...mapActions({
				get_locations: types.GET_ADMIN_DELIVERY_LOCATIONS
			})
		}
	}
</script>
