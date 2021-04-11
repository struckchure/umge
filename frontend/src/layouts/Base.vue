<template>
	<div class="pama-0">
		<aside>
			<router-link
				:to="{ name: 'Home' }"
				title="UMGE"
			>
				<img src="@/assets/logo.png" class="logo">
			</router-link>

			<router-link :to="{ name: 'Home' }">
				<button class="active">
					<i class="fas fa-home"></i>
					<span>Home</span>
				</button>
			</router-link>

			<router-link to="/">
				<button>
					<i class="fas fa-user"></i>
					<span>Profile</span>
				</button>
			</router-link>

			<router-link to="/">
				<button>
					<i class="fas fa-wallet"></i>
					<span>Wallet</span>
				</button>
			</router-link>

			<router-link :to="{ name: 'Login' }">
				<button>
					<i class="fas fa-door-open"></i>
					<span>Logout</span>
				</button>
			</router-link>
		</aside>

		<main>
			<div class="navbar">
				<div class="brand-name">
					<router-link to="/">eCommerce</router-link>
				</div>

				<div class="cart">
					<p class="wallet-balance">
						&#8358; 1245.78
					</p>
					<router-link :to="{ name: 'Cart' }">
						<button>
							<i class="fas fa-shopping-cart"></i>
						</button>
					</router-link>
					<label>40</label>
				</div>
			</div>

			<div class="main-container">
				<slot name="main">
					<div class="entry-card">
						<div class="breadcrumb">
							<div class="current-page">
								Home / <span>{{ current_page }}</span>
							</div>

							<p class="page-title">{{ page_title }}</p>

							<div class="breadcrumb-extra">
								<slot name="extra"></slot>
							</div>
						</div>
						<slot></slot>
					</div>
				</slot>
			</div>
		</main>
	</div>
</template>

<script>
	import '@/assets/css/all.css'
	import '@/assets/css/style.css'
	import '@/assets/css/layouts.css'

	export default {
		name: 'Base',
		props: [
			'current_page',
			'page_title'
		],
		methods: {
			toggle_aside() {
				// var aside = document.getElementsByTagName('aside')[0]
			}
		}
	}
</script>
