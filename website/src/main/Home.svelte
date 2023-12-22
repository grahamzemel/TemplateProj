<script>
	import { onMount } from "svelte";

	let data = {};

	let isLoading = false;
	let errorMsg = "";

	async function fetchData() {
		isLoading = true;
		try {
			let response = await fetch("http://localhost:3000/api/data");
			if (!response.ok) {
				throw new Error(`HTTP error! status: ${response.status}`);
			}
			data = await response.json();
		} catch (error) {
			errorMsg = error.message;
		} finally {
			isLoading = false;
		}
	}

	async function postData() {
		isLoading = true;
		try {
			let response = await fetch("http://localhost:3000/api/data", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({
					msg: "Hello from SvelteKit",
				}),
			});
			if (!response.ok) {
				throw new Error(`HTTP error! status: ${response.status}`);
			}
			data = await response.json();
		} catch (error) {
			errorMsg = error.message;
		} finally {
			isLoading = false;
		}
	}

	onMount(() => {
		fetchData();
		postData();
	});

</script>

<div class="container mt-5">
	<h1 class="title has-text-centered mb-5">
		BaseKit (Bulma, Firebase, Sveltekit)
	</h1>
	<div class="box p-5">
		{#if isLoading}
			<p>Loading...</p>
		{:else if errorMsg !== ""}
			<p>{errorMsg}</p>
		{:else}
			<button on:click={fetchData}>Fetch Data</button>
			<button on:click={postData}>Post Data</button>
		{/if}
	</div>
	<div class="box p-5">
		{data.message}
	</div>
</div>

<style>
	.container {
		max-width: 800px;
	}
	p {
		color: darkslategray;
	}
</style>
