<template>
    <section>
      <h2>编辑</h2>
      <hr/><br/>
  
      <form @submit.prevent="submit">
        <div class="mb-3">
          <label for="name" class="form-label">药店名:</label>
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
        <button type="submit" class="btn btn-primary">保存</button>
      </form>
    </section>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'EditPharmacy',
    props: ['id'],
    data() {
      return {
        form: {
          name: '',
          contact: '',
          addr: '',
        },
      };
    },
    created: function() {
      this.GetPharmacy();
    },
    computed: {
      ...mapGetters({ pharmacy: 'statePharmacy' }),
    },
    methods: {
      ...mapActions(['updatePharmacy', 'viewPharmacy']),
      async submit() {
      try {
        let pharmacy = {
          id: this.id,
          form: this.form,
        };
        await this.updatePharmacy(pharmacy);
        this.$router.push('/profile');
      } catch (error) {
        console.log(error);
      }
      },
      async GetPharmacy() {
        try {
          await this.viewPharmacy(this.id);
          this.form.name = this.pharmacy.name;
          this.form.contact = this.pharmacy.contact;
          this.form.addr = this.pharmacy.addr;
        } catch (error) {
          console.error(error);
          this.$router.push('/profile');
        }
      }
    },
  });
  </script>
  