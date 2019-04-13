<template>
  <div class="comment-adder">
    <LabelInput
      v-model="comment"
      @keypress.native.enter="submit"
    />
    <Button
      accent
      no-margin
      @click="submit"
    />
  </div>
</template>

<script>
import LabelInput from '@/components/inputs/LabelInput'
import Button from '@/components/buttons/Button'

export default {

  name: 'CommentAdder',

  components: {
    LabelInput,
    Button
  },

  data () {
    return {
      comment: ''
    }
  },

  methods: {
    submit () {
      if (this.comment) {
        this.$emit('submit', this.comment)
        this.comment = ''
      }
    }
  }

}
</script>

<style lang="scss">
.comment-adder {
  display: flex;
  align-items: center;
  padding: 0 8px;
}
</style>
