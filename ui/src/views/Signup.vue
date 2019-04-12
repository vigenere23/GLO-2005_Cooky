<template>
  <div>
    <div class="signup-page" />
    <h1> Signup </h1>
    <div class="inputs-wrapper">
      <LabelInput
        label="First name"
        v-model="firstname"
      />
      <LabelInput
        label="Last name"
        v-model="lastname"
      />
      <LabelInput
        label="Email"
        v-model="email"
      />
      <LabelInput
        label="Username"
        v-model="username"
      />
      <LabelInput
        label="Door number"
        v-model="doorNumber"
      />
      <LabelInput
        label="Apartment"
        v-model="apartment"
      />
      <LabelInput
        label="Street"
        v-model="street"
      />
      <LabelInput
        label="City"
        v-model="city"
      />
      <LabelInput
        label="Country"
        v-model="country"
      />
      <LabelInput
        label="Password"
        v-model="password"
      />
      <LabelInput
        label="Confirm password"
        v-model="confirmPassword"
      />
      <Button
        accent
        right
        @click="signup"
      >
        Signup
      </Button>
    </div>
  </div>
</template>

<script>
import { API } from '@/js/api/api'
import { EventBus } from '@/js/eventbus'
import Cookies from 'js-cookie'
import Button from '@/components/buttons/Button'
import LabelInput from '@/components/inputs/LabelInput'

export default {
  name: 'Signup',

  components: {
    Button,
    LabelInput
  },

  data () {
    return {
      firstname: '',
      lastname: '',
      email: '',
      username: '',
      password: '',
      confirmPassword: '',
      doorNumber: '',
      apartment: '',
      street: '',
      city: '',
      country: ''
    }
  },

  methods: {
    async signup () {
      if (parseInt(this.doorNumber).isNaN) {
        EventBus.$emit('toast', { type: 'error', message: 'Invalid door number' })
      } else if (this.firstname.length === 0 || this.lastname.length === 0 || this.email.length === 0 || this.username.length === 0 || this.password === 0 ||
        this.doorNumber.length === 0 || this.street.length === 0 || this.city.length === 0 || this.country.length === 0) {
        EventBus.$emit('toast', { type: 'error', message: 'Please fill all fields' })
      } else {
        if (this.password === this.confirmPassword) {
          const data = API.addNewUser(this.firstname, this.lastname, this.email,
            this.username, this.password, this.doorNumber, this.apartment, this.street, this.city, this.country)
          if (!data) {
            EventBus.$emit('toast', { type: 'error', message: 'Username already exists' })
          } else {
            console.log('user created')
            await Cookies.set('cookyUsername', this.username)
            await Cookies.set('cookyPassword', this.password)
            const userId = await API.getUserByUsername(this.username)
            this.$router.push({ path: `/users/${userId}` })
          }
        } else {
          this.confirmPassword = ''
          EventBus.$emit('toast', { type: 'error', message: 'Passwords do not concord' })
        }
      }
    }
  }
}
</script>

<style>
.inputs-wrapper {
  width: 100%;
  max-width: 320px;
  margin: auto;
}
</style>
