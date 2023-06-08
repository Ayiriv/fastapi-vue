<template>
  <div>
    <div class="logo">
      <img src="../assets/logo.png" alt="Logo" />
      <h2>药品资源查询系统</h2>
    </div>
    <br />
    <div class="search-bar">
      <input type="text" placeholder="请输入关键词" name="search" v-model="inputValue" class="form-control search-input"/>
      <br />
      <label class="radio-inline">
        <input type="radio" name="inlineRadioOptions" id="inlineRadio1" value="ph" v-model="selectedOption"> 药店
      </label>&nbsp;
      <label class="radio-inline">
        <input type="radio" name="inlineRadioOptions" id="inlineRadio2" value="md" v-model="selectedOption"> 药品
      </label>

      <br /><br />
      <button @click="search" class="btn btn-primary">搜索</button>
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
import { mapActions } from 'vuex';

export default defineComponent({
  name: 'HomeView',
  data() {
    return {
      inputValue: '',
      pharmacyList: [],
      selectedOption: 'ph'
    };
  },
  methods: {
    ...mapActions(['searchPharmacies']),
    async search () {
      try {
        this.$router.push(`/search/${this.selectedOption}/${this.inputValue}`);
      } catch (error) {
        console.log(error);
      }
    }
  },
});
</script>
