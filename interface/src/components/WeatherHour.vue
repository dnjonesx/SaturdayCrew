<template> 
    <tr>
        <td><img src="../assets/dino.ico" class="weatherIcon"></td>
        <td id="time">{{ time }}</td>
        <td id="temp">{{ temp }}</td>
        <td id="precip">{{ precip }}</td>
        <td id="wind">{{ wind }}</td>
    </tr>
</template>

<script lang="ts">

    import { defineComponent } from 'vue';

    export default defineComponent({
        name: "Weather Hour",
        data () {
            return {

            };
        },
        props: [
            'time', 
            'temp', 
            'precip', 
            'wind'
        ],
        methods: {

        }
    })
</script>

<style>

</style>