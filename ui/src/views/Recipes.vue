<template>
  <div class="recipes-page">
    <h1>Explore recipes</h1>
    <GridList
      :items="recipes"
    ></GridList>
  </div>
</template>

<script>
import GridList from '@/components/lists/GridList'

export default {

  name: 'Recipes',

  components: {
    GridList
  },

  data () {
    return {
      recipes: [
        {
          title: 'Fruity smoothie bowl',
          description: 'Wake up energic and be ready for the day. This smoothie will get you everything you need to be productive, bright and perseverant during the entire day.',
          image: 'https://img1.cookinglight.timeinc.net/sites/default/files/styles/medium_2x/public/image/2017/04/main/dragon-fruit-smoothie-bowl-1704w.jpg'
        }
      ]
    }
  }

}
</script>

<style lang="scss">
.recipes-page {
  h1 {
    text-align: center;
  }
}
</style>
