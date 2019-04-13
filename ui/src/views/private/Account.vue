<template>
  <div class="account-page">
    <h1> Account </h1>
    <div>
      <h2> FirstName : {{ firstname }} </h2>
    </div>
    <div>
      <h2> LastName : {{ lastname }} </h2>
    </div>
    <div>
      <h2> Email : {{ email }} </h2>
    </div>
    <div>
      <h2> Username : {{ username }} </h2>
    </div>
    <div>
      <h2> Address : {{ doorNumber }} {{ street }} </h2>
    </div>
    <div>
      <h2> Appartement : {{ apartment }} </h2>
    </div>
    <div>
      <h2> City : {{ city }} </h2>
    </div>
    <div>
      <h2> Country : {{ country }} </h2>
    </div>
    <div class="buttons-wrapper">
      <Button
        accent
        @click="editAccount"
      >
        Edit info
      </Button>
    </div>
  </div>
</template>

<script>
import { API } from '@/js/api/api'
import Button from '@/components/buttons/Button'

export default {
  name: 'Account',

  components: {
    Button
  },

  data () {
    return {
      firstname: '',
      lastname: '',
      email: '',
      username: '',
      doorNumber: '',
      apartment: '',
      street: '',
      city: '',
      country: ''
    }
  },
  methods: {
    editAccount () {
      this.$router.push({ path: `${this.$route.params.id}/edit` })
    }
  },
  async beforeMount () {
    let userId = this.$route.params.id
    let data = await API.getUserById(userId)
    this.username = data.username

    let dataAccount = await API.getAccount(userId)
    this.email = dataAccount.email
    this.firstname = dataAccount.firstName
    this.lastname = dataAccount.lastName

    let dataAddress = await API.getAddress(userId)
    this.apartment = dataAddress[0].apartment
    this.city = dataAddress[0].apartment
    this.country = dataAddress[0].country
    this.doorNumber = dataAddress[0].number
    this.street = dataAddress[0].street
  }
}
</script>

<style>

</style>
