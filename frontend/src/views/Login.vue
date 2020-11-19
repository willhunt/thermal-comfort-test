<template>
  <v-card min-width="400" max-width="500">
    <v-form>
      <v-container>
        <v-col>
          <v-row>
            <v-text-field v-model="user.username" label="Username" :rules="nameRules" required></v-text-field>
          </v-row>
          <v-row>
            <v-text-field v-model="user.password" label="Password" type="password" required></v-text-field>
          </v-row>
          <v-row>
            <v-btn type="submit" color="secondary" @click="handleLogin">Submit</v-btn>
          </v-row>
        </v-col>
      </v-container>
    </v-form>
  </v-card>
</template>

<script>
import User from '../models/user';

export default {
  name: 'Login',
  data() {
    return {
      user: new User('', ''),
      loading: false,
      message: '',
      nameRules: [
        v => !!v || 'Name is required',
        v => v.length <= 10 || 'Name must be less than 10 characters',
      ]
    };
  },
  computed: {
    loggedIn() {
      return this.$store.state.auth.status.loggedIn;
    }
  },
  created() {
    if (this.loggedIn) {
      this.$router.push('/profile');
    }
  },
  methods: {
    handleLogin() {
      this.loading = true;
      if (this.user.username && this.user.password) {
        this.$store.dispatch('auth/login', this.user).then(
          () => {
            this.$router.push('/profile');
          },
          error => {
            this.loading = false;
            this.message =
              (error.response && error.response.data) ||
              error.message ||
              error.toString()
          }
        )
      }
    }
  }
};
</script>

<style scoped>
label {
  display: block;
  margin-top: 10px;
}
</style>