import axios from 'axios';

const state = {
  pharmacies: null,
  pharmacy: null,
  myPharmacies: null
};

const getters = {
  statePharmacies: state => state.pharmacies,
  statePharmacy: state => state.pharmacy,
  stateMyPharmacies: state => state.myPharmacies,
};

const actions = {
  async createPharmacy({dispatch}, pharmacy) {
    await axios.post('pharmacies', pharmacy);
    await dispatch('getPharmacies');
  },
  async getPharmacies({commit}) {
    let {data} = await axios.get('pharmacies');
    commit('setPharmacies', data);
  },
  async viewPharmacy({commit}, id) {
    let {data} = await axios.get(`pharmacy/${id}`);
    commit('setPharmacy', data);
  },
  async searchPharmacies({commit}, name) {
    let {data} = await axios.get(`pharmacy/search/${name}`);
    commit('setPharmacies', data);
    console.log("search", data);
  },
  async getPharmaciesByOwner({commit}, owner_id) {
    let {data} = await axios.get(`pharmacy/by-owner/${owner_id}`);
    commit('setMyPharmacies', data);
    console.log("get by owner", data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updatePharmacy({}, pharmacy) {
    await axios.patch(`pharmacy/${pharmacy.id}`, pharmacy.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deletePharmacy({}, id) {
    await axios.delete(`pharmacy/${id}`);
  },
  // eslint-disable-next-line no-empty-pattern
  async deletePharmaciesByOwner({}, owner_id) {
    await axios.delete(`pharmacy/by-owner/${owner_id}`);
  }
};

const mutations = {
  setPharmacies(state, pharmacies){
    state.pharmacies = pharmacies;
  },
  setPharmacy(state, pharmacy){
    state.pharmacy = pharmacy;
  },
  setMyPharmacies(state, myPharmacies){
    state.myPharmacies = myPharmacies;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
