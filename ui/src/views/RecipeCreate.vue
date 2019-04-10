<template>
  <div class="recipe-create-page">
    <LabelInput
      label="name"
      v-model="name"
    />
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
      name: 'A test'
    }
  }

}
</script>
