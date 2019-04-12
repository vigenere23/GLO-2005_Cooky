<template>
  <div
    class="user-page"
    v-if="user"
  >
    <FloatingButton
      v-if="$route.params.id === userId"
      link="/recipes/create"
    />
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
import FloatingButton from '@/components/buttons/FloatingButton'
import TabSlider from '@/components/lists/TabSlider'
import GridList from '@/components/lists/GridList'
import { API } from '@/js/api/api'
import { mapState } from 'vuex'

export default {

  name: 'User',

  components: {
    FloatingButton,
    TabSlider,
    GridList
  },

  computed: mapState('user', ['userId']),

  data () {
    return {
      tabs: [
        'recipes',
        'likes'
      ],
      id: null,
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
    fetchData () {
      this.id = this.user = this.recipes = this.likes = null
      this.id = this.$route.params.id
      this.fetchUser()
      this.fetchRecipes()
      this.fetchLikes()
    },
    async fetchUser () {
      this.user = await API.getUserById(this.id)
    },
    async fetchRecipes () {
      this.recipes = await API.getRecipesByUser(this.id)
    },
    async fetchLikes () {
      this.likes = await API.getUserLikes(this.id)
    }
  }

}
</script>
