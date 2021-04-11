<template>
	<div class="cart-item elevation-2 row">
		<div class="col s12 m12 l2">
			<div class="cart-img">
				<img class="elevation-2" src="@/assets/img/prod-4.jpg"/>
			</div>
		</div>

		<div class="col s12 m12 l3">
			<div class="cart-description">
				<p>{{ item.name }}</p>
				<label>{{ item.store }}</label>
			</div>
		</div>

		<div class="col s12 m12 l7">
			<div class="cart-tools">
				<button @click="reduce_qty()">
					<i class="fas fa-minus"></i>
				</button>
				<input type="number" min="1" max="99" v-model="qty" />
				<button @click="add_qty()">
					<i class="fas fa-plus"></i>
				</button>

				<p class="price">&#8358; {{ get_price }}</p>

				<button class="danger">
					<i class="fas fa-trash"></i>
				</button>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'CarItem',
		props: [
			'item'
		],
		data () {
			return {
				qty: 1
			}
		},
		computed: {
			get_price () {
				return 250
			}
		},
		mounted () {
			// this.set_image()
		},
		methods: {
			set_image () {
				var img = document.getElementsByTagName('img')[0]
				console.log(img)
				img.src = this.item.image
			},
			add_qty () {
				this.qty += 1
			},
			reduce_qty () {
				if (this.qty > 0) {
					this.qty -= 1
				}
			}
		}
	}
</script>
