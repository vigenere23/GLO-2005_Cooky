<template>
  <div class="logout">
    <h1>Logout</h1>
    <button
      class="blue"
      @click="goToHomePage"
    >
      Logout
    </button>
  </div>
</template>

<script>
import * as Cookies from 'js-cookie'

export default {
  name: 'Logout',

  methods: {
    async goToHomePage () {
      await Cookies.set('cookyUsername', '')
      await Cookies.set('cookyPassword', '')
      this.$router.push({ path: '/home' })
    }
  }
}
</script>
<style>
.blue {
  background-color: blue;
}
</style>
