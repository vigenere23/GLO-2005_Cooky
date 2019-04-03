import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export const router = new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: require('@/views/Home.vue').default
    },
    {
      path: '/signup',
      name: 'Signup',
      component: () => import('@/views/Signup.vue')
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import('@/views/Login.vue')
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
      path: '/users/:id/edit',
      name: 'UserEdit',
      component: () => import('@/views/private/UserEdit.vue')
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
      path: '/cart',
      name: 'Cart',
      component: () => import('@/views/private/Cart.vue')
    },
    {
      path: '/commands',
      name: 'Commands',
      component: () => import('@/views/private/Commands.vue')
    },
    {
      path: '/settings',
      name: 'Settings',
      component: () => import('@/views/private/Settings.vue')
    },
    {
      path: '/logout',
      name: 'Logout',
      component: () => import('@/views/private/Logout.vue')
    },
    {
      path: '*',
      name: 'PageNotFound',
      component: () => import('@/views/PageNotFound.vue')
    }
  ]
})
