<template>
    <div>
        <h1>Periodic Elements</h1>

        <p>This component demonstrates fetching data from another K8S service / pods.</p>

        <p v-if="!system"><em>Loading...</em></p>

        <pre>{{system}}</pre>

        

    </div>
</template>

<script>
export default {
    data() {
        return {
            system: null
        }
    },

    methods: {
    },

    async created() {
        // ES2017 async/await syntax via babel-plugin-transform-async-to-generator
        // TypeScript can also transpile async/await down to ES5
        try {
            let response = await this.$http.get('/api/SampleData/elementversion')
            console.log(response.data);
            this.system = response.data;
        } catch (error) {
            console.log(error)
        }
        // Old promise-based approach
        //this.$http
        //    .get('/api/SampleData/WeatherForecasts')
        //    .then(response => {
        //        console.log(response.data)
        //        this.forecasts = response.data
        //    })
        //    .catch((error) => console.log(error))*/
    }
}
</script>

<style>
</style>