<template>
  <div
    class="recipe-page"
    v-if="recipe"
  >
    <h1>{{ recipe.name }}</h1>
    <div class="recipe_intro">
      <img src="https://img1.cookinglight.timeinc.net/sites/default/files/styles/medium_2x/public/image/2017/04/main/dragon-fruit-smoothie-bowl-1704w.jpg">
      <p class="recipe_description">
        {{ recipe.description }}
      </p>
      <p class="user">
        by
        <router-link
          tag="a"
          :to="`/users/${userId}`"
        >
          {{ recipe.user.username }}
        </router-link>
      </p>
    </div>
    <div class="recipe_content">
      <div v-if="ingredients">
        <h2>Ingredients</h2>
        <IngredientsDataTable
          :columns="columns"
          :items="ingredients"
          :small="true"
        />
      </div>
      <div>
        <h2>Steps</h2>
        <p>{{ recipe.directives }}</p>
      </div>
    </div>
    <div v-if="comments">
      <h2>Comments</h2>
      <CommentList
        :comments="comments"
        :owner-id="userId"
      />
    </div>
  </div>
</template>

<script>
import IngredientsDataTable from '@/components/wrappers/IngredientsDataTable'
import CommentList from '@/components/comments/CommentList'
import { comments } from '@/js/data/comments'
import { mapState } from 'vuex'
import { API } from '@/js/api/api'

export default {

  name: 'Recipe',

  components: {
    IngredientsDataTable,
    CommentList
  },

  computed: mapState('user', ['userId']),

  data () {
    return {
      id: null,
      recipe: null,
      ingredients: null,
      columns: [
        { name: 'name', text: 'Name', sortable: true, initiallySorted: true },
        { name: 'quantity', text: 'Quantity' }
      ],
      comments: comments
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
      this.id = this.recipe = this.ingredients = null
      this.id = this.$route.params.id
      this.recipe = await API.getRecipeById(this.id)
      this.ingredients = await API.getIngredientFromIdRecipe(this.id)
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
