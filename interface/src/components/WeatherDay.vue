<template> 
    <tr>
        <td><img src="../assets/dino.ico" class="weatherIcon"></td>
        <td id="day">{{ day }}</td>
        <td id="minTemp">{{ minTemp }}</td>
        <td id="maxTemp">{{ maxTemp }}</td>
    </tr>
</template>


<script lang="ts">

    import { defineComponent } from 'vue';

    export default defineComponent({
        name: "Weather Day",
        data () {
            return {

            };
        },
        props: [
            'day', 
            'minTemp', 
            'maxTemp', 
        ],
    })
</script>

<style>

</style>