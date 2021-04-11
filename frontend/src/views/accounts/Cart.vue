<template>
	<Base>
		<template v-slot:main>
			<div class="row">
				<div class="col s12 m12 l7">
					<CartItemContainer
						:items="items"
					/>
				</div>

				<div class="col s12 m12 l5">
					<CartForm />
				</div>
			</div>
		</template>
	</Base>
</template>

<script>
	import CartForm from '@/components/CartForm.vue'
	import CartItemContainer from '@/components/CartItemContainer.vue'

	export default {
		name: 'Cart',
		components: {
			CartForm,
			CartItemContainer
		},
		data () {
			return {
				items: [
					{
						name: 'Gurasa',
						image: '~/assets/img/prod-4.png',
						store: 'Gali\'s Store'
					},
					{
						name: 'Shawarma',
						image: '~/assets/img/prod-2.jpg',
						store: 'Blue Shop'
					},
					{
						name: 'Cake',
						image: '~/assets/img/prod-4.png',
						store: 'Gali\'s Store'
					},
					{
						name: 'Bread',
						image: '~/assets/img/prod-2.jpg',
						store: 'Issa\'s'
					}
				]
			}
		}
	}
</script>
