import svelte from 'rollup-plugin-svelte';
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import livereload from 'rollup-plugin-livereload';
import { terser } from 'rollup-plugin-terser';

//added for bulma
import postcss from 'rollup-plugin-postcss'
import serve from 'rollup-plugin-serve';

const production = !process.env.ROLLUP_WATCH;

export default {
	input: 'src/main.js',
	output: {
		sourcemap: true,
		format: 'iife',
		name: 'app',
		file: 'public/bundle.js',
		globals: {
			'svelte/internal': 'internal',
			'svelte/store': 'store'
		  }
	},
	plugins: [
		svelte({
			// enable run-time checks when not in production
			compilerOptions: {
				dev: !production,
			  },
		}),
		//added for bulma
 		postcss(),
		resolve({
			browser: true,
			dedupe: importee => importee === 'svelte' || importee.startsWith('svelte/')
		}),
		commonjs(),

		!production && serve({
			contentBase: 'public',
			historyApiFallback: true,
			host: 'localhost',
			port: 8080,
		  }),
		  !production && livereload('public'),
		  production && terser(),
	],
	watch: {
		clearScreen: false
	}
};
