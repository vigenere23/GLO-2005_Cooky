<template>
  <div class="ingredients-page">
    <h1>Find ingredients</h1>
    <SearchBar />
    <IngredientsDataTable
      :columns="columns"
      :items="ingredients"
    />
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar'
import IngredientsDataTable from '@/components/wrappers/IngredientsDataTable'
import { ingredients } from '@/js/data/ingredients'

export default {

  name: 'Ingredients',

  components: {
    SearchBar,
    IngredientsDataTable
  },

  data () {
    return {
      columns: [
        { name: 'name', text: 'Name', sortable: true, initiallySorted: true },
        { name: 'quantity', text: 'Quantity' },
        { name: 'price', text: 'Price ($)', sortable: true }
      ],
      ingredients: ingredients
    }
  }

}
</script>
