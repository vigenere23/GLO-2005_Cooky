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
import { API } from '@/js/api/api'

export default {

  name: 'Recipes',

  components: {
    SearchBar,
    GridList
  },

  data () {
    return {
      recipes: null,
      defaultDesc: 'Lorem ipsum ipridus karem de la satuple como quiero salades par itadus. Lorem ipsum ipridus karem de la satuple como quiero salades par itadus.'
    }
  },

  created () {
    this.fetchData()
  },

  watch: {
    '$route': 'fetchData'
  },

  methods: {
    async fetchData () {
      this.recipes = null
      this.recipes = await API.getRecipes()
      this.recipes.forEach(recipe => { recipe.description = recipe.description || this.defaultDesc })
    }
  }

}
</script>
