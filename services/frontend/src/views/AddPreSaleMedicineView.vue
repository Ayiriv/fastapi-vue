<template>
    <div>
      <section>
        <h1>添加药品信息</h1>
        <hr/><br/>
  
        <form @submit.prevent="submit">
          <div class="mb-3">
            <label for="name" class="form-label">药品:</label>
            <div v-if="medicines && medicines.length">
            <select v-model="form.Mid_id" class="form-control">
              <option v-for="medicine in medicines" :key="medicine.id" :value="medicine.id">{{ medicine.name }}</option>
            </select>
          </div>
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
          <div v-if="hasError" class="mb-3 text-danger">
          药品已添加，请勿重复操作
        </div>
          <br/>
          <button type="submit" class="btn btn-primary">添加</button>
        </form>
      </section>
  
      <br/><br/>
  
    </div>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'AddPreSaleMedicine',
    data() {
      return {
        form: {
          Mid_id:0,
          Pid_id:parseInt(this.$route.params.id),
          amount: 0,
          price: 0,
          arrive: new Date(),
        },
        hasError: false,
      };
    },
    created: function() {
      this.pharmacyId = this.$route.params.id;
      return this.$store.dispatch('getMedicines');
    },
    computed: {
      ...mapGetters({ medicines: 'stateMedicines', check: 'stateCheck'}),
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
      ...mapActions(['createPresale', 'checkPresalesExistence', 'updatePresale']),
      async submit() {
        await this.checkPresalesExistence(this.form.Mid_id);
        if (this.check) {
          this.hasError = true;
          // 进行错误提示
        } else {
          this.hasError = false;
          await this.createPresale(this.form);
          this.$router.push(`/medicine/${this.pharmacyId}`);
        }
      },
    },
  });
  </script>
  