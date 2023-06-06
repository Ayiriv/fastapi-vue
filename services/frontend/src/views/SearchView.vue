<template>
    <div>
      <section>
        <h1>Search Notes</h1>
        <hr /><br />
  
        <form @submit.prevent="search">
          <div class="mb-3">
            <label for="searchTerm" class="form-label">Search Term:</label>
            <input type="text" name="searchTerm" v-model="searchTerm" class="form-control" />
          </div>
          <button type="submit" class="btn btn-primary">Search</button>
        </form>
      </section>
  
      <br /><br />
  
      <section>
        <h1>Search Results</h1>
        <hr /><br />
  
        <div v-if="searchResults.length">
          <div v-for="result in searchResults" :key="result.id" class="notes">
            <div class="card" style="width: 18rem;">
              <div class="card-body">
                <ul>
                  <li><strong>Note Title:</strong> {{ result.title }}</li>
                  <li><strong>Note Contact:</strong> {{ result.contact }}</li>
                  <li><strong>Author:</strong> {{ result.author.username }}</li>
                  <li><router-link :to="{ name: 'Note', params: { id: result.id } }">View</router-link></li>
                </ul>
              </div>
            </div>
            <br />
          </div>
        </div>
  
        <div v-else>
          <p>No search results found.</p>
        </div>
      </section>
    </div>
  </template>
  
  <script>
  
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'SearchView',
    data() {
      return {
        searchTerm: '',
      };
    },
    computed: {
      ...mapGetters({ searchResults: 'stateSearchResults' }),
    },
    methods: {
      ...mapActions(['searchNotes']),
      async search() {
        await this.searchNotes(this.searchTerm);
      },
    },
  });
  </script>
  