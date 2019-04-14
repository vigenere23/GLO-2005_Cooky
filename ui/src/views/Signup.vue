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
import { mapActions } from 'vuex'

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
      return !isNaN(parseInt(this.number))
    },
    validApartement () {
      return this.apartment === '' || !isNaN(parseInt(this.apartment))
    },
    validPasswordConfirmation () {
      return this.password === this.confirmPassword
    },
    noEmptyFields () {
      return this.firstname && this.lastname &&
        this.email && this.username && this.street &&
        this.number && this.city && this.country &&
        this.password && this.confirmPassword
    },
    allValid () {
      return this.validNumber && this.validApartement && this.noEmptyFields
    }
  },

  methods: {
    ...mapActions('user', ['loadAll']),
    async signup () {
      if (this.validate()) {
        const registeringData = {
          user: {
            username: this.username
          },
          account: {
            firstName: this.firstname,
            lastName: this.lastname,
            email: this.email,
            password: this.password
          },
          address: {
            number: parseInt(this.number),
            street: this.street,
            apartment: parseInt(this.apartment) || null,
            city: this.city,
            country: this.country
          }
        }
        const registeringResponse = await API.signup(registeringData)
        if (registeringResponse && !registeringResponse.error) {
          const loginData = {
            username: registeringResponse.username,
            password: this.password
          }
          const loginResponse = await API.login(loginData)
          if (loginResponse && !loginResponse.error) {
            Cookies.set('cooky_token', 'JWT ' + loginResponse.token)
            this.$router.push(`/users/${loginResponse.id}`)
            this.loadAll()
          }
        }
      }
    },
    validate () {
      if (!this.validNumber) {
        EventBus.$emit('toast', { type: 'error', message: 'Invalid door number' })
        return false
      }
      if (!this.validApartement) {
        EventBus.$emit('toast', { type: 'error', message: 'Invalid apartement number' })
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
