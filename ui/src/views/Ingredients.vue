<template>
  <div class="ingredients-page">
    <h1>Find ingredients</h1>
    <SearchBar
      @input="search"
      @send="search"
    />
    <DataTable
      v-if="ingredients"
      :columns="columns"
      :items="ingredients"
      :actions="actions"
    />
  </div>
</template>

<script>
import SearchBar from '@/components/inputs/SearchBar'
import DataTable from '@/components/lists/DataTable'
import { API } from '@/js/api/api'
import { mapState, mapGetters, mapActions } from 'vuex'

export default {

  name: 'Ingredients',

  components: {
    SearchBar,
    DataTable
  },

  computed: {
    ...mapGetters('user', ['cartContains']),
    ...mapState('user', ['userId'])
  },

  data () {
    return {
      searching: false,
      searchTimeout: null,
      columns: [
        { name: 'name', text: 'Name', sortable: true, initiallySorted: true },
        { name: 'quantity', text: 'Quantity' },
        { name: 'price', text: 'Price ($)', sortable: true }
      ],
      ingredients: null,
      actions: {
        isSelected: (ingredient) => this.cartContains(ingredient.id),
        onSelection: (ingredient) => this.addCartItem(ingredient.id),
        onDeselection: (ingredient) => this.removeCartItem(ingredient.id)
      }
    }
  },

  created () {
    this.fetchData()
  },

  watch: {
    '$route': 'fetchData'
  },

  methods: {
    fetchData () {
      let timeout = null
      setTimeout(async () => {
        if (!this.userId) {
          clearTimeout(timeout)
          timeout = setTimeout(this.fetchData, 800)
        } else {
          this.ingredients = null
          this.ingredients = await API.getIngredients()
        }
      }, 200)
    },
    async search (search) {
      clearTimeout(this.searchTimeout)
      this.searchTimeout = setTimeout(async () => {
        this.ingredients = await API.getIngredientsByName(search)
      }, 300)
    },
    ...mapActions('user', ['addCartItem', 'removeCartItem'])
  }

}
</script>
