<template>
  <div>
    <div class="search-bar">
      <input type="text" placeholder="请输入关键词" v-model="inputValue" class="form-control search-input" />
      <br /><br />
      <button @click="search" class="btn btn-primary">Search</button>
    </div>
    <div class="search-results" v-if="searchResults && searchResults.length">
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
        <table class="table table-bordered table-striped">
          <!-- 在这里添加表格的列和行来显示搜索结果 -->
          <!-- 使用 v-for 指令来显示你的搜索结果 -->
          <tr v-for="result in searchResults" :key="result.id">
            <td>{{ result.name }}</td>
            <td>{{ result.contact }}</td>
            <td>{{ result.addr }}</td>
          </tr>
        </table>
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
      };
    },
    created: async function() {
      // 从路由参数中获取搜索关键字
      this.inputValue = this.$route.params.query;
  
      // 执行搜索
      await this.search();
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
          this.searchResults = this.pharmacies;
          console.log(this.searchResults);
        } catch (error) {
          console.log(error);
        }
      }
    },
  });
  </script>
  
  <!-- 这里是你的样式代码 -->
  
  