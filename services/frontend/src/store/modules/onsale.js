import axios from 'axios';

const state = {
  onsales: null,
  onsale: null,
  myOnsales: null,
  check: null,
};

const getters = {
  stateOnsales: state => state.onsales,
  stateOnsale: state => state.onsale,
  stateMyOnsales: state => state.myOnsales,
  stateCheck: state => state.check,
};

const actions = {
  async createOnsale({dispatch}, onsale) {
    await axios.post('onsales', onsale);
    await dispatch('getOnsales');
  },
  async getOnsales({commit}) {
    let {data} = await axios.get('onsales');
    commit('setOnsales', data);
  },
  async viewOnsale({commit}, id) {
    let {data} = await axios.get(`onsale/${id}`);
    commit('setOnsale', data);
  },
  async searchOnsales({commit}, name) {
    let {data} = await axios.get(`onsale/search/${name}`);
    commit('setOnsales', data);
    console.log("search", data);
  },
  async searchOnsalesBySymptom({commit}, symptom) {
    let {data} = await axios.get(`onsale/search/symptom/${symptom}`);
    commit('setOnsales', data);
    console.log("search", data);
  },
  async getOnsalesByPharmacy({commit}, pharmacy_id) {
    let {data} = await axios.get(`onsale/by-pharmacy/${pharmacy_id}`);
    commit('setMyOnsales', data);
    console.log("get by pharmacy", data);
  },
  async checkOnsalesExistence({commit}, medicine_id) {
    let {data} = await axios.get(`onsale/exist/${medicine_id}`);
    commit('setCheck', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateOnsale({}, onsale) {
    await axios.patch(`onsale/${onsale.id}`, onsale.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteOnsale({}, id) {
    await axios.delete(`onsale/${id}`);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteOnsalesByPharmacy({}, pharmacy_id) {
    await axios.delete(`onsale/by-pharmacy/${pharmacy_id}`);
  }
};

const mutations = {
  setOnsales(state, onsales){
    state.onsales = onsales;
  },
  setOnsale(state, onsale){
    state.onsale = onsale;
  },
  setMyOnsales(state, myOnsales){
    state.myOnsales = myOnsales;
  },
  setCheck(state, check){
    state.check = check;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
