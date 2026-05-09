<template> 
    <div class="center-grid">
        <div id="weather" if="weatherPulled">
            <WeatherDisplay></WeatherDisplay>
        </div>

    </div>
</template>


<script lang="ts">

    import { defineComponent } from 'vue';
    import WeatherDisplay from './WeatherDisplay.vue';

    export default defineComponent({
        name: "Travel the World",
        data () {
            return {

            };
        },
        methods: {

        },
        components: {
            WeatherDisplay,
        }
    })
</script>

<style>

</style>