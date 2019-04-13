<template>
  <div class="comments">
    <template v-if="comments.length">
      <CommentItem
        v-for="(comment, i) in comments"
        :key="comment.id || i"
        :comment="comment"
        :is-reply="comment.user.id === ownerId"
      />
    </template>
    <template v-else>
      <NoContent />
    </template>
    <CommentAdder @submit="submit" />
  </div>
</template>

<script>
import CommentItem from '@/components/comments/CommentItem'
import CommentAdder from '@/components/comments/CommentAdder'
import NoContent from '@/components/NoContent'

export default {

  name: 'Comments',

  components: {
    CommentItem,
    CommentAdder,
    NoContent
  },

  props: {
    comments: {
      type: Array,
      required: true
    },
    ownerId: {
      type: String,
      default: null
    }
  },

  methods: {
    submit (comment) {
      this.$emit('submit', comment)
    }
  }

}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.comments {
  width: 100%;
  display: flex;
  flex-direction: column;
  background-color: white;
  border-radius: 4px;
  border: $faded-border;
  @include mdElevation(2);
}
</style>
