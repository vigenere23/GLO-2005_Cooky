<template>
  <div class="search-bar">
    <input
      type="text"
      @input="emit('inout')"
    >
    <div class="search-icon">
      <i class="material-icons search-icon">search</i>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SearchBar'
}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.search-bar {
  position: relative;
  margin: 48px auto;
  width: 100%;
  max-width: 460px;

  input {
    display: block;
    width: 100%;
    font-size: 18px;
    line-height: 1.2em;
    padding: 16px;
    padding-right: 48px;
    border-radius: 4px;
    border: $faded-border;
    @include mdElevationElement('search-bar');
  }

  .search-icon {
    position: absolute;
    right: 0;
    top: 0;
    bottom: 0;
    height: calc(100% - 2px);
    margin: 1px 0;
    padding: 0 12px;
    border-radius: 4px;
    display: flex;
    align-items: center;
    background-color: white;
  }
}
</style>
