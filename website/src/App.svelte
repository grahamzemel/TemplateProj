<script>
	import "./main.scss";
	import { state } from "./store/states.js";
	import Home from "./main/Home.svelte";
	import Docs from "./main/Docs.svelte";

	let page 
    $: if ($state) {
        page = $state[0].component.name;
    }
</script>

<body class="container">
	{#if page == "Home"}
		<Home />
	{/if}
	{#if page == "Docs"}
		<Docs />
	{/if}
</body>
