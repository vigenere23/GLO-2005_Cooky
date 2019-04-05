<template>
  <div class="user-page">
    <h1>{{ username }}</h1>
    <TabSlider :tabs="tabs">
      <template #recipes>
        <GridList
          :items="recipes"
          baselink="/recipes"
        />
      </template>
      <template #likes>
        <GridList
          :items="recipes"
          baselink="/recipes"
        />
      </template>
    </TabSlider>
  </div>
</template>

<script>
import TabSlider from '@/components/lists/TabSlider'
import GridList from '@/components/lists/GridList'
import { recipes } from '@/data/recipes'

export default {

  name: 'User',

  components: {
    TabSlider,
    GridList
  },

  data () {
    return {
      username: 'mscupcake352',
      tabs: [
        'recipes',
        'likes'
      ],
      recipes: recipes
    }
  }

}
</script>
