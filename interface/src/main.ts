import './assets/main.css'

import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'

import { StorageMode } from '@/Types/StorageMode';

// globals - need to update down below too
const storage_mode = StorageMode.SESSIONSTORAGE;

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
        }, 
        {
            path: "/theWorld", 
            name: "The World", 
            component: () => import("./components/TheWorld.vue")
        }
    ]
});


// const app as App<Element> = createApp(App).use(router).mount("#app");
const app = createApp(App);
app.use(router);

// globals
app.config.globalProperties.$storage_mode = storage_mode;

app.mount("#app");

