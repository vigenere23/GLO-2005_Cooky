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
      if (this.password === this.confirmPassword) {
        API.addNewUser(this.firstname, this.lastname, this.email,
          this.username, this.password, this.number, this.apartment, this.street, this.city, this.country)
      } else {
        this.confirmPassword = ''
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
