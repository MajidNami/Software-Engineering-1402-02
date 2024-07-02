// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    typescript: false,
    ssr:false,
    app: {
        head: {
            title: 'Tick8',
            link: [
                {
                    id: 'theme-css',
                    rel: 'stylesheet',
                    type: 'text/css',
                    href: '/themes/aura-dark-amber/theme.css'
                }
            ]
        }
    },
    modules: ['nuxt-primevue'],
    primevue: {

        locale: {
            dayNames:	['یکشنبه', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
            dayNamesShort	:['یکش', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

        },
        options: { ripple: true },
        components: {
            exclude: ['Editor']
        }
    },
    script: [
        {
            strategy: 'lazyOnload',
            src: 'https://www.googletagmanager.com/gtag/js?id=UA-93461466-1'
        },
        {
            id: 'ga-analytics',
            strategy: 'lazyOnload',
            children: `
                window.dataLayer = window.dataLayer || [];
                function gtag(){dataLayer.push(arguments);}
                gtag('js', new Date());
                gtag('config', 'UA-93461466-1');
            `
        }
    ],
    baseURL:'/group8/',
    css: ['primeicons/primeicons.css', 'primeflex/primeflex.scss', 'primevue/resources/primevue.min.css', '@/assets/styles.scss'],
    runtimeConfig: {

    }

});
