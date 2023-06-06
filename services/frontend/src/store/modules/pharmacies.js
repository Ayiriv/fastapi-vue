import axios from 'axios';

const state = {
  pharmacies: null,
  pharmacy: null
};

const getters = {
  statePharmacies: state => state.pharmacies,
  statePharmacy: state => state.pharmacy,
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
  async searchPharmacy({commit}, name) {
    try {
      let {data} = await axios.get(`pharmacy/search/${name}`);
      commit('setPharmacies', data);
      console.log("search", data);
    } catch (error) {
    console.error("search-error", error);
    }
  },
  // eslint-disable-next-line no-empty-pattern
  async updatePharmacy({}, pharmacy) {
    await axios.patch(`pharmacy/${pharmacy.id}`, pharmacy.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deletePharmacy({}, id) {
    await axios.delete(`pharmacy/${id}`);
  }
};

const mutations = {
  setPharmacies(state, pharmacies){
    state.pharmacies = pharmacies;
  },
  setPharmacy(state, pharmacy){
    state.pharmacy = pharmacy;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
