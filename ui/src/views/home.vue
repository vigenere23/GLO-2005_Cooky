<template>
  <div>
    <h1> Welcome to Cookie </h1>
    <div>
      <button
        class="red"
        @click="goToLogIn"
      >
        LogIn
      </button>

      <button
        class="blue"
        @click="gotToSignUp"
      >
        Signup
      </button>
    </div>
  </div>
</template>

<script>
import { API } from '@/js/api/api'
import * as Cookies from 'js-cookie'
export default {
  name: 'Home',

  methods: {
    goToLogIn () {
      this.$router.push({ path: '/login' })
    },

    gotToSignUp () {
      this.$router.push({ path: '/signup' })
    }
  },
  async beforeMount () {
    const password = Cookies.get('cookyPassword')
    const username = Cookies.get('cookyUsername')
    if (!((password === null || password === undefined || password === '') || (username === null || username === undefined || username === ''))) {
      const userId = await API.login(username, password)
      console.log(userId)
      this.$router.push({ path: `/users/${userId.id}` })
    }
  }
}
</script>

<style>
.red {
    background-color: red;
}

.blue {
    background-color: blue;
}

</style>
