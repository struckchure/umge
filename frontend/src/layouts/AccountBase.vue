<template>
	<div class="accounts-base">
		<div class="accounts-form elevation">
			<slot></slot>
		</div>
	</div>
</template>

<script>
	import '@/assets/css/all.css'
	// import '@/assets/css/style.css'
	import '@/assets/css/accounts.css'
	import '@/assets/css/layouts.css'

	export default {
		name: 'AccountBase'
	}
</script>
