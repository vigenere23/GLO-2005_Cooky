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
      <Button
        accent
        :disable="!enableButton"
        @click="submit"
      />
    </div>
  </div>
</template>

<script>
import LabelInput from '@/components/inputs/LabelInput'
import Button from '@/components/buttons/Button'
import { API } from '@/js/api/api'
import { mapState } from 'vuex'

export default {

  name: 'RecipeCreate',

  components: {
    LabelInput,
    Button
  },

  computed: {
    ...mapState('user', ['userId']),
    enableButton () {
      return this.name && this.directives && this.ingredients
    }
  },

  data () {
    return {
      name: '',
      description: '',
      directives: '',
      ingredients: []
    }
  },

  methods: {
    submit () {
      API.addRecipe(this.userId, this.name, this.directives, this.ingredients)
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
