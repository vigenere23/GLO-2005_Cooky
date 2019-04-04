<template>
  <div class="small-card-wrapper">
    <router-link
      class="small-card"
      :class="{ 'add-margins': addMargins }"
      tag="a"
      :to="link || ''"
    >
      <div
        class="small-card_image"
        :style="background"
      />
      <div class="small-card_content">
        <p class="small-card_title hide-text">
          {{ title }}
        </p>
        <p class="small-card_description hide-text">
          {{ description }}
        </p>
      </div>
    </router-link>
  </div>
</template>

<script>
import { FormatHelper } from '@/js/helpers/format'

export default {

  name: 'SmallCard',

  props: {
    title: {
      type: String,
      default: ''
    },
    image: {
      type: String,
      default: ''
    },
    description: {
      type: String,
      default: ''
    },
    addMargins: {
      type: Boolean,
      default: false
    },
    link: {
      type: String,
      default: ''
    }
  },

  computed: {
    defaultImage () {
      return '../../../static/default-recipe-image.png'
    },
    background () {
      return FormatHelper.backgroundImageStyle(this.image || this.defaultImage)
    }
  }

}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.small-card {
  display: flex;
  border-radius: 4px;
  overflow: hidden;
  @include mdElevationElement('card');

  &.add-margins {
    margin-bottom: 16px;
  }

  .small-card_image {
    flex-shrink: 0;
    height: 100px;
    width: 100px;
    @include background();
  }

  .small-card_content {
    padding: 12px;
    flex-grow: 1;
    overflow: hidden;

    p {
      margin: 0;
    }

    .small-card_title {
      font-size: 16px;
      font-weight: 500;
      margin-bottom: 12px;
      max-height: 1.4em;
      white-space: nowrap;
    }

    .small-card_description {
      color: $secondary-text-color;
      font-size: 14.5px;
      max-height: calc(2 * 1.4em);
    }
  }
}
</style>
