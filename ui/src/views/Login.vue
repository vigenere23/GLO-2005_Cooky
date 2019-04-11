<template>
  <div>
    <div class="login-page" />
    <h1> Login </h1>
    <div>
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
          placeholder="password"
          v-model="password"
        >
      </div>
      <div>
        <button
          class="blue"
          @click="logIn"
        >
          Login
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',

  data () {
    return {
      email: '',
      password: ''
    }
  },

  methods: {
    async logIn () {
    }
  }
}
</script>

<style>
.blue {
  background-color: blue;
}
</style>
