<template> 
    <h1>BRUH</h1>
</template>


<script lang="ts">

    import { defineComponent } from 'vue';
    import { StorageMode } from '@/Types/StorageMode';

    export default defineComponent({
        name: "",
        data () {
            return {

            };
        },
        methods: {
            kickout() {
                console.log("heathen !! banish");
                this.$router.replace({path: "/"});
            },
        },
        mounted() {
            // @ts-ignore
            switch (this.$storage_mode) {
                case StorageMode.COOKIES: 
                    if (document.cookie.split(";").some((item) => item.trim().startsWith("amongus="))) {
                        // cookie among us exists
                    } else {
                        // cookie among us does not exist
                        this.kickout();
                    }
                    break;
                case StorageMode.LOCALSTORAGE: 
                    if (localStorage.getItem("amongus") == "evil") {
                        // key amongus exists and is equal to evil
                    } else {
                        this.kickout();
                    }
                    break;
                case StorageMode.SESSIONSTORAGE: 
                    if (sessionStorage.getItem("amongus") == "evil") {
                        // key amongus exists and is equal to evil
                    } else {
                        this.kickout();
                    }
                    break;
            }
        }
    })
</script>

<style>

</style>