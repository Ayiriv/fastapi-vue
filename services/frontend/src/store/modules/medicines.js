import axios from 'axios';

const state = {
  medicines: null,
  medicine: null,
};

const getters = {
  stateMedicines: state => state.medicines,
  stateMedicine: state => state.medicine,
};

const actions = {
  async getMedicines({commit}) {
    let {data} = await axios.get('medicines');
    commit('setMedicines', data);
  },
  async viewMedicine({commit}, id) {
    let {data} = await axios.get(`medicine/${id}`);
    commit('setMedicine', data);
  },
  async searchMedicines({commit}, name) {
    let {data} = await axios.get(`medicine/search/${name}`);
    commit('setMedicines', data);
    console.log("search", data);
  },
};

const mutations = {
  setMedicines(state, medicines){
    state.medicines = medicines;
  },
  setMedicine(state, medicine){
    state.medicine = medicine;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};
