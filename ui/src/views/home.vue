<template>
  <div>
    <h1> Welcome to Cookie </h1>
    <div>
      <button
        class="red"
        @click="goToLogIn"
      >
        LogIn
      </button>

      <button
        class="blue"
        @click="gotToSignUp"
      >
        Signup
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home',

  methods: {
    goToLogIn () {
      this.$router.push({ path: '/login' })
    },

    gotToSignUp () {
      this.$router.push({ path: '/signup' })
    }
  }
}
</script>

<style>
.red {
    background-color: red;
}

.blue {
    background-color: blue;
}

</style>
