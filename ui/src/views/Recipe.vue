<template>
  <div
    class="recipe-page"
    v-if="recipe"
  >
    <FloatingButton
      v-if="recipe"
      icon="edit"
      :link="`/recipes/${$route.params.id}/edit`"
    />
    <h1>{{ recipe.name }}</h1>
    <div class="actions">
      <div class="like">
        <span
          class="material-icons"
          v-if="liked"
          @click="unlike"
        >
          favorite
        </span>
        <span
          class="material-icons"
          v-else
          @click="like"
        >
          favorite_outline
        </span>
      </div>
      <Rating :initial-rating="3" />
    </div>
    <div class="recipe_intro">
      <img src="https://img1.cookinglight.timeinc.net/sites/default/files/styles/medium_2x/public/image/2017/04/main/dragon-fruit-smoothie-bowl-1704w.jpg">
      <p class="recipe_description">
        {{ recipe.description }}
      </p>
      <p class="user">
        by
        <router-link
          tag="a"
          :to="`/users/${recipe.user.id}`"
        >
          {{ recipe.user.username }}
        </router-link>
      </p>
    </div>
    <div class="recipe_content">
      <div v-if="ingredients">
        <h2>Ingredients</h2>
        <DataTable
          id="id_Ingredient"
          :columns="columns"
          :items="ingredients"
          :small="true"
          :actions="actions"
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
import FloatingButton from '@/components/buttons/FloatingButton'
import DataTable from '@/components/lists/DataTable'
import CommentList from '@/components/comments/CommentList'
import Rating from '@/components/inputs/Rating'
import { comments } from '@/js/data/comments'
import { mapState, mapGetters, mapActions } from 'vuex'
import { API } from '@/js/api/api'

export default {

  name: 'Recipe',

  components: {
    FloatingButton,
    DataTable,
    CommentList,
    Rating
  },

  computed: {
    ...mapState('user', ['userId']),
    ...mapGetters('user', ['cartContains'])
  },

  data () {
    return {
      id: null,
      recipe: null,
      ingredients: null,
      columns: [
        { name: 'name', text: 'Name', sortable: true, initiallySorted: true },
        { name: 'quantity', text: 'Quantity' }
      ],
      comments: comments,
      liked: false,
      actions: {
        isSelected: (recipeIngredient) => {
          return this.cartContains(recipeIngredient.id_Ingredient)
        },
        onSelection: (recipeIngredient) => {
          return this.addCartItem(recipeIngredient.id_Ingredient)
        },
        onDeselection: (recipeIngredient) => {
          return this.removeCartItem(recipeIngredient.id_Ingredient)
        }
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
    async fetchData () {
      this.id = this.recipe = this.ingredients = null
      this.id = this.$route.params.id
      await this.fetchRecipe()
      await this.fetchIngredients()
      await this.fetchLikes()
    },
    async fetchLikes () {
      const likes = await API.getUserLikes(this.userId)
      if (likes.find(recipe => recipe.id === this.id)) {
        this.liked = true
      }
    },
    async fetchRecipe () {
      this.recipe = await API.getRecipeById(this.id)
    },
    async fetchIngredients () {
      this.ingredients = await API.getIngredientFromIdRecipe(this.id)
    },
    async like () {
      await API.addLike(this.id, this.userId)
      this.fetchLikes()
    },
    async unlike () {
      await API.removeLike(this.id, this.userId)
      this.fetchLikes()
    },
    ...mapActions('user', ['addCartItem', 'removeCartItem'])
  }

}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.recipe-page {

  .actions {
    display: flex;
    align-items: center;

    > * {
      margin: 0 8px;
      flex-shrink: 0;
    }

    .like {
      cursor: pointer;
    }
  }

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
