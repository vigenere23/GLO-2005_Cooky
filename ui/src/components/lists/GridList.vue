<template>
  <div class="grid-list">
    <template v-if="isPhone">
      <SmallCard
        v-for="(item, i) in items"
        :key="item.id || i"
        :title="item.title"
        :description="item.description"
        :image="item.image"
        add-margins="true"
      />
    </template>
    <template v-else>
      <MediumCard
        v-for="(item, i) in items"
        :key="item.id || i"
        :title="item.title"
        :description="item.description"
        :image="item.image"
      />
    </template>
  </div>
</template>

<script>
import SmallCard from '@/components/cards/SmallCard'
import MediumCard from '@/components/cards/MediumCard'

export default {

  name: 'GridList',

  components: {
    SmallCard,
    MediumCard
  },

  props: {
    items: {
      type: Array,
      default: () => []
    },
    small: {
      type: Boolean,
      default: false
    }
  },

  computed: {
    isPhone () {
      return this.$store.getters.isPhone
    }
  }

}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.grid-list {
  display: grid;
  grid-gap: 16px;
  justify-content: center;
  justify-items: center;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));

  > * {
    grid-column: span 1;
  }
}

@media screen and (max-width: $phone-max) {
  .grid-list {
    display: block;
  }
}
</style>
