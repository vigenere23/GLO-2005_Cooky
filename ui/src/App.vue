<template>
  <div id="app">
    <DefaultLayout>
      <transition
        name="fade"
        mode="out-in"
      >
        <router-view />
      </transition>
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

  p {
    line-height: 1.4em;
  }

  button {
    border: none;
    background: none;
  }

  h1 {
    font-family: "Noto Serif", Helvetica, Arial, sans-serif;
    font-weight: 400;
    font-size: 48px;
    margin: 1em 0;
    text-align: center;
  }

  h2 {
    margin-bottom: 0.5em;
    margin-top: 1em;
    font-weight: 500;
  }

  .hide-text {
    position: relative;
    overflow: hidden;

    &:after {
      content: '';
      display: block;
      position: absolute;
      bottom: 0;
      right: 0;
      width: 2em;
      height: 1.4em;
      background: linear-gradient(to right, transparent, white 80%);
    }
  }

  .emoji {
    font-family: Arial;
  }

  .fade-enter-active,
  .fade-leave-active {
    transition: opacity .2s
  }

  .fade-enter,
  .fade-leave-to {
    opacity: 0
  }
}

@media screen and (max-width: $phone-max) {
  body {
    h1 {
      font-size: 32px;
    }
  }
}
</style>
