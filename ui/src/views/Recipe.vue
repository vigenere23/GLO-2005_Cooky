<template>
  <div class="recipe-page">
    <h1>{{ title }}</h1>
    <div class="recipe_intro">
      <img src="https://img1.cookinglight.timeinc.net/sites/default/files/styles/medium_2x/public/image/2017/04/main/dragon-fruit-smoothie-bowl-1704w.jpg">
      <p class="recipe_description">
        {{ description }}
      </p>
      <p class="user">
        by
        <router-link
          tag="a"
          :to="`/users/${user.id}`"
        >
          {{ user.username }}
        </router-link>
      </p>
    </div>
    <div class="recipe_content">
      <div>
        <h2>Ingredients</h2>
        <DataTable
          :columns="columns"
          :items="ingredients"
          :small="true"
          action-icon="add_circle"
        />
      </div>
      <div>
        <h2>Steps</h2>
        <p>{{ steps }}</p>
      </div>
    </div>
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
      user: {
        username: 'mscupcake352',
        id: this.$store.state.userId
      },
      description: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
      steps: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor. Incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
      columns: [
        { name: 'name', text: 'Name' },
        { name: 'quantity', text: 'Quantity' }
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

  .recipe_intro {
    width: 100%;
    max-width: 700px;
    margin: auto;

    img {
      width: 100%;
      display: block;
      border-radius: 4px;
      @include mdElevation(2);
    }

    .recipe_description {
      color: $secondary-text-color;
    }

    .user {
      font-size: 16px;

      a {
        color: $primary-color;
        font-weight: 500;
      }
    }
  }

  .recipe_content {
    display: grid;
    margin: auto;
    justify-content: space-around;
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 32px;

    > * {
      grid-column: span 1;
    }
  }
}

@media screen and (max-width: $phone-max) {
  .recipe-page {
    .recipe_content {
      > * {
        grid-column: span 2;
      }
    }
  }
}
</style>
