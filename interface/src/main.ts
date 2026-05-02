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
            path: "/test",
            name: "test", 
            component: () => import("./components/Test.vue"),
        },
        {
            path: "/weatherMachine", 
            name: "Weather Machine", 
            component: () => import("./components/WeatherMachine.vue")
        }
    ]
});


createApp(App).use(router).mount("#app");
