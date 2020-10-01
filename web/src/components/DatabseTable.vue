<template>
    <div id="scrollTable">
        <table>
            <tr>
                <th v-for="cn in this.$store.state.colomnNames" v-bind:key="cn">
                    <span>{{cn}}</span>
                </th>
            </tr>

            <tr v-for="row in this.$store.state.tableData" v-bind:key="row">
                <td v-for="col in row" v-bind:key="col">
                    <span>{{col}}</span>
                </td>
            </tr>
        </table>
    </div>
</template>

<script>
export default {
    name: "DatabaseTable",
    mounted(){
        this.$store.dispatch('updateFromAPI');
    } 
}
</script>

<style>
#scrollTable{
  height: 41.5em;
  overflow: auto;
  display: inline-block;
}

table {
  border-collapse: collapse;
  margin-left: auto;
  margin-right: auto;
}

table, th, td {
  border: 1px solid black;
  padding: 1em;
}

th {
    background-color: #00b0ff;
    position: sticky;
    top: 0px;
}

tr:hover {
    background-color: lightgray;
}
</style>