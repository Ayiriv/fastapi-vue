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
    <button type="search" class="btn btn-primary" @click="getpharmacy">Search</button>
  </div>
  <div v-for="pharmacy in pharmacies" :key="pharmacy.id">
      <!-- 显示药店数据 -->
      <p>{{ pharmacy.name }}</p>
      <p>{{ pharmacy.contact }}</p>
      <p>{{ pharmacy.addr }}</p>
  </div>
  
</template>
<script>


import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HomeView',
  data() {
    return {
      inputValue: '',
    };
  },
  computed : {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    },
    pharmacies() {
    return this.$store.getters.statePharmacies;
  }
  },
  methods: {
    async getpharmacy() {
      try{
        console.log(this.inputValue);
        await this.$store.dispatch('searchPharmacy', this.inputValue);
        console.log("finished");
      }catch (error) {
        console.log("error", error);
      }
    },
  },
});
</script>
