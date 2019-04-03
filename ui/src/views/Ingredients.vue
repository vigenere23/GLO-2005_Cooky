<template>
  <div class="ingredients-page">
    <h1>Find ingredients</h1>
    <SearchBar />
    <DataTable
      :columns="columns"
      :items="items"
    />
  </div>
</template>

<script>
import SearchBar from '@/components/SearchBar'
import DataTable from '@/components/lists/DataTable'

export default {

  name: 'Ingredients',

  components: {
    SearchBar,
    DataTable
  },

  data () {
    return {
      columns: [
        { for: null, text: '' },
        { for: 'name', text: 'Name' },
        { for: 'quantity', text: 'Quantity' },
        { for: 'price', text: 'Price ($)' }
      ],
      items: [
        {
          name: 'Orange',
          quantity: '1 unit',
          price: '3.45'
        },
        {
          name: 'Natural whipped cream',
          quantity: '355 mL',
          price: '6.99'
        },
        {
          name: 'Honey Bunches of Oats',
          quantity: '411 g',
          price: '4.99'
        },
        {
          name: 'Jasmine rice',
          quantity: '5 kg',
          price: '18.62'
        }
      ]
    }
  }

}
</script>
