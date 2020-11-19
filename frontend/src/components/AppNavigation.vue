<template>
  <span>
    <v-navigation-drawer app v-model="drawer" :clipped="true" >
      <v-list>
        <template v-for="item in items">
          <router-link :key="item.title" :to="item.path">
            <v-list-item  link>
              <v-list-item-action>
                <v-icon>{{ item.icon }}</v-icon>
              </v-list-item-action>
              <v-list-item-content>
                <v-list-item-title>{{ item.title }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </router-link>
        </template>
      </v-list>

      <a href="admin">
        <v-list-item class="primary darken-2" link style="position: absolute; bottom:0; width: 100%">
          <v-list-item-action>
            <v-icon>mdi-lock</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Admin</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </a>
    </v-navigation-drawer>

    <v-app-bar app color="primary" :clipped-left="true">
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-spacer class="hidden-md-and-up"></v-spacer>
      <!-- <v-img
        class="mx-2"
        src="../assets/logo.png"
        max-height="40"
        max-width="40"
        contain
      ></v-img> -->
      <!-- <v-icon large class="mx-6">mdi-head-snowflake</v-icon> -->
      <v-icon large class="mx-6">mdi-hexagon-slice-6</v-icon>

      <v-toolbar-title class="hidden-sm-and-down">{{appTitle}}</v-toolbar-title>

      <v-spacer class="hidden-sm-and-down"></v-spacer>
      <router-link v-if="!currentUser" to="/login" class="hidden-sm-and-down nav-link mx-2">login</router-link>
      <v-btn fab small depressed v-if="currentUser" color="secondary" class="hidden-sm-and-down" to="/profile">
        <v-icon>mdi-account</v-icon>
      </v-btn>
    </v-app-bar>
  </span>

</template>

<script>
// import { eventBus } from '@/main'
export default {
  name: 'AppNavigation',
  data () {
    return {
      appTitle: 'Thermal Comfort Testing',
      drawer: false,
      items: [
        { title: 'Participate', icon: 'mdi-chevron-right-circle', path: '/participate' },
        { title: 'User', icon: 'mdi-account', path: '/user' },
        { title: 'Test Management', icon: 'mdi-clipboard-edit', path: '/manage' },
      ]
    }
  },
  props: {
  },
  computed: {
    currentUser: function () {
      return this.$store.state.auth.user
    }
  },
  methods: {    
    userRedirect: function () {
      if (!this.currentUser) {
        this.$router.push('/login')
      } else {
        this.$router.push('/profile')
      }
    }  
  }
}
</script>

<style scoped>
a {
    color: white;
    text-decoration: none;
}
.nav-link {
  color: black;
}
</style>
