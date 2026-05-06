<template> 
     <img src="../assets/among_us_green.ico" v-show="showAmong" id="amongus" v-on:mouseover="onAmongUs">
    
    <div class="center-grid">
        <h1>no place like home :)</h1>

        <div class="large-text-input">
            <input type="text" id="location" placeholder="Enter your location here..." class="large-text-input">
        </div>
    </div>
</template>


<script lang="ts">

    import { defineComponent } from 'vue';

    export default defineComponent({
        name: "Home",
        data () {
            return {
                showAmong: false,
                intervalID: 0,
                counter: 0,
            };
        },
        methods: {
            onAmongUs() {
                this.$router.replace({path: "/amongUS"}); 
                // TODO: update so only some people can access page (cookies prob)
            },
        }, 
        mounted() {
            const among = document.getElementById("amongus");
            if (!among) return;

            among.style.bottom = "0";
            among.style.left = "0";
            this.showAmong = true;

            this.intervalID = setInterval(() => {
                among.style.left = this.counter + "px";
                this.counter += 2;
                console.log("to the left.." + among.style.left);
            }, 20);
        }, 
        unmounted() {
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