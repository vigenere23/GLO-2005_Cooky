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
        type="password"
        :validate="(value) => !!value"
        v-model="password"
      />
      <Button
        accent
        :disable="!allValid"
        @click="login"
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

  computed: {
    allValid () {
      return this.username && this.password
    }
  },

  methods: {
    async login () {
      const loginData = {
        username: this.username,
        password: this.password
      }
      const loginResponse = await API.login(loginData)
      if (loginResponse && !loginResponse.error) {
        Cookies.set('token', 'JWT ' + loginResponse.token)
        this.$router.push(`/users/${loginResponse.id}`)
        // TODO call loadInfos to store
      } else {
        this.username = ''
        this.password = ''
      }
    }
  },
  beforeMount () {
    Cookies.remove('token')
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
