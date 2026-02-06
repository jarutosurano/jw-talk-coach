// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://jarutosurano.github.io',
	base: '/jw-talk-coach',
	integrations: [
		starlight({
			title: 'JW Talk Coach',
			favicon: '/favicon.png',
			social: [
				{ icon: 'github', label: 'GitHub', href: 'https://github.com/jarutosurano/jw-talk-coach' },
			],
			sidebar: [
				{
					label: '10-Minute Talks',
					autogenerate: { directory: 'talks/10min' },
				},
				{
					label: '30-Minute Talks',
					autogenerate: { directory: 'talks/30min' },
				},
				{
					label: 'Field Ministry',
					autogenerate: { directory: 'field-ministry' },
				},
				{
					label: 'Reference',
					autogenerate: { directory: 'reference' },
				},
			],
			defaultLocale: 'root',
			locales: {
				root: { label: 'Tagalog', lang: 'tl' },
			},
		}),
	],
});
