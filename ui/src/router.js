import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/recipes",
      name: "recipes",
      component: () => import("@/views/Recipes.vue")
    },
    {
      path: "/recipes/:id",
      name: "recipe",
      component: () => import("@/views/Recipe.vue")
    },
    {
      path: "/ingredients",
      name: "ingredients",
      component: () => import("@/views/Ingredients.vue")
    },
    {
      path: "/ingredients/:id",
      name: "ingredient",
      component: () => import("@/views/Ingredient.vue")
    },
    {
      path: "/users/:id",
      name: "user",
      component: () => import("@/views/User.vue")
    },
    {
      path: "/users/:id/recipes",
      name: "userRecipes",
      component: () => import("@/views/UserRecipes.vue")
    },
    {
      path: "/users/:id/likes",
      name: "userLikes",
      component: () => import("@/views/UserLikes.vue")
    },
    {
      path: "/users/:id/bookmarks",
      name: "userBookmarks",
      component: () => import("@/views/UserBookmarks.vue")
    },
    {
      path: "*",
      name: "404",
      component: () => import("@/views/404.vue")
    }
  ]
});
