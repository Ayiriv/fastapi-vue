import { createStore } from "vuex";

import notes from './modules/notes';
import users from './modules/users';
import pharmacies from "./modules/pharmacies";
import onsale from "./modules/onsale";
import presale from "./modules/presale";
import medicines from "./modules/medicines";

export default createStore({
  modules: {
    notes,
    users,
    pharmacies,
    onsale,
    presale,
    medicines,
  }
});
