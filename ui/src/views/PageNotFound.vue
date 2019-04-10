<template>
  <div class="not-found-page">
    <h1>404</h1>
    <h2>This page was not found <span class="emoji">😢</span></h2>
    <p>
      Maybe you should take a look at the
      <router-link
        tag="a"
        to="/recipes"
      >
        recipes
      </router-link>!
    </p>
  </div>
</template>

<script>
export default {
  name: 'PageNotFound'
}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.not-found-page {
  h2, p {
    text-align: center;
  }

  a {
    color: $primary-color;
    font-weight: 500;
  }
}
</style>
