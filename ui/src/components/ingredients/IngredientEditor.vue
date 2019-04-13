<template>
  <div class="ingredient-editor">
    <h3>Ingredients</h3>
    <IngredientEditorItem
      v-for="(ingredient, i) in ingredients"
      :key="ingredient.id || i"
      :initial-ingredient="ingredient"
      :ingredients="ingredientList"
      :quantities="quantityList"
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
import { API } from '@/js/api/api'

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
      ingredients: this.initialIngredients,
      ingredientList: [],
      quantityList: []
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
      this.ingredients.splice(index, 1)
    },
    updateIngredient (i, ingredient) {
      this.ingredients[i] = ingredient
      this.$emit('change', this.ingredients)
    },
    getQuantityList () {
      const quantities = []
      for (let i = 1; i < 100; i++) {
        quantities.push(i)
      }
      return quantities
    },
  },

  async mounted () {
    if (!this.ingredients.length) {
      this.addIngredient()
    }
    this.quantityList = this.getQuantityList()
    this.ingredientList = await API.getIngredients()
  }

}
</script>
