<template>
  <div class="user">
   
  </div>

</template>

<script>
import axios from 'axios'
export default {
  name: 'User',
  components: {
  },
  data: function () {
    return {
        user: null
    }
  },
  methods: {
    getUser (id) {
      axios.get('/api/user/' + id + '/')
        .then(response => {
          console.log(response.data)
          this.user = response.data
        })
        .catch(error => console.log(error))
    }
  },
  created () {

  }
}
</script>

<style scoped>
</style>

