<template>
  <div
    class="user-page"
    v-if="user"
  >
    <h1>{{ user.username }}</h1>
    <TabSlider
      :tabs="tabs"
      v-if="recipes && likes"
    >
      <template #recipes>
        <GridList
          :items="recipes"
          baselink="/recipes"
        />
      </template>
      <template #likes>
        <GridList
          :items="likes"
          baselink="/recipes"
        />
      </template>
    </TabSlider>
  </div>
</template>

<script>
import TabSlider from '@/components/lists/TabSlider'
import GridList from '@/components/lists/GridList'
import { API } from '@/js/api/api'

export default {

  name: 'User',

  components: {
    TabSlider,
    GridList
  },

  data () {
    return {
      tabs: [
        'recipes',
        'likes'
      ],
      user: null,
      recipes: null,
      likes: null
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
      this.user = this.recipes = this.likes = null
      const id = this.$route.params.id
      this.user = await API.getUserById(id)
      this.recipes = await API.getRecipesByUser(id)
      this.likes = await API.getLikedRecipesByUser(id)
    }
  }

}
</script>
