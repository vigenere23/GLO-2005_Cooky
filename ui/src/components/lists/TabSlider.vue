<template>
  <div class="tab-slider">
    <div class="tabs">
      <div
        v-for="(tab, i) in tabs"
        :key="i"
        class="tab"
        :class="{ current: currentTab === i }"
        @mousedown="switchTab(i)"
      >
        {{ tab }}
      </div>
    </div>
    <div
      class="tab-slider_content-wrapper"
      :style="translateStyle"
    >
      <div
        class="tab-slider_content"
        v-for="(tab, i) in tabs"
        :key="i"
      >
        <slot :name="tab" />
      </div>
    </div>
  </div>
</template>

<script>
export default {

  name: 'Tabs',

  props: {
    tabs: {
      type: Array,
      required: true
    }
  },

  data () {
    return {
      currentTab: 0
    }
  },

  computed: {
    translateStyle () {
      return `transform: translateX(calc(-100% * ${this.currentTab}));`
    }
  },

  methods: {
    switchTab (n) {
      this.currentTab = n
    }
  }

}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.tab-slider {
  background-color: white;
  overflow-x: hidden;
  border: $faded-border;
  @include mdElevation(2);

  .tabs {
    display: flex;
    justify-content: center;
    cursor: pointer;

    .tab {
      display: block;
      flex-basis: 200px;
      padding: 16px 0;
      font-size: 16px;
      text-transform: capitalize;
      text-align: center;
      transition: background-color 0.2s ease-in-out,
                  color 0.2s ease-in-out;

      &.current {
        border-bottom: solid 3px $primary-color;
        color: $primary-color;
        font-weight: 500;
      }

      &:hover {
        @include primary-color-background(0.1);
      }

      &:active {
        @include primary-color-background(0.2);
      }
    }
  }

  .tab-slider_content-wrapper {
    display: flex;
    will-change: transform;
    transition: all 0.3s ease-in-out;

    .tab-slider_content {
      width: 100%;
      padding: 16px;
      flex-shrink: 0;
    }
  }
}
</style>
