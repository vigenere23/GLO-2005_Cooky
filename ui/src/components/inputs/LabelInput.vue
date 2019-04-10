<template>
  <div
    class="label-input"
    :class="{ focused, error }"
  >
    <input
      @focus="focus"
      @blur="blur"
      @input="input"
      :type="type"
      :placeholder="placeholder"
      :name="label"
      :value="value"
    >
    <span class="label">
      {{ label }}
    </span>
  </div>
</template>

<script>
export default {
  name: 'LabelInput',
  props: {
    type: {
      type: String,
      default: 'text'
    },
    label: {
      type: String,
      default: ''
    },
    value: {
      type: String,
      default: ''
    },
    placeholder: {
      type: String,
      default: ''
    }
  },
  data () {
    return {
      focused: false,
      error: false
    }
  },
  methods: {
    focus () { this.focused = true },
    blur () {
      this.focused = false
      this.error = !this.value
    },
    input (e) { this.$emit('input', e.target.value) }
  }
}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.label-input {
  margin: 16px 0;
  width: 100%;

  input {
    display: block;
    width: 100%;
    font-size: 18px;
    line-height: 1.2em;
    padding: 8px 12px;
    padding-right: 48px;
    border-radius: 4px;
    border: $faded-border;
    border-width: 2px;
  }

  .label {
    display: block;
  }

  &.focused {
    input {
      border-color: #1e88e5;
    }

    .label {
      color: #1e88e5;
    }
  }

  &:not(.focused).error {
    input {
      border-color: #d32c2c;
    }

    .label {
      color: #d32c2c;
    }
  }
}
</style>
