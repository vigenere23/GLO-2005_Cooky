<template>
  <div class="account-page">
    <h1>Account</h1>
    <button
      @click.native="this.myFonction"
      id="myButton"
    >
      Test
    </button>
  </div>
</template>

<script>

export default {
  name: 'Account',
  data () {
    return {
      name: 'hello'
    }
  },
  methods: {
    async myFunction () {
      this.name = 'alpha'
      console.log(this.name)
      window.alert('im a king')
    }
  }
}
</script>

<style>

#myButton{
  background-color: red
}

</style>
