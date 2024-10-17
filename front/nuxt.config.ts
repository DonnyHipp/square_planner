// https://nuxt.com/docs/api/configuration/nuxt-config


const pkg = require('./package')


module.exports = {
    mode: 'universal',

    /*
    ** Headers of the page
    */
    head: {
        title: 'Nuxt project',
        meta: [
            {charset: 'utf-8'},
            {name: 'viewport', content: 'width=device-width, initial-scale=1'},
            {hid: 'description', name: 'description', content: pkg.description}
        ],
        link: [
            {rel: 'icon', type: 'image/x-icon', href: '/favicon.ico'}
        ]
    },
    compatibilityDate: '2024-04-03',
    devtools: {enabled: true},
    modules: ['@pinia/nuxt', '@nuxtjs/tailwindcss', '@nuxt/image'],
    css: ['@/assets/styles/main.scss'],
    plugins: [
        '@/plugins/global-scss.js', // Регистрация плагина
    ],
    vite: {
        css: {
            preprocessorOptions: {
                scss: {
                    additionalData: '@use "~/assets/global/_vars.scss" as *;'
                }
            }
        }
    }
    }

