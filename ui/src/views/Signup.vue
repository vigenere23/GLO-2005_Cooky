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
        v-model="number"
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
        type="password"
        v-model="password"
      />
      <LabelInput
        label="Confirm password"
        type="password"
        v-model="confirmPassword"
      />
      <Button
        accent
        right
        :disable="!allValid"
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
      number: '',
      apartment: '',
      street: '',
      city: '',
      country: ''
    }
  },

  computed: {
    validNumber () {
      return this.number === '' || !isNaN(parseInt(this.number))
    },
    validPasswordConfirmation () {
      return this.password === this.confirmPassword
    },
    noEmptyFields () {
      return this.firstname && this.lastname &&
        this.email && this.username &&
        this.street && this.city && this.country &&
        this.password && this.confirmPassword
    },
    allValid () {
      return this.validNumber && this.noEmptyFields
    }
  },

  methods: {
    async signup () {
      if (this.validate()) {
        const userId = await API.addNewUser(this.firstname, this.lastname, this.email,
          this.username, this.password, this.number, this.apartment, this.street, this.city, this.country)
        if (!userId) {
          EventBus.$emit('toast', { type: 'error', message: 'Username already exists' })
        } else {
          await Cookies.set('cookyUsername', this.username)
          await Cookies.set('cookyPassword', this.password)
          await this.$router.push({ path: `/users/${userId}` })
        }
      }
    },
    validate () {
      if (!this.validNumber) {
        EventBus.$emit('toast', { type: 'error', message: 'Invalid door number' })
        return false
      }
      if (!this.validPasswordConfirmation) {
        EventBus.$emit('toast', { type: 'error', message: 'Passwords do not match' })
        this.password = this.confirmPassword = ''
        return false
      }
      if (!this.noEmptyFields) {
        EventBus.$emit('toast', { type: 'error', message: 'Please fill all fields' })
        return false
      }
      return true
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
