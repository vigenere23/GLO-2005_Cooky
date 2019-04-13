<template>
  <div class="like">
    <span
      class="material-icons"
      @click="handleLike"
    >
      <template v-if="liked">
        favorite
      </template>
      <template v-else>
        favorite_border
      </template>
    </span>
  </div>
</template>

<script>
export default {

  name: 'Like',

  props: {
    liked: {
      type: Boolean,
      required: true
    }
  },

  methods: {
    handleLike () {
      this.liked
        ? this.$emit('unliked')
        : this.$emit('liked')
    }
  }

}
</script>

<style lang="scss">
.like {
  color: #E91E63;
}
</style>
