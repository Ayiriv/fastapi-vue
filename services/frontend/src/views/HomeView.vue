<template>
  <section>
    <p>This site is built with FastAPI and Vue.</p>

    <div v-if="isLoggedIn" id="logout">
      <p id="logout">Click <a href="/dashboard">here</a> to view all notes.</p>
    </div>
    <p v-else>
      <span><a href="/register">Register</a></span>
      <span> or </span>
      <span><a href="/login">Log In</a></span>
    </p>
  </section>
  <div class="mb-3">
    <input type="text" placeholder="请输入关键词" name="addr" v-model="inputValue" class="form-control" />
    <button @click="search" class="btn btn-primary">Search</button>
  </div>
  <div v-for="pharmacy in pharmacies" :key="pharmacy.id">
    <div class="card" style="width: 18rem;">
            <div class="card-body">
      <!-- 显示药店数据 -->
      <li>{{ pharmacy.name }}</li>
      <li>{{ pharmacy.contact }}</li>
      <li>{{ pharmacy.addr }}</li>
  </div>
  </div>
  </div>
  
</template>
<script>


import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'HomeView',
  data() {
    return {
      inputValue: '',
      pharmacyList: [],
    };
  },
  created: function() {
    return this.$store.dispatch('getPharmacies');
  },
  computed : {
    ...mapGetters({pharmacies: 'statePharmacies'}),
  },
  methods: {
    ...mapActions(['searchPharmacies']),
    async search () {
      try {
        console.log("click", this.inputValue);
        await this.searchPharmacies(this.inputValue);
        this.pharmacyList = this.pharmacies;
        console.log(this.pharmacyList);
      } catch (error) {
        console.log(error);
      }
    }
  },
});
</script>
