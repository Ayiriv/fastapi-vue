import { createStore } from "vuex";

import notes from './modules/notes';
import users from './modules/users';
import pharmacies from "./modules/pharmacies";

export default createStore({
  modules: {
    notes,
    users,
    pharmacies,
  }
});
