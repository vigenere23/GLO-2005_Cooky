<template>
  <div>
    <div class="signup-page" />
    <h1> Signup </h1>
    <div>
      <div>
        <input
          type="text"
          placeholder="firstName"
          v-model="firstname"
        >
      </div>
      <div>
        <input
          type="text"
          placeholder="lastName"
          v-model="lastname"
        >
      </div>
      <div>
        <input
          type="text"
          placeholder="email"
          v-model="email"
        >
      </div>
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
          placeholder="Door number"
          v-model="number"
        >
      </div>
      <div>
        <input
          type="text"
          placeholder="apartment"
          v-model="apartment"
        >
      </div>
      <div>
        <input
          type="text"
          placeholder="street"
          v-model="street"
        >
      </div>
      <div>
        <input
          type="text"
          placeholder="city"
          v-model="city"
        >
      </div>
      <div>
        <input
          type="text"
          placeholder="country"
          v-model="country"
        >
      </div>
      <div>
        <input
          type="password"
          placeholder="password"
          v-model="password"
        >
      </div>
      <div>
        <input
          type="password"
          placeholder="confirm password"
          v-model="confirmPassword"
        >
      </div>
      <div>
        <button
          class="blue"
          @click="signUp"
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
  name: 'Signup',

  components: {

  },

  data () {
    return {
      firstname: '',
      lastname: '',
      email: '',
      username: '',
      password: '',
      confirmPassword: '',
      number: '',
      apartment: '',
      street: '',
      city: '',
      country: ''
    }
  },

  methods: {
    async signUp () {
      if (parseInt(this.number).isNaN) {
        window.alert('door number must be a number')
      } else if (this.firstname.length === 0 || this.lastname.length === 0 || this.email.length === 0 || this.username.length === 0 || this.password === 0 ||
        this.number.length === 0 || this.street.length === 0 || this.city.length === 0 || this.country.length === 0) {
        window.alert('there is an empty field')
      } else {
        if (this.password === this.confirmPassword) {
          const data = await API.addNewUser(this.firstname, this.lastname, this.email,
            this.username, this.password, this.number, this.apartment, this.street, this.city, this.country)
          if (!data) {
            window.alert('username already used')
          } else {
            await Cookies.set('cookyUsername', this.username)
            await Cookies.set('cookyPassword', this.password)
            const userId = data.id
            await this.$router.push({ path: `/users/${userId}` })
          }
        } else {
          this.confirmPassword = ''
          window.alert('password and confirm password are not the same')
        }
      }
    }
  }
}
</script>

<style>
.blue {
  background-color: blue
}
</style>
