<template>
  <div class="account-edit-page">
    <h1> Edit Account  </h1>
    <div class="inputs-wrapper">
      <LabelInput
        label="Email"
        v-model="email"
      />
    </div>
    <div class="buttons-wrapper">
      <Button
        accent
        right
        @click="changeEmail"
      >
        Change email
      </Button>
    </div>
    <div class="inputs-wrapper">
      <LabelInput
        label="Door number"
        v-model="doorNumber"
      />
    </div>
    <div class="buttons-wrapper">
      <Button
        accent
        right
        @click="changeDoorNumber"
      >
        Change door number
      </Button>
    </div>
    <div class="inputs-wrapper">
      <LabelInput
        label="Apartment"
        v-model="apartment"
      />
    </div>
    <div class="buttons-wrapper">
      <Button
        accent
        right
        @click="changeApartment"
      >
        Change apartment
      </Button>
    </div>
    <div class="inputs-wrapper">
      <LabelInput
        label="Street"
        v-model="street"
      />
    </div>
    <div class="buttons-wrapper">
      <Button
        accent
        right
        @click="changeStreet"
      >
        Change street
      </Button>
    </div>
    <div class="inputs-wrapper">
      <LabelInput
        label="City"
        v-model="city"
      />
    </div>
    <div class="buttons-wrapper">
      <Button
        accent
        right
        @click="changeCity"
      >
        Change city
      </Button>
    </div>
    <div class="inputs-wrapper">
      <LabelInput
        label="Country"
        v-model="country"
      />
    </div>
    <div class="buttons-wrapper">
      <Button
        accent
        right
        @click="changeCountry"
      >
        Change country
      </Button>
    </div>
    <div class="inputs-wrapper">
      <LabelInput
        label="Password"
        v-model="password"
      />
      <LabelInput
        label="Confirm password"
        v-model="confirmPassword"
      />
    </div>
    <div class="buttons-wrapper">
      <Button
        accent
        right
        @click="changePassword"
      >
        Change password
      </Button>
    </div>
  </div>
</template>

<script>
import { API } from '@/js/api/api'
import { EventBus } from '@/js/eventbus'
import Button from '@/components/buttons/Button'
import LabelInput from '@/components/inputs/LabelInput'

export default {
  name: 'AccountEdit',

  components: {
    Button,
    LabelInput
  },

  data () {
    return {
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
    async changePassword () {
      if (this.password === this.confirmPassword && this.password.length !== 0) {
        const userId = this.$route.params.id
        API.modifyPassword(userId, this.password)
        EventBus.$emit('toast', { type: 'warning', message: 'Password modified' })
        this.password = ''
        this.confirmPassword = ''
      } else {
        EventBus.$emit('toast', { type: 'error', message: 'Passwords do not concord' })
        this.confirmPassword = ''
      }
    },

    async changeCountry () {
      if (this.country.length !== 0) {
        const userId = this.$route.params.id
        API.modifyCountry(userId, this.country)
        EventBus.$emit('toast', { type: 'warning', message: 'Country modified' })
        this.country = ''
      } else {
        EventBus.$emit('toast', { type: 'error', message: 'Empty field' })
      }
    },

    async changeCity () {
      if (this.city.length !== 0) {
        const userId = this.$route.params.id
        API.modifyCity(userId, this.city)
        EventBus.$emit('toast', { type: 'warning', message: 'City modified' })
        this.city = ''
      } else {
      }
    },

    async changeStreet () {
      if (this.street.length !== 0) {
        const userId = this.$route.params.id
        API.modifyStreet(userId, this.street)
        EventBus.$emit('toast', { type: 'warning', message: 'Street modified' })
        this.street = ''
      } else {
        EventBus.$emit('toast', { type: 'error', message: 'Empty field' })
      }
    },

    async changeApartment () {
      const userId = this.$route.params.id
      API.modifyApartment(userId, this.apartment)
      EventBus.$emit('toast', { type: 'warning', message: 'Apartment modified' })
      this.apartment = ''
    },

    async changeDoorNumber () {
      if (this.doorNumber.length !== 0 && !parseInt(this.doorNumber).isNaN) {
        const userId = this.$route.params.id
        API.modifyDoorNumber(userId, this.doorNumber)
        EventBus.$emit('toast', { type: 'warning', message: 'Door number modified' })
        this.doorNumber = ''
      } else {
        EventBus.$emit('toast', { type: 'error', message: 'Empty field or door is not a number' })
      }
    },

    async changeEmail () {
      console.log('work')
      if (this.email.length !== 0) {
        const userId = this.$route.params.id
        API.modifyEmail(userId, this.email)
        EventBus.$emit('toast', { type: 'warning', message: 'Email modified' })
        this.email = ''
      } else {
        EventBus.$emit('toast', { type: 'error', message: 'Empty field' })
      }
    }
  }
}
</script>
