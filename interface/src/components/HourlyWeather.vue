<template> 
    <h1>hi this is a test</h1>
    <h2>
        <slot name="h2test"></slot>
    </h2>
</template>


<script lang="ts">

    import { defineComponent } from 'vue';

    export default defineComponent({
        name: "",
        data () {
            return {

            };
        },
        methods: {

        }
    })
</script>

<style>

</style>