<template> 
    <div class="center-flex">
        <button id="hourlyButton" class="tab" @:click="hourly = true;">Hourly</button>
        <button id="7DaysButton" class="tab" @:click="hourly = false;">This Week</button>
    </div>

    <HourlyWeather v-if="hourly">
        <template #h2test>this is also a test</template>
    </HourlyWeather>

    <DayWeather v-if="!hourly">
        <template #h2test>this is a test but for daily</template>
    </DayWeather>
</template>


<script lang="ts">

    import { defineComponent } from 'vue';
    import HourlyWeather from './HourlyWeather.vue';
    import DayWeather from './7DayWeather.vue';

    export default defineComponent({
        name: "",
        data () {
            return {
                hourly: true,
            };
        },
        methods: {

        },
        components: {
            HourlyWeather,
            DayWeather,
        }
    })
</script>

<style>

</style>