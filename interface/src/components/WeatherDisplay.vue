<template> 
    <div class="center-flex">
        <button id="hourlyButton" class="tab" @:click="hourly = true;">Hourly</button>
        <button id="7DaysButton" class="tab" @:click="hourly = false;">This Week</button>
    </div>

    <HourlyWeather v-if="hourly" :weather=weather></HourlyWeather>

    <DailyWeather v-if="!hourly" :weather=weather></DailyWeather>
</template>


<script lang="ts">

    import { defineComponent } from 'vue';
    import HourlyWeather from './HourlyWeather.vue';
    import DailyWeather from './DailyWeather.vue';
    import WeatherService from '@/Services/WeatherService';
    import { WeatherMode } from '@/Types/WeatherMode';

    export default defineComponent({
        name: "WeatherDisplay",
        data () {
            return {
                hourly: true,
                // random: false,
                // @ts-ignore
                weather: ((this.$weather_mode == WeatherMode.TEST) ? WeatherService.getWeatherTest() : (this.random ? WeatherService.getWeatherRandom(): (this.locationName != null ? WeatherService.getWeatherFromLocation(this.locationName): ((this.latitude != null && this.longitude != null) ? WeatherService.getWeatherFromCoors(this.latitude, this.longitude): WeatherService.getWeatherTest()))  )),
                // weather: WeatherService.getWeatherTest(),
            };
        },
        props: [
            'random', 
            'locationName',
            'latitude',
            'longitude'
        ],
        components: {
            HourlyWeather,
            DailyWeather,
        }
    })
</script>

<style>

</style>