<template>
  <section>
    <h3>药店信息</h3>
    <hr/><br/>
    <div>
      <p><strong>药店名:</strong> <span>{{ pharmacy.name }}</span></p>
      <p><strong>联系方式:</strong> <span>{{ pharmacy.contact }}</span></p>
      <p><strong>地址:</strong> <span>{{ pharmacy.addr }}</span></p>
    </div>
  </section>
  <br/><br/>
  <section>
    <h3>在售药品</h3>
    <hr/>
    &nbsp;&nbsp;&nbsp;&nbsp;<router-link :to="{name: 'AddOnsaleMedicine', params:{id: this.pharmacyId}}" class="btn btn-primary">添加</router-link>
    <br/><br/><br/>
    <div v-if="onsales && onsales.length">
        <div v-for="onsale in onsales" :key="onsale.id">
          <div class="card" style="width: 18rem;">
            <div class="card-body">
                <p><strong>药品名:</strong> {{ onsale.Mid.name }}</p>
                <p><strong>数量:</strong> {{ onsale.amount }}</p>
                <p><strong>价格:</strong> {{ onsale.price }}</p>
                <p>
                  <router-link :to="{name: 'EditOnsale', params:{id: onsale.id}}" class="btn btn-primary">编辑</router-link>&nbsp;&nbsp;
                  <button @click="removeOnsale(onsale.id)" class="btn btn-danger">删除</button>&nbsp;&nbsp;
                </p>
            </div>
        </div>
          <br/>
    </div>
    </div>
  </section>
  <section>
    <br/><br/>
    <h3>预售药品</h3>
    <hr/>
    &nbsp;&nbsp;&nbsp;&nbsp;<router-link :to="{name: 'AddPresaleMedicine', params:{id: this.pharmacyId}}" class="btn btn-primary">添加</router-link>
    <br/><br/><br/>
    <div v-if="presales && presales.length">
        <div v-for="presale in presales" :key="presale.id">
          <div class="card" style="width: 18rem;">
            <div class="card-body">
                <p><strong>药品名:</strong> {{ presale.Mid.name }}</p>
                <p><strong>数量:</strong> {{ presale.amount }}</p>
                <p><strong>价格:</strong> {{ presale.price }}</p>
                <p><strong>到货日期:</strong> {{ presale.arrive }}</p>
                <p>
                  <router-link :to="{name: 'EditPresale', params:{id: presale.id}}" class="btn btn-primary">编辑</router-link>&nbsp;&nbsp;
                  <button @click="removePresale(presale.id)" class="btn btn-danger">删除</button>&nbsp;&nbsp;
                </p>
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
  name: 'MedicineView',
  created: function() {
    this.pharmacyId = this.$route.params.id;
    this.$store.dispatch('viewPharmacy', this.pharmacyId);
    this.$store.dispatch('getOnsalesByPharmacy', this.pharmacyId);
    this.$store.dispatch('getPresalesByPharmacy', this.pharmacyId);
  },
  computed: {
    ...mapGetters({user: 'stateUser' , pharmacy: 'statePharmacy', onsales: 'stateMyOnsales', presales: 'stateMyPresales'}),
  },
  methods: {
    ...mapActions(['deleteOnsale', 'getOnsalesByPharmacy', 'deletePresale', 'getPresalesByPharmacy']),
    async removeOnsale(OnsaleId) {
      try {
        await this.deleteOnsale(OnsaleId);
        await this.$store.dispatch('getOnsalesByPharmacy', this.pharmacyId); 
      } catch (error) {
        console.error(error);
      }
    },
    async removePresale(PresaleId) {
      try {
        await this.deletePresale(PresaleId);
        await this.$store.dispatch('getPresalesByPharmacy', this.pharmacyId); 
      } catch (error) {
        console.error(error);
      }
    }
  },
});
</script>
