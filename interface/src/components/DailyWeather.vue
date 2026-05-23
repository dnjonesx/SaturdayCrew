<template> 
    <table>
        <tbody>
            <tr>
                <th></th>
                <th>Day</th>
                <th>Low</th>
                <th>High</th>
            </tr>
            <WeatherDay 
                v-for="x in weatherDays" 
                :day="x.day"
                :minTemp="x.minTemp"
                :maxTemp="x.maxTemp"
                >
            </WeatherDay> 
        </tbody>
    </table>
</template>


<script lang="ts">

    import { defineComponent } from 'vue';
    import WeatherService from '@/Services/WeatherService';
    import WeatherDay from './WeatherDay.vue';

    export default defineComponent({
        name: "",
        data () {
            return {
                weatherDays: WeatherService.fromWeatherToDailyWeather(this.weather),
            };
        },
        props: [
            'weather'
        ],
        components: {
            WeatherDay,
        }
    })
</script>

<style>

</style>