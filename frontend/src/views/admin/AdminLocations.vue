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
							<form class="border-0" @submit.prevent="add_location()">
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
										<select
											class="rounded rounded-r-none m-0 p-2 w-full appearance-none leading-tight w-full"
											v-model="location_region"
											required
										>
											<option value="" disabled>Select region</option>
											<option
												v-for="(region, index) in regions"
												:key="index"
												:value="region.id"
											>
												{{ region.region }}
											</option>
										</select>

										<AddRegionForm />

										<button
											class="rounded-l-none m-0 p-2 bg-red-700"
											type="button"
											@click="add_region"
										>
											<i class="fas fa-plus"></i>
										</button>
									</div>
								</div>

								<div class="row">
									<div class="col s12 m12 l12">
										<label class="form-header">Location</label>
									</div>

									<div class="col s12 m12 l12">
										<input type="text" class="p-2 bg-white" v-model="new_location" required />
									</div>
								</div>

								<div class="row">
									<div class="col s12 m12 l12">
										<button
											class="w-auto h-auto bg-red-700 p-2 px-5"
											type="submit"
										>
											save
										</button>
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
	import AddRegionForm from '@/components/locations/AddRegionForm.vue'

	import * as types from '@/store/types.js'
	import { mapGetters, mapActions } from 'vuex'
	import '@/assets/css/modal.css'
	import { show_modal } from '@/assets/js/modal.js'

	export default {
		name: 'AdminLocation',
		components: {
			LocationsList,
			AddRegionForm
		},
		data () {
			return {
				location_region: '',
				new_location: ''
			}
		},
		mounted () {
			this.get_locations()
			this.get_regions()
		},
		computed: {
			...mapGetters({
				locations: 'get_locations',
				regions: 'get_regions',
				user: 'get_user'
			})
		},
		methods: {
			...mapActions({
				get_locations: types.GET_ADMIN_DELIVERY_LOCATIONS,
				get_regions: types.GET_ADMIN_DELIVERY_REGIONS,
				create_region: types.CREATE_ADMIN_DELIVERY_REGION,
				create_location: types.CREATE_ADMIN_DELIVERY_LOCATION,
			}),
			add_location () {
				const coordinates = {
					latitude: 5.547373458458345,
					longitude: 2.345346457547
				}

				const payload = {
					location_author: this.user.id,
					region: this.location_region,
					title: this.new_location,
					latitude: coordinates.latitude,
					longitude: coordinates.longitude
				}

				this.create_location(payload)

				this.clear_form_field()

				this.get_locations()
				this.get_regions()
			},
			clear_form_field () {
				this.new_location = ''
			},
			add_region () {
				show_modal('add_region_form')
			}
		}
	}
</script>
