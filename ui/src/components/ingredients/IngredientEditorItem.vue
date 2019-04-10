<template>
  <div class="ingredient-editor-item">
    <span>hey</span>
  </div>
</template>

<script>
export default {

  name: 'IngredientEditorItem',

  props: {
    initialName: {
      type: String,
      default: ''
    },
    initialMesure: {
      type: String,
      default: ''
    },
    initialQuantity: {
      type: Number,
      default: 1
    }
  },

  data () {
    return {
      ingredient: this.initialIngredient
    }
  }

}
</script>

<style>
.ingredient-editor-item {
  display: flex;
}
</style>
