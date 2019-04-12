<template>
  <div class="ingredient-editor-item">
    <Dropdown
      class="ingredient"
      v-if="ingredients"
      label="name"
      text-attribute="name"
      :items="ingredients"
      @input="updateId"
    />
    <Dropdown
      class="unit"
      label="unit"
      :disabled="!units.length"
      text-attribute="abbreviation"
      :items="units"
      @input="updateUnitId"
    />
    <Dropdown
      class="quantity"
      v-if="quantities"
      label="quantity"
      :items="quantities"
      @input="updateQuantity"
    />
    <div
      class="remove-item"
      @click="$emit('remove')"
    >
      <span class="material-icons">
        close
      </span>
    </div>
  </div>
</template>

<script>
import Dropdown from '@/components/inputs/Dropdown'
import { API } from '@/js/api/api'

export default {

  name: 'IngredientEditorItem',

  components: {
    Dropdown
  },

  props: {
    initialIngredient: {
      type: Object,
      required: true
    }
  },

  data () {
    return {
      ingredientId: this.initialIngredient.id_Ingredient,
      unitQuantityId: this.initialIngredient.id_QuantityUnit,
      quantity: this.initialIngredient.totalQuantity,
      ingredients: null,
      units: [],
      quantities: null
    }
  },

  computed: {
    ingredient () {
      return {
        id_Ingredient: this.ingredientId,
        id_QuantityUnit: this.unitQuantityId,
        totalQuantity: this.quantity
      }
    }
  },

  methods: {
    async updateId (ingredient) {
      this.ingredientId = ingredient.id
      await this.getUnits()
      this.emitChange()
    },
    updateQuantity (quantity) {
      this.quantity = quantity
      this.emitChange()
    },
    updateUnitId (unit) {
      this.unitQuantityId = unit.id
      this.emitChange()
    },
    emitChange () {
      if (this.ingredientId && this.quantity && this.unitQuantityId) {
        this.$emit('change', this.ingredient)
      }
    },
    getQuantities () {
      const quantities = []
      for (let i = 1; i < 100; i++) {
        quantities.push(i)
      }
      return quantities
    },
    async getUnits () {
      this.units = await API.getQuantityUnitsOfIngredient(this.ingredientId)
      this.unitQuantityId = null
    }
  },

  async mounted () {
    this.ingredients = await API.getIngredients()
    this.ingredients.sort()
    this.quantities = this.getQuantities()
  }

}
</script>

<style lang="scss">
.ingredient-editor-item {
  display: flex;
  align-items: flex-end;
  width: 100%;

  .ingredient {
    flex-basis: 50%;
  }

  .unit {
    flex-basis: 20%;
  }

  .quantity {
    flex-basis: 20%;
  }

  .remove-item {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 64px;
    height: 64px;
    cursor: pointer;
  }
}
</style>
