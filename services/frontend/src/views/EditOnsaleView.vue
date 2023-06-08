<template>
    <section>
      <h2>编辑</h2>
      <hr/><br/>
  
      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="name" class="form-label">药品:</label>
          <p class="form-control-static">{{onsale.Mid.name}}</p>
        </div>
        <div class="mb-3">
          <label for="amount" class="form-label">数量:</label>
          <input type="number" name="amount" v-model="form.amount" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="price" class="form-label">价格:</label>
          <input type="number" step="0.01" name="price" v-model="form.price" class="form-control" />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
    </section>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'EditOnsale',
    props: ['id'],
    data() {
      return {
        form: {
          amount: 0,
          price: 0,
        },
      };
    },
    created: function() {
      this.GetPharmacy();
    },
    computed: {
      ...mapGetters({ onsale: 'stateOnsale' }),
    },
    methods: {
      ...mapActions(['updateOnsale', 'viewOnsale']),
      async submit() {
      try {
        let onsale = {
          id: this.id,
          form: this.form,
        };
        await this.updateOnsale(onsale);
        // await this.viewOnsale(this.id);
        this.$router.push(`/medicine/${this.onsale.Pid.id}`);
      } catch (error) {
        console.log(error);
      }
      },
      async GetPharmacy() {
        try {
          await this.viewOnsale(this.id);
          this.form.amount = this.onsale.amount;
          this.form.price = this.onsale.price;
        } catch (error) {
          console.error(error);
        this.$router.push(`/medicine/${this.onsale.Pid.id}`);
        }
      }
    },
  });
  </script>
  