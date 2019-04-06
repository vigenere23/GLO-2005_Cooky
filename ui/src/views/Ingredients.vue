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
import { mapGetters, mapMutations } from 'vuex'

export default {

  name: 'Ingredients',

  components: {
    SearchBar,
    DataTable
  },

  computed: mapGetters('user', ['cartContains']),

  data () {
    return {
      columns: [
        { name: 'name', text: 'Name', sortable: true, initiallySorted: true },
        { name: 'quantity', text: 'Quantity' },
        { name: 'price', text: 'Price ($)', sortable: true }
      ],
      ingredients: ingredients,
      actions: {
        isSelected: (item) => this.cartContains(item.id),
        onSelection: (item) => this.addCartItem(item.id),
        onDeselection: (item) => this.removeCartItem(item.id)
      }
    }
  },

  methods: mapMutations('user', ['addCartItem', 'removeCartItem'])

}
</script>
