<template>
  <div class="recipes-page">
    <h1>Explore recipes</h1>
    <FloatingButton link="/recipes/create" />
    <SearchBar
      @input="search"
      @send="search"
    />
    <GridList
      v-if="recipes"
      :items="recipes"
      baselink="/recipes"
    />
  </div>
</template>

<script>
import FloatingButton from '@/components/buttons/FloatingButton'
import SearchBar from '@/components/inputs/SearchBar'
import GridList from '@/components/lists/GridList'
import { API } from '@/js/api/api'

export default {

  name: 'Recipes',

  components: {
    FloatingButton,
    SearchBar,
    GridList
  },

  data () {
    return {
      recipes: null,
      searching: false
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
    },
    async search (search) {
      clearTimeout(this.searchTimeout)
      this.searchTimeout = setTimeout(async () => {
        this.recipes = await API.getRecipesByName(search)
      }, 300)
    }
  }

}
</script>
