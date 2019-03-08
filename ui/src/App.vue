<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style lang="scss">
@import '~@/assets/scss/variables';

body {
  margin: 0;
}

#app {
  font-family: "Roboto", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: $primary-text-color;

  * {
    box-sizing: border-box;
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
    font-family: "Lora", Helvetica, Arial, sans-serif;
    font-weight: 400;
  }

  h1 {
    font-size: 48px;
  }
}
</style>
