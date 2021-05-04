<template>
	<div class="bg-gray-300 p-4 my-1 rounded-2xl border-l-4 border-solid border-red-700">
		<p class="text-blue-600 font-bold fntz-9">
			{{ history.description }} |
			<a href="#" class="underline text-blue-400 hover:text-blue-500">Details</a>
		</p>
		<label class="p-0 text-right italic">{{ history.date | date }}</label>
	</div>
</template>

<script>
	export default {
		name: 'WalletFundHistory',
		props: [
			'history'
		]
	}
</script>
