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
    <div class="actions">
      <Like
        :liked="liked"
        @liked="like"
        @unliked="unlike"
      />
      <Rating
        :rating="rating"
        @rated="rate"
      />
      <span v-if="recipe">
        Rated {{ recipe.rating }} stars
      </span>
    </div>
    <div class="recipe_content">
      <div>
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
import Like from '@/components/inputs/Like'
import { comments } from '@/js/data/comments'
import { mapState, mapGetters, mapActions } from 'vuex'
import { API } from '@/js/api/api'

export default {

  name: 'Recipe',

  components: {
    FloatingButton,
    DataTable,
    CommentList,
    Rating,
    Like
  },

  computed: {
    ...mapState('user', ['userId']),
    ...mapGetters('user', ['cartContains']),
    liked () {
      return !!this.userLikes.find(recipe => recipe.id === this.id)
    },
    rating () {
      const rating = this.userRatings.find(rating => rating.id === this.id)
      return rating ? rating.value : 0
    }
  },

  data () {
    return {
      id: null,
      recipe: null,
      userRatings: [],
      userLikes: [],
      ingredients: [],
      columns: [
        { name: 'name', text: 'Name', sortable: true, initiallySorted: true },
        { name: 'quantity', text: 'Quantity' }
      ],
      comments: comments,
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
      this.id = Number(this.$route.params.id)
      this.recipe = null
      this.userRatings = this.ingredients = this.userLikes = []
      this.recipe = await API.getRecipeById(this.id)
      this.ingredients = await API.getIngredientFromIdRecipe(this.id)
      await this.fetchUserLikes()
      await this.fetchUserRatings()
    },
    async fetchUserLikes () {
      this.userLikes = await API.getUserLikes(this.userId)
    },
    async fetchUserRatings () {
      this.userRatings = await API.getUserRecipeRatings(this.userId)
    },
    async like () {
      await API.userLikeRecipe(this.userId, this.id)
      this.fetchUserLikes()
    },
    async unlike () {
      await API.userUnlikeRecipe(this.userId, this.id)
      this.fetchUserLikes()
    },
    async rate (rating) {
      await API.userRateRecipe(this.userId, this.id, rating, this.rating !== 0)
      this.fetchUserRatings()
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
      flex-shrink: 0;

      &:not(:last-child) {
        margin-right: 16px;
      }
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
