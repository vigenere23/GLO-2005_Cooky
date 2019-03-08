<template>
  <div id="default-layout">
    <Header />
    <Sidenav />
    <slot />
  </div>
</template>

<script>
import Header from '@/components/Header'
import Sidenav from '@/components/Sidenav'

export default {
  name: 'DefaultLayout',
  components: {
    Header,
    Sidenav
  }
}
</script>

<style lang="scss">
#default-layout {
  width: 100%;
  min-height: 100vh;
}
</style>
