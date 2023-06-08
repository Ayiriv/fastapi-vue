<template>
  <div>
    <div class="search-bar">
      <input type="text" placeholder="请输入关键词" v-model="inputValue" class="form-control search-input" />
      <label class="radio-inline">
        <input type="radio" name="inlineRadioOptions" id="inlineRadio1" value="ph" v-model="selectedOption"> 药店
      </label>
      <label class="radio-inline">
        <input type="radio" name="inlineRadioOptions" id="inlineRadio2" value="md" v-model="selectedOption"> 药品
      </label>
      <br /><br />
      <button @click="search" class="btn btn-primary">Search</button>
    </div>
    
      <h2>搜索结果</h2>
      <hr /><br />
        <!-- <div class="result-item">
          <div v-for="result in searchResults" :key="result.id" class="card">
            <div class="card" style="width: 18rem;">
              <div class="card-body">
                <p><strong>药店名:</strong> {{ result.name }}</p>
                <p><strong>联系方式:</strong> {{ result.contact }}</p>
                <p><strong>地址:</strong> {{ result.addr }}</p>
              </div>
            </div>
          </div>
        </div> -->

      <div class="search-results" v-if="searchResults && searchResults.length">
        <div class="result-item">
        <div v-for="result in searchResults" :key="result.id" class="card">
          <div class="card" style="width: 18rem;">
            <div class="card-body">
              <p><strong>药店名:</strong> {{ result.name }}</p>
              <p><strong>联系方式:</strong> {{ result.contact }}</p>
              <p><strong>地址:</strong> {{ result.addr }}</p>
            </div>
          </div>
        </div>
      </div>
      </div>
        <div class="search-results" v-if="searchResultsOn && searchResultsOn.length">
          <div class="result-item">
          <div v-for="result in searchResultsOn" :key="result.id" class="card">
            <div class="card" style="width: 18rem;">
              <div class="card-body">
                <p><strong>药品:</strong>{{ result.Mid.name }}</p>
                <p><strong>数量:</strong>{{ result.amount }}件</p>
                <p><strong>价格:</strong>{{ result.price }}元</p>
              </div>
            </div>
          </div>
        </div>
        </div>
        <div class="search-results" v-if="searchResultsPre && searchResultsPre.length">
          <div class="result-item">
          <div v-for="result in searchResultsPre" :key="result.id" class="card">
            <div class="card" style="width: 18rem;">
              <div class="card-body">
                <p><strong>药品:</strong>{{ result.Mid.name }}</p>
                <p><strong>数量:</strong>{{ result.amount }}件</p>
                <p><strong>价格:</strong>{{ result.price }}元</p>
                <p><strong>到货时间:</strong>{{ result.arrive }}</p>
              </div>
            </div>
          </div>
        </div>
        </div>
    
  </div>
</template>

<style>
.result-item {
  display: flex;
  flex-wrap: wrap;
}

.card {
  flex: 0 0 18rem;
  margin: 10px;
}
</style>  
  
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'SearchView',
    data() {
      return {
        inputValue: '',
        searchResults: [],
        searchResultsOn: [],
        searchResultsPre: [],
        selectedOption: this.$route.params.type
      };
    },
    created: async function() {
      // 从路由参数中获取搜索关键字
      this.inputValue = this.$route.params.query;
  
      // 执行搜索
      await this.search();
    },
    computed : {
      ...mapGetters({pharmacies: 'statePharmacies', onsales: 'stateOnsales', preonsales: 'statePresales'}),
    },
    methods: {
      ...mapActions(['searchPharmacies', 'searchOnsales', 'searchPresales']),
      async search () {
        this.searchResults = [];
        this.searchResultsOn = [];
        this.searchResultsPre = [];
        if(this.selectedOption == 'ph') {
          try {
            console.log("click1", this.inputValue);
            await this.searchPharmacies(this.inputValue);
            this.searchResults = this.pharmacies;
            console.log(this.searchResults);
          } catch (error) {
            console.log(error);
          }
        } else if(this.selectedOption == 'md'){
          try {
            console.log("click2", this.inputValue);
            await this.searchOnsales(this.inputValue);
            await this.searchPresales(this.inputValue);
            this.searchResultsOn = this.onsales;
            this.searchResultsPre = this.preonsales;
            console.log('s1', this.searchResults);
            console.log('s2', this.searchResultsSub);
          } catch (error) {
            console.log(error);
          }
        }
      }
    },
  });
  </script>
  
  <!-- 这里是你的样式代码 -->
  
  