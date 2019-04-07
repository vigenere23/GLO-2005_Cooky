<template>
  <div class="grid-list">
    <template v-if="small || isPhone">
      <SmallCard
        v-for="(item, i) in items"
        :key="item.id || i"
        :title="item.name"
        :description="item.description"
        :image="item.image"
        :link="`${baselink}/${item.id}`"
      />
    </template>
    <template v-else>
      <MediumCard
        v-for="(item, i) in items"
        :key="item.id || i"
        :title="item.name"
        :description="item.description"
        :image="item.image"
        :link="`${baselink}/${item.id}`"
      />
    </template>
  </div>
</template>

<script>
import SmallCard from '@/components/cards/SmallCard'
import MediumCard from '@/components/cards/MediumCard'
import { mapGetters } from 'vuex'

export default {

  name: 'GridList',

  components: {
    SmallCard,
    MediumCard
  },

  props: {
    items: {
      type: Array,
      required: true
    },
    small: {
      type: Boolean,
      default: false
    },
    baselink: {
      type: String,
      default: ''
    }
  },

  computed: mapGetters('layout', ['isPhone'])

}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.grid-list {
  display: grid;
  grid-gap: 16px;
  justify-content: center;
  justify-items: center;
  margin: 16px auto;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));

  > * {
    grid-column: span 1;
    min-width: 100%;
  }
}
</style>
