<template>
  <section>
    <form @submit.prevent="submit">
      <!-- 账号信息 -->
      <h4>注册</h4>
      <br />
      <div class="mb-3">
        <label for="username" class="form-label">Username:</label>
        <input type="text" name="username" v-model="user.username" class="form-control" />
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Password:</label>
        <input type="password" name="password" v-model="user.password" class="form-control" />
      </div>
      
      <hr />
      
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </section>
</template>

<script>
import { defineComponent } from 'vue';
import { mapActions } from 'vuex';

export default defineComponent({
  name: 'RegisterView',
  data() {
    return {
      user: {
        username: '',
        password: '',
      },
      pharmacy: {
        name: '',
        contact: '',
        address: '',
      },
    };
  },
  methods: {
    ...mapActions(['register']),
    async submit() {
      try {
        console.log("registering...");
        await this.register(this.user);
        console.log("finished registering");
        this.$router.push('/pharmacy');
        console.log("finished pushing");
      } catch (error) {
        throw 'Username already exists. Please try again.';
      }
    },
  },
});
</script>
