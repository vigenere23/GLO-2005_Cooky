<template>
  <div>
    <div class="login-page" />
    <h1> Login </h1>
    <div>
      <div>
        <input
          type="text"
          placeholder="username"
          v-model="username"
        >
      </div>
      <div>
        <input
          type="text"
          placeholder="password"
          v-model="password"
        >
      </div>
      <div>
        <button
          class="blue"
          @click="logIn"
        >
          Login
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { API } from '@/js/api/api'
import * as Cookies from 'js-cookie'

export default {
  name: 'Login',

  data () {
    return {
      username: '',
      password: ''
    }
  },

  methods: {
    async logIn () {
      if (this.username.length === 0 || this.password === 0) {
        window.alert('you have an empty field')
      } else {
        const userId = await API.login(this.username, this.password)
        if (!userId) {
          window.alert('email or password is invalid')
        } else {
          await Cookies.set('cookyPassword', this.password)
          await Cookies.set('cookyUsername', this.username)
          this.$router.push({ path: `/users/${userId}` })
        }
      }
    }
  },
  async beforeMount () {
    const password = Cookies.get('cookyPassword')
    const username = Cookies.get('cookyUsername')
    if (!((password === null || password === undefined || password === '') || (username === null || username === undefined || username === ''))) {
      const userId = await API.login(username, password)
      this.$router.push({ path: `/users/${userId}` })
    }
  }
}
</script>

<style>
.blue {
  background-color: blue;
}
</style>
