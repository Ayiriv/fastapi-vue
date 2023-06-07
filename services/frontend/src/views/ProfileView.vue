<template>
  <section>
    <h2>基本信息</h2>
    <hr/><br/>
    <div>
      <p><strong>Username:</strong> <span>{{ user.username }}</span></p>
      <p><button @click="deleteAccount()" class="btn btn-primary">Delete Account</button></p>
    </div>
  </section>
  <hr/><br/><br/>
  <section>
    <h2>药店信息</h2>
    <hr/><br/>
    <p><router-link :to="{name: 'AddPharmacy'}" class="btn btn-primary">添加</router-link></p>
    <hr/><br/>
    <div v-if="mypharmacies && mypharmacies.length">
        <div v-for="pharmacy in mypharmacies" :key="pharmacy.id" class="pharmacies">
          <div class="card" style="width: 18rem;">
            <div class="card-body">
              <ul>
                <li><strong>药店名:</strong> {{ pharmacy.name }}</li>
                <li><strong>联系方式:</strong> {{ pharmacy.contact }}</li>
                <li><strong>地址:</strong> {{ pharmacy.addr }}</li>
                <li><router-link :to="{name: 'EditPharmacy', params:{id: pharmacy.id}}" class="btn btn-primary">编辑</router-link></li>
                <li><button @click="removePharmacy(pharmacy.id)" class="btn btn-secondary">删除</button></li>
              </ul>
            </div>
          </div>
          <br/>
        </div>
      </div>
  </section>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'ProfileView',
  created: function() {
    return this.$store.dispatch('viewMe'), this.$store.dispatch('getPharmaciesByOwner', this.user.id);
  },
  computed: {
    ...mapGetters({user: 'stateUser' , mypharmacies: 'stateMyPharmacies'}),
  },
  methods: {
    ...mapActions(['deleteUser', 'deletePharmaciesByOwner', 'deletePharmacy']),
    async deleteAccount() {
      try {
        await this.deletePharmaciesByOwner(this.user.id);
        await this.deleteUser(this.user.id);
        await this.$store.dispatch('logOut');
        this.$router.push('/');
      } catch (error) {
        console.error(error);
      }
    },
    async removePharmacy(pharmacyId) {
      try {
        await this.deletePharmacy(pharmacyId);
        await this.$store.dispatch('getPharmaciesByOwner', this.user.id); //刷新mypharmacies
      } catch (error) {
        console.error(error);
      }
    }
  },
});
</script>
