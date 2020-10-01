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
        fetch('/api/countries')
        .then(response => response.json())
        .then(
            resp => {
                state.commit('setColomnNames', resp[0]);
                state.commit('setTableData', resp.slice(1))
            }
        )
    }
  }
});