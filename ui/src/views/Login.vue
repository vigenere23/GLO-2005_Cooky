<template>
  <div>
    <div class="login-page" />
    <h1>Login</h1>
    <div class="inputs-wrapper">
      <LabelInput
        label="Username"
        :validate="(value) => !!value"
        v-model="username"
      />
      <LabelInput
        label="Password"
        :validate="(value) => !!value"
        v-model="password"
      />
      <Button
        accent
        @click="logIn"
      >
        Login
      </Button>
    </div>
  </div>
</template>

<script>
import Cookies from 'js-cookie'
import { API } from '@/js/api/api'
import LabelInput from '@/components/inputs/LabelInput'
import Button from '@/components/buttons/Button'

export default {

  name: 'Login',

  components: {
    LabelInput,
    Button
  },

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

<style lang="scss">
.inputs-wrapper {
  width: 100%;
  max-width: 240px;
  margin: auto;
}
</style>
