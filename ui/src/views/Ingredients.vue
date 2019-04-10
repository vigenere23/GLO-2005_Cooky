<template>
  <div class="ingredients-page">
    <h1>Find ingredients</h1>
    <SearchBar @send="search" />
    <IngredientsDataTable
      v-if="ingredients"
      :columns="columns"
      :items="ingredients"
    />
  </div>
</template>

<script>
import SearchBar from '@/components/inputs/SearchBar'
import IngredientsDataTable from '@/components/wrappers/IngredientsDataTable'
import { API } from '@/js/api/api'

export default {

  name: 'Ingredients',

  components: {
    SearchBar,
    IngredientsDataTable
  },

  data () {
    return {
      searching: false,
      columns: [
        { name: 'name', text: 'Name', sortable: true, initiallySorted: true },
        { name: 'quantity', text: 'Quantity' },
        { name: 'price', text: 'Price ($)', sortable: true }
      ],
      ingredients: null
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
      this.ingredients = null
      this.ingredients = await API.getIngredients()
    },
    async search (name) {
      if (!this.searching) {
        this.searching = true
        this.ingredients = null
        this.ingredients = await API.getIngredientsByName(name)
        this.searching = false
      }
    }
  }

}
</script>
