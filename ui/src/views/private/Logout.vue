<template>
  <div />
</template>

<script>
import Cookies from 'js-cookie'

export default {

  name: 'Logout',

  async mounted () {
    await Cookies.set('cookyUsername', '')
    await Cookies.set('cookyPassword', '')
    this.$router.push('/home')
  }
}
</script>
