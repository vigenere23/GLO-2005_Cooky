<template>
  <div id="app">
    <DefaultLayout>
      <router-view />
    </DefaultLayout>
  </div>
</template>

<script>
import DefaultLayout from '@/layouts/DefaultLayout'

export default {
  name: 'App',
  components: {
    DefaultLayout
  }
}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

body {
  margin: 0;
  font-family: "Roboto", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: $primary-text-color;

  * {
    box-sizing: border-box;
    position: relative;
  }

  a {
    color: inherit;
    text-decoration: none;
    cursor: pointer;
  }

  button {
    border: none;
    background: none;
  }

  h1, h2, h3 {
    font-family: "Merriweather", Helvetica, Arial, sans-serif;
    font-weight: 300;
  }

  h1 {
    font-size: 48px;
    margin-top: 0;
  }
}
</style>
