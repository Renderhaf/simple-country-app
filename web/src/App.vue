<template>
  <div id="app">
    <h1>Vue.js + MySQL + Python Test Website</h1>
    <DatabaseTable/>
  </div>
</template>

<script>
import DatabaseTable from './components/DatabseTable.vue'

export default {
  name: 'App',
  components: {
    DatabaseTable
  }
}
</script>

<style>
#app {
  font-family: 'Roboto', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  margin-top: 60px;
}
</style>
