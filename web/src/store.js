import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
      tableData: [],
      colomnNames: []
  },
  
  getters: {
  },
  
  mutations: {
    setTableData(context, tableData){
        context.tableData = tableData;
    },
    setColomnNames(context, colomnNames){
        context.colomnNames = colomnNames;
    }
  },
  
  actions: {
    updateFromAPI(state){
        console.log("FETCHING")
        fetch('/api/countries')
        .then(response => {
            console.log(response);
            return response
        })
        .then(response => response.json())
        .then(response => {
            return response
        })
        .then(
            resp => {
                state.commit('setColomnNames', resp[0]);
                state.commit('setTableData', resp.slice(1))
            }
        )
    }
  }
});