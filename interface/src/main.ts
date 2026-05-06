import './assets/main.css'

import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        // {
        //     path: "/",
        //     name: "home",
        //     component: App,
        // },
        {
            path: "/",
            alias: "/home",
            name: "home", 
            component: () => import("./components/Home.vue"),
        },
        {
            path: "/weatherMachine", 
            name: "Weather Machine", 
            component: () => import("./components/WeatherMachine.vue")
        }, 
        {
            path: "/amongUS", 
            name: "Among Us", 
            component: () => import("./components/AmongUs.vue")
        }
    ]
});


createApp(App).use(router).mount("#app");
