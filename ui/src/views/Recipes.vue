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
      recipes: null
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
    }
  }

}
</script>
