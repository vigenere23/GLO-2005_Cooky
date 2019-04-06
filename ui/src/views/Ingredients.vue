<template>
  <div class="ingredients-page">
    <h1>Find ingredients</h1>
    <SearchBar />
    <DataTable
      :columns="columns"
      :items="ingredients"
      :actions="actions"
    />
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar'
import DataTable from '@/components/lists/DataTable'
import { ingredients } from '@/js/data/ingredients'

export default {

  name: 'Ingredients',

  components: {
    SearchBar,
    DataTable
  },

  data () {
    return {
      columns: [
        { name: 'name', text: 'Name', sortable: true, defaultSortingAscending: true },
        { name: 'quantity', text: 'Quantity' },
        { name: 'price', text: 'Price ($)', sortable: true }
      ],
      ingredients: ingredients,
      actions: {
        initiallySelected (item) {
          return item.name === 'Orange'
        },
        selected: {
          icon: 'add_circle_outline',
          action (item) {
            return true
          }
        },
        deselected: {
          icon: 'add_circle',
          action (item) {
            return true
          }
        }
      }
    }
  }

}
</script>
