<template>
  <div class="ingredient-editor">
    <h3>Ingredients</h3>
    <IngredientEditorItem
      v-for="(ingredient, i) in ingredients"
      :key="ingredient.id || i"
      :initial-ingredient="ingredient"
      @remove="removeIngredient(i)"
      @change="(ingredient) => updateIngredient(i, ingredient)"
    />
    <Button
      accent
      @click="addIngredient"
    >
      New ingredient
    </Button>
  </div>
</template>

<script>
import IngredientEditorItem from '@/components/ingredients/IngredientEditorItem'
import Button from '@/components/buttons/Button'

export default {

  name: 'IngredientEditor',

  components: {
    IngredientEditorItem,
    Button
  },

  props: {
    initialIngredients: {
      type: Array,
      default: () => []
    }
  },

  data () {
    return {
      ingredients: this.initialIngredients
    }
  },

  methods: {
    addIngredient () {
      this.ingredients.push({
        id_Ingredient: null,
        id_QuantityUnit: null,
        totalQuantity: null
      })
    },
    removeIngredient (index) {
      // const index = this.ingredients.findIndex(x => x.id === id)
      this.ingredients.splice(index, 1)
    },
    updateIngredient (i, ingredient) {
      this.ingredients[i] = ingredient
      this.$emit('change', this.ingredients)
    }
  },

  mounted () {
    if (!this.ingredients.length) {
      this.addIngredient()
    }
  }

}
</script>
