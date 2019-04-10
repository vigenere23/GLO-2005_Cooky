<template>
  <div class="recipe-create-page">
    <h1>Create a recipe</h1>
    <div class="form">
      <LabelInput
        label="name"
        v-model="name"
      />
      <LabelInput
        label="description"
        type="textarea"
        allow-empty
        v-model="description"
      />
      <LabelInput
        label="directives"
        type="textarea"
        v-model="directives"
      />
    </div>
  </div>
</template>

<script>
import LabelInput from '@/components/inputs/LabelInput'

export default {

  name: 'RecipeCreate',

  components: {
    LabelInput
  },

  data () {
    return {
      name: '',
      description: '',
      directives: ''
    }
  }

}
</script>

<style lang="scss">
@import '~@/assets/scss/variables';

.recipe-create-page {
  .form {
    width: 100%;
    max-width: 600px;
    margin: auto;
  }
}
</style>
