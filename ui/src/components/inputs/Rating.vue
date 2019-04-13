<template>
  <div class="rating">
    <div
      class="star"
      v-for="i in 5"
      :key="i"
      @mouseover="updateHoveredRating(i)"
      @mouseleave="updateHoveredRating(0)"
      @click="emitRating(i)"
    >
      <span class="material-icons">
        <template v-if="isFilled(i)">
          star
        </template>
        <template v-else>
          star_border
        </template>
      </span>
    </div>
  </div>
</template>

<script>
export default {

  name: 'Rating',

  props: {
    rating: {
      type: Number,
      required: true
    }
  },

  data () {
    return {
      hovered: false,
      hoveredRating: 0
    }
  },

  methods: {
    isFilled (i) {
      return this.hovered
        ? i <= this.hoveredRating
        : i <= this.rating
    },
    updateHoveredRating (i) {
      if (i > 0) {
        this.hovered = true
        this.hoveredRating = i
      } else {
        this.hovered = false
      }
    },
    emitRating (i) {
      this.$emit('rated', i)
    }
  }

}
</script>

<style lang="scss">
.rating {
  display: flex;
  align-items: center;

  .star {
    flex-shrink: 0;
    color: #FFC107;
    cursor: pointer;
  }
}
</style>
