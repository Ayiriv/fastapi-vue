import axios from 'axios';

const state = {
  presales: null,
  presale: null,
  myPresales: null
};

const getters = {
  statePresales: state => state.presales,
  statePresale: state => state.presale,
  stateMyPresales: state => state.myPresales,
};

const actions = {
  async createPresale({dispatch}, presale) {
    await axios.post('presales', presale);
    await dispatch('getPresales');
  },
  async getPresales({commit}) {
    let {data} = await axios.get('presales');
    commit('setPresales', data);
  },
  async viewPresale({commit}, id) {
    let {data} = await axios.get(`presale/${id}`);
    commit('setPresale', data);
  },
  async searchPresales({commit}, name) {
    let {data} = await axios.get(`presale/search/${name}`);
    commit('setPresales', data);
    console.log("search", data);
  },
  async getPresalesByPharmacy({commit}, pharmacy_id) {
    let {data} = await axios.get(`presale/by-pharmacy/${pharmacy_id}`);
    commit('setMyPresales', data);
    console.log("get by pharmacy", data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updatePresale({}, presale) {
    await axios.patch(`presale/${presale.id}`, presale.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deletePresale({}, id) {
    await axios.delete(`presale/${id}`);
  },
  // eslint-disable-next-line no-empty-pattern
  async deletePresalesByPharmacy({}, pharmacy_id) {
    await axios.delete(`presale/by-pharmacy/${pharmacy_id}`);
  }
};

const mutations = {
  setPresales(state, presales){
    state.presales = presales;
  },
  setPresale(state, presale){
    state.presale = presale;
  },
  setMyPresales(state, myPresales){
    state.myPresales = myPresales;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
