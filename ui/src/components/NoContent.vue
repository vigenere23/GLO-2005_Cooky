<template>
  <div class="no-content">
    <slot>
      <span>No content</span>
    </slot>
  </div>
</template>

<script>
export default {
  name: 'NoContent'
}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.no-content {
  width: 100%;
  padding: 48px;
  text-align: center;
  font-size: 20px;
  font-weight: 500;
  color: $secondary-text-color;
}
</style>
