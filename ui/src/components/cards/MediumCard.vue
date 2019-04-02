<template>
  <a class="medium-card">
    <div class="medium-card_image"
      :style="background"></div>
    <div class="medium-card_content">
      <p class="medium-card_title">{{ title }}</p>
      <p class="medium-card_creator"></p>
      <p class="medium-card_description">{{ description }}</p>
      <div class="medium-card_tags"></div>
      <div class="medium-card_actions"></div>
    </div>
  </a>
</template>

<script>
import { FormatHelper } from '@/js/helpers/format'

export default {

  name: 'MediumCard',

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
    }
  },

  computed: {
    defaultImage() {
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

.medium-card {
  display: block;
  width: 320px;
  border-radius: 4px;
  @include mdElevationElement('card');

  .medium-card_image {
    width: 100%;
    padding-bottom: calc(100% / 16 * 9);
    @include background();
  }

  .medium-card_content {
    padding: 16px;

    p {
      margin: 0;
    }

    .medium-card_title {
      font-size: 20px;
      font-weight: 500;
      margin-bottom: 20px;
    }

    .medium-card_description {
      color: $secondary-text-color;
      font-size: 14.5px;
      line-height: 1.4em;
      max-height: calc(2 * 1.4em);
      position: relative;
      overflow: hidden;

      &:after {
        content: '';
        display: block;
        position:absolute;
        bottom: 0;
        right: 0;
        width: 4em;
        height: 1.4em;
        background: linear-gradient(to right, transparent, white 80%);
      }
    }
  }
}
</style>
