<template>
  <div class="grid-list">

    <div v-if="small">
      <SmallCard
        v-for="(i, item) in items"
        :key="item.id || i"
        :item="item"
      ></SmallCard>
    </div>

    <div v-else>
      <MediumCard
        v-for="(item, i) in items"
        :key="item.id || i"
        :title="item.title"
        :description="item.description"
        :image="item.image"
      ></MediumCard>
    </div>
  </div>
</template>

<script>
import MediumCard from '@/components/cards/MediumCard'
import SmallCard from '@/components/cards/SmallCard'

export default {

  name: 'GridList',

  components: {
    MediumCard,
    SmallCard
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
  }

}
</script>
