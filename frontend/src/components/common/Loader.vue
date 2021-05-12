<template>
	<div class="loader flex flex-h-center" :style="{ display: get_display }">
		<div class="loader-content">
			<img src="@/assets/logo.png" class="loader-animation">
			<i class="loader-animation">
			</i>

			<p class="form-header mx-auto text-sm md:text-3xl">
				loading ...
			</p>
		</div>
	</div>
</template>

<script>
	import { mapGetters } from 'vuex'

	import '@/assets/css/loader.css'

	export default {
		name: 'Loader',
		computed: {
			...mapGetters({
				is_loading: 'get_is_loading'
			}),
			get_display () {
				if (this.is_loading === true) {
					return 'flex'
				} else {
					return 'none'
				}
			}
		}
	}
</script>
