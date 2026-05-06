<template> 
    <div class="center-grid">
        <h1>Change the weather with the click of (several) buttons!</h1>
        <h2>Coming soon to the interweb near you</h2>
        <div class="large-text-input">
            <input type="text" id="location" placeholder="Enter your location here..." class="large-text-input" v-model="weather.location">
        </div>
    </div>
</template>


<script lang="ts">

    import { defineComponent } from 'vue';
    import type Weather from '@/Types/Weather';

    export default defineComponent({
        name: "Weather Machine",
        data () {
            return {
                weather: {
                    id: null, 
                    location: "",
                    current_weather: "",
                } as Weather
            };
        },
        methods: {
            saveWeather() {
                // TODO: write logic - save through cookies? or update for everyone
            }
        }
    })
</script>

<style>

</style>