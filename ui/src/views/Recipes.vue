<template>
  <div class="recipes-page">
    <h1>Explore recipes</h1>
    <SearchBar />
    <GridList
      :items="recipes"
      baselink="/recipes"
    />
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar'
import GridList from '@/components/lists/GridList'
import { recipes } from '@/js/data/recipes'

export default {

  name: 'Recipes',

  components: {
    SearchBar,
    GridList
  },

  data () {
    return {
      recipes: recipes
    }
  }

}
</script>
