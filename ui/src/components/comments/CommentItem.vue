<template>
  <div
    class="comment-item"
    :class="{ reply: isReply }"
  >
    <div class="comment-item_user">
      <img :src="avatar(comment.user)">
      <router-link
        :to="`/users/${comment.user.id}`"
        tag="a"
      >
        {{ comment.user.username }}
      </router-link>
    </div>
    <span class="comment-item_text">
      {{ comment.text }}
    </span>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {

  name: 'CommentItem',

  props: {
    comment: {
      type: Object,
      required: true
    },
    isReply: {
      type: Boolean,
      default: false
    }
  },

  computed: mapGetters('user', ['avatar'])

}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.comment-item {
  width: 100%;
  padding: 16px;

  &:not(:last-child) {
    border-bottom: $faded-border;
  }

  .comment-item_user {
    display: flex;
    align-items: center;
    margin-bottom: 16px;

    img {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      flex-shrink: 0;
    }

    a {
      padding-left: 16px;
      font-size: 13.5px;
      font-weight: 500;
    }
  }

  .comment-item_text {
    line-height: 1.4em;
  }

  &.reply {
    padding-left: 32px;

    .comment-item_user a {
      color: $primary-color;
    }
  }
}

@media screen and (max-width: $phone-max) {
  .comment-item {
    padding: 12px;
  }
}
</style>
