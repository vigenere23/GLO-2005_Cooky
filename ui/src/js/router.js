import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: require('@/views/Home.vue').default
    },
    {
      path: '/recipes',
      name: 'Recipes',
      component: () => import('@/views/Recipes.vue')
    },
    {
      path: '/recipes/:id',
      name: 'Recipe',
      component: () => import('@/views/Recipe.vue')
    },
    {
      path: '/ingredients',
      name: 'Ingredients',
      component: () => import('@/views/Ingredients.vue')
    },
    {
      path: '/ingredients/:id',
      name: 'Ingredient',
      component: () => import('@/views/Ingredient.vue')
    },
    {
      path: '/users/:id',
      name: 'User',
      component: () => import('@/views/User.vue')
    },
    {
      path: '/users/:id/recipes',
      name: 'UserRecipes',
      component: () => import('@/views/UserRecipes.vue')
    },
    {
      path: '/users/:id/likes',
      name: 'UserLikes',
      component: () => import('@/views/UserLikes.vue')
    },
    {
      path: '/users/:id/comments',
      name: 'UserComments',
      component: () => import('@/views/UserComments.vue')
    },
    {
      path: '*',
      name: 'PageNotFound',
      component: () => import('@/views/PageNotFound.vue')
    }
  ]
})
