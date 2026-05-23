<template> 
    <table>
        <tbody>
            <tr>
                <th></th>
                <th>Time</th>
                <th>Temp</th>
                <th>Precipitation</th>
                <th>Wind</th>
            </tr>
            <WeatherHour 
                v-for="x in weatherHours" 
                :time="x.time"
                :temp="x.temp"
                :precip="x.precip"
                :wind="x.wind"
                >
            </WeatherHour> 
        </tbody>
    </table>
</template>

<!-- :key="x.time" -->

<script lang="ts">

    import { defineComponent } from 'vue';
    import WeatherService from '@/Services/WeatherService';
    import WeatherHour from './WeatherHour.vue';

    export default defineComponent({
        name: "",
        data () {
            return {
                // weather: this.weather,
                weatherHours: WeatherService.fromWeatherToHourlyWeather(this.weather),
            };
        },
        props: [
            'weather'
        ],
        methods: {

        }, 
        components: {
            WeatherHour,
        }
    })
</script>

<style>

</style>