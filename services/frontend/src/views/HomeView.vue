<template>
  <div>
    <div class="logo">
      <img src="../assets/logo.png" alt="Logo" />
      <h2>药品资源查询系统</h2>
    </div>
    <br />
    <div class="search-bar">
      <input type="text" placeholder="请输入关键词" name="search" v-model="inputValue" class="form-control search-input"/>
      <br /><br />
      <button @click="search" class="btn btn-primary">Search</button>
    </div>
  </div>
</template>

<style scoped>
.logo {
  text-align: center;
  margin-bottom: 20px;
}

.logo img {
  width: 200px;
  height: 200px;
}

.logo h1 {
  margin-top: 10px;
}

.search-bar {
  text-align: center;
  margin-bottom: 20px;
}

.search-input {
    text-align: center;  
  }
</style>
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
        // console.log("click", this.inputValue);
        // await this.searchPharmacies(this.inputValue);
        // this.pharmacyList = this.pharmacies;
        // console.log(this.pharmacyList);
        this.$router.push(`/search/${this.inputValue}`);
      } catch (error) {
        console.log(error);
      }
    }
  },
});
</script>
