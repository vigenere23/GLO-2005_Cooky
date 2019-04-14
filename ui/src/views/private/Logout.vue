<template>
  <div />
</template>

<script>
import Cookies from 'js-cookie'
import { mapMutations } from 'vuex'

export default {

  name: 'Logout',

  methods: mapMutations('user', ['clear']),

  async mounted () {
    this.clear()
    Cookies.remove('cooky_token')
    this.$router.push('/home')
  }
}
</script>
