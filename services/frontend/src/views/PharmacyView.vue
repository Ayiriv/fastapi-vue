<template>
  <div>
    <section>
      <h1>填写药店信息</h1>
      <hr/><br/>

      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="name" class="form-label">药店名称:</label>
          <input type="text" name="name" v-model="form.name" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="contact" class="form-label">联系方式:</label>
          <input type="text" name="contact" v-model="form.contact" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="addr" class="form-label">地址:</label>
          <input type="text" name="addr" v-model="form.addr" class="form-control" />
        </div>
        <br/>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </section>

    <br/><br/>

  </div>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'PharmacyView',
  data() {
    return {
      form: {
        name: '',
        addr: '',
        contact: '',
      },
    };
  },
  created: function() {
    return this.$store.dispatch('getPharmacies');
  },
  computed: {
    ...mapGetters({ notes: 'statePharmacies'}),
  },
  methods: {
    ...mapActions(['createPharmacy']),
    async submit() {
      await this.createPharmacy(this.form);
    },
  },
});
</script>
