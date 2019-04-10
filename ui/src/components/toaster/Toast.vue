<template>
  <div
    class="toast"
    :class="[type, { show }]"
  >
    <span class="message">
      {{ message }}
    </span>
  </div>
</template>

<script>
export default {
  name: 'Toast',
  props: {
    type: {
      type: String,
      required: true
    },
    message: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      show: false
    }
  },
  created () {
    setTimeout(() => { this.show = true }, 100)
    setTimeout(() => { this.show = false }, 3700)
    setTimeout(() => this.$emit('delete'), 4000)
  }
}
</script>

<style lang="scss">
.toast {
  width: 100%;
  padding: 16px;
  color: white;
  font-weight: 500;
  position: relative;
  border-radius: 4px;
  margin-top: 8px;
  opacity: 0;
  top: -100%;
  transition: all 0.2s ease-in-out;

  &.show {
    opacity: 1;
    top: 0;
    transition: all 0.2s ease-in-out;
  }

  &.success {
    background-color: #2bc226;
  }

  &.warning {
    background-color: #eac017;
  }

  &.error {
    background-color: #d32c2c;
  }
}
</style>
