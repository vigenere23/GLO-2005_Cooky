<template>
  <div class="comments">
    <CommentItem
      v-for="(comment, i) in comments"
      :key="comment.id || i"
      :comment="comment"
      :is-reply="comment.user.id === ownerId"
    />
  </div>
</template>

<script>
import CommentItem from '@/components/comments/CommentItem'

export default {

  name: 'Comments',

  components: {
    CommentItem
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
