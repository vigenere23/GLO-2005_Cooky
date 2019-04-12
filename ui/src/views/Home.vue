<template>
  <div>
    <h1>Welcome to Cooky</h1>
    <div class="buttons-wrapper">
      <Button @click="goToLogin">
        Login
      </Button>
      <Button
        accent
        @click="gotToSignup"
      >
        Signup
      </Button>
    </div>
  </div>
</template>

<script>
import Button from '@/components/buttons/Button'

export default {

  name: 'Home',

  components: {
    Button
  },

  methods: {
    goToLogin () {
      this.$router.push('/login')
    },

    gotToSignup () {
      this.$router.push('/signup')
    }
  }

}
</script>

<style lang="scss">
.buttons-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;

  > *:not(:last-child) {
    margin-right: 16px;
  }
}
</style>
