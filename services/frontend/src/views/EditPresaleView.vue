<template>
    <section>
      <h2>编辑</h2>
      <hr/><br/>
  
      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="name" class="form-label">药品:</label>
          <p class="form-control-static">{{presale.Mid.name}}</p>
        </div>
        <div class="mb-3">
          <label for="amount" class="form-label">数量:</label>
          <input type="number" name="amount" v-model="form.amount" class="form-control" />
        </div>
        <div class="mb-3">
          <label for="price" class="form-label">价格:</label>
          <input type="number" step="0.01" name="price" v-model="form.price" class="form-control" />
        </div>
        <div class="mb-3">
            <label for="arrive" class="form-label">到货日期:</label>
            <input type="datetime-local" name="arrive" v-model="arriveAsDateTimeLocal" class="form-control" />
          </div>
        <button type="submit" class="btn btn-primary">保存</button>
      </form>
    </section>
  </template>
  
  <script>
  
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'EditPresale',
    props: ['id'],
    data() {
      return {
        form: {
          amount: 0,
          price: 0,
          arrive: new Date(),
        },
      };
    },
    created: function() {
      this.GetPharmacy();
    },
    computed: {
      ...mapGetters({ presale: 'statePresale' }),
      arriveAsDateTimeLocal: {
        get: function() {
          let d = this.form.arrive;
          function pad(n) { return n<10 ? '0'+n : n }
          return d.getFullYear() + '-'
                + pad(d.getMonth()+1) + '-'
                + pad(d.getDate()) + 'T'
                + pad(d.getHours()) + ':'
                + pad(d.getMinutes());
        },
        set: function(val) {
          this.form.arrive = new Date(val);
        }
      },
    },
    methods: {
      ...mapActions(['updatePresale', 'viewPresale']),
      async submit() {
      try {
        let presale = {
          id: this.id,
          form: this.form,
        };
        await this.updatePresale(presale);
        this.$router.push(`/medicine/${this.presale.Pid.id}`);
      } catch (error) {
        console.log(error);
      }
      },
      async GetPharmacy() {
        try {
          await this.viewPresale(this.id);
          this.form.amount = this.presale.amount;
          this.form.price = this.presale.price;
        } catch (error) {
          console.error(error);
          this.$router.push(`/medicine/${this.presale.Pid.id}`);
        }
      }
    },
  });
  </script>
  