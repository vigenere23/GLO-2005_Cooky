<template>
  <div class="recipe-page">
    <h1>{{ title }}</h1>
    <img src="https://img1.cookinglight.timeinc.net/sites/default/files/styles/medium_2x/public/image/2017/04/main/dragon-fruit-smoothie-bowl-1704w.jpg">
    <p class="recipe_description">
      {{ description }}
    </p>
    <h2>Ingredients</h2>
    <DataTable
      :columns="columns"
      :items="ingredients"
      :small="true"
      action-icon="add_circle"
    />
    <h2>Steps</h2>
    <p>{{ steps }}</p>
  </div>
</template>

<script>
import DataTable from '@/components/lists/DataTable'

export default {

  name: 'Recipe',

  components: {
    DataTable
  },

  data () {
    return {
      title: 'Fruity smoothie bowl',
      description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
      steps: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor. Incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
      columns: [
        { for: 'name', text: 'Name' },
        { for: 'quantity', text: 'Quantity' }
      ],
      ingredients: [
        {
          name: 'Orange',
          quantity: '3/4 unit'
        },
        {
          name: 'Natural whipped cream',
          quantity: '10 mL'
        },
        {
          name: 'Honey Bunches of Oats',
          quantity: '1 cup'
        },
        {
          name: 'Jasmine rice',
          quantity: '2 cups'
        },
        {
          name: 'Water',
          quantity: '3 1/2 cups'
        }
      ]
    }
  }

}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.recipe-page {
  img {
    width: 100%;
    border-radius: 4px;
    @include mdElevation(2);
  }

  .recipe_description {
    color: $secondary-text-color;
  }
}
</style>
