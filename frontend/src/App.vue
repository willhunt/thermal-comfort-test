<template>
  <v-app>
    <AppNaviagtion />

    <v-content>
      <v-container fluid class="mt-5">
        <v-row align="center" justify="center">
          <router-view></router-view>
        </v-row>
      </v-container>
    </v-content>

    <v-footer app>
      <!-- -->
    </v-footer>
  </v-app>
</template>

<script>
import axios from 'axios'
import AppNaviagtion from './components/AppNavigation'

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.headers['Content-Type'] = 'application/json'
axios.defaults.withCredentials = true
axios.defaults.trailingSlash = true
axios.interceptors.request.use((config) => {
  if (config.addTrailingSlash && config.url[config.url.length - 1] !== '/') {
    config.url += '/'
  }
  return config
})

export default {
  name: 'App',

  components: {
    AppNaviagtion,
  },

  data: () => ({
    //
  }),
}
</script>
