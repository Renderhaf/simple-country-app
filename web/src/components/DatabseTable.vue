<template>
    <div>
        <h1>Table</h1>
        <h2>{{this.$store.state.colomnNames}}</h2>
        <h3>{{this.$store.state.tableData}}</h3>
    </div>
</template>

<script>
export default {
    name: "DatabaseTable",
    mounted(){
        console.log('Table loaded')
        this.$store.dispatch('updateFromAPI');
    } 
}
</script>

<style>

</style>