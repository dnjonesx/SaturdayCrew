<template> 
     <img src="../assets/among_us_green.ico" v-show="showAmong" id="amongus" v-on:mouseover="onAmongUs">
    
    <div class="center-grid">
        <h1>{{ location_msg }}</h1>

        <div class="large-text-input">
            <input type="text" id="location" placeholder="Enter your location here..." class="large-text-input">
        </div>
    </div>
</template>


<script lang="ts">

    import { defineComponent } from 'vue';
    import { LocationEntered } from '@/Types/LocationEntered';
    import { StorageMode } from '@/Types/StorageMode';

    export default defineComponent({
        name: "Home",
        data () {
            return {
                showAmong: false,
                intervalID: 0,
                counter: 0,
                left: false,
                location_msg: "no place like home :)",
                location: "",
                locationEntered: LocationEntered.FALSE as LocationEntered
            };
        },
        methods: {
            // triggered when someone hovers their mouse over our among us guy
            onAmongUs() {
                console.log("Something despicable has occurred...");

                // still need to figure out which storage functionality i want to use...
                // @ts-ignore
                switch (this.$storage_mode) {
                    case StorageMode.COOKIES: 
                        document.cookie = "amongus=evil; path=/";
                        break;
                    case StorageMode.LOCALSTORAGE: 
                        localStorage.setItem("amongus", "evil");
                        break;
                    case StorageMode.SESSIONSTORAGE: 
                        sessionStorage.setItem("amongus", "evil");
                        break;
                }
                this.$router.replace({path: "/amongUS"}); 
            },
            // after having retrieved the user's location
            locationRetrieved(position: GeolocationPosition) {
                this.location_msg = "hold still while we track you...";
                let lat = position.coords.latitude;
                let long = position.coords.longitude;
                this.locationEntered = LocationEntered.COORDS_ENTERED;
            }, 
            // unable to retrieve the user's location
            locationError(error: GeolocationPositionError) {
                switch(error.code) {
                    case error.PERMISSION_DENIED: 
                        this.location_msg = "alright keep your secrets then...";
                        break;
                    case error.POSITION_UNAVAILABLE:
                        this.location_msg = "bro where are you ??" 
                        break;
                    case error.TIMEOUT :
                        break;
                    default: 

                }
            }
        }, 
        mounted() {
            // little among us guy trekking functionality
            const among = document.getElementById("amongus");
            if (!among) return;

            among.style.bottom = "0";
            among.style.left = "0";
            this.showAmong = true;

            this.intervalID = setInterval(() => {
                among.style.left = this.counter + "px";

                if (this.counter >= window.innerWidth - 20) {
                    this.left = true;
                    among.style.transform = "scaleX(-1)";
                } else if (this.counter == 0) {
                    this.left = false;
                    among.style.transform = "scaleX(1)";
                }

                if (!this.left) {
                    this.counter += 2;
                    // console.log("to the left.." + among.style.left);
                } else {
                    this.counter -= 2;
                    // console.log("to the right.." + among.style.left);
                }
            }, 20);

            // user's location functionality
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(this.locationRetrieved, this.locationError);
                // navigator.geolocation.watchPosition(this.locationRetrieved, this.locationError);
            } else {
                // geolocation not supported by user's browser
            }
        }, 
        unmounted() {
            // clear amongus trekking interval
            if (this.intervalID != 0) clearInterval(this.intervalID);
        },
    })
</script>

<style>

    #amongus {
        position: fixed;
        height: 30px;
    }

</style>