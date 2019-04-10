import { AxiosHelper } from '@/js/helpers/axios'
const BASE_URL = ' http://127.0.0.1:5000'

export class API {
  static async getUserById (id) {
    const url = `${BASE_URL}/users/${id}`
    return AxiosHelper.axiosGet(url)
  }

  static async getRecipesByUser (userId) {
    const url = `${BASE_URL}/users/${userId}/recipes`
    return AxiosHelper.axiosGet(url)
  }

  static async getLikedRecipesByUser (userId) {
    const url = `${BASE_URL}/users/${userId}/likes`
    return AxiosHelper.axiosGet(url)
  }

  static async getAccount (id) {
    const url = `${BASE_URL}/users/${id}/account`
    return AxiosHelper.axiosGet(url)
  }

  static async getProfile (id) {
    const url = `${BASE_URL}/users/${id}/profile`
    return AxiosHelper.axiosGet(url)
  }

  static async getAddress (id) {
    const url = `${BASE_URL}/users/${id}/address`
    return AxiosHelper.axiosGet(url)
  }

  static async getAllCartFromUserId (id) {
    const url = `${BASE_URL}/users/${id}/cart`
    return AxiosHelper.axiosGet(url)
  }

  static async getRecipes () {
    const url = `${BASE_URL}/recipes`
    return AxiosHelper.axiosGet(url)
  }

  static async getRecipeById (id) {
    const url = `${BASE_URL}/recipes/${id}`
    return AxiosHelper.axiosGet(url)
  }

  static async getRecipesByName (name) {
    const url = `${BASE_URL}/recipes`
    const params = { name }
    return AxiosHelper.axiosGet(url, { params })
  }

  static async getIngredientFromIdRecipe (recipeId) {
    const url = `${BASE_URL}/recipes/${recipeId}/ingredients`
    return AxiosHelper.axiosGet(url)
  }

  static async getIngredients () {
    const url = `${BASE_URL}/ingredients`
    return AxiosHelper.axiosGet(url)
  }

  static async getIngredientsByName (name) {
    const url = `${BASE_URL}/ingredients`
    const params = { name }
    return AxiosHelper.axiosGet(url, { params })
  }

  static async getCartItem (id) {
    const url = `${BASE_URL}/cart/${id}/cartItems`
    return AxiosHelper.axiosGet(url)
  }

  static async getCommandFromCart (id) {
    const url = `${BASE_URL}/cart/${id}/command`
    return AxiosHelper.axiosGet(url)
  }

  static async addIngredientToCart (cartId, ingredientId, subCost) {
    const body = {
      'id_Ingredient': ingredientId,
      'subCost': subCost
    }
    const url = `${BASE_URL}/cart/${cartId}/cartItems`
    return AxiosHelper.axiosPost(url, body)
  }

  static async addRecipe (userId, name, directives, ingredients) {
    const body = {
      'id_User': userId,
      name,
      directives,
      ingredients
    }
    const url = `${BASE_URL}/recipes/`
    return AxiosHelper.axiosPost(url, body)
  }

  static async addComment (recipeId, userId, comment) {
    const body = {
      'id_User': userId,
      'text': comment
    }
    const url = `${BASE_URL}/recipes/${recipeId}/comment`
    return AxiosHelper.axiosPost(url, body)
  }

  static async addLike (recipeId, userId) {
    const body = {
      'id_User': userId
    }
    const url = `${BASE_URL}/recipes/${recipeId}/like`
    return AxiosHelper.axiosPost(url, body)
  }

  static async addRating (recipeId, userId, mark) {
    const body = {
      'id_User': userId,
      'value': mark
    }
    const url = `${BASE_URL}/recipes/${recipeId}/rate`
    return AxiosHelper.axiosPost(url, body)
  }

  static async addNewUser (userName) {
    const body = {
      'username': userName
    }
    const url = `${BASE_URL}/users`
    return AxiosHelper.axiosPost(url, body)
  }

  static async addNewCommand (cartId) {
    const url = `${BASE_URL}/cart/${cartId}/command`
    return AxiosHelper.axiosPost(url)
  }

  static async deleteIngredientFromCart (cartId, ingredientId) {
    const url = `${BASE_URL}/cart/${cartId}/cartItems/${ingredientId}/ingredient`
    return AxiosHelper.axiosDelete(url)
  }

  static async deleteRecipe (recipeId) {
    const url = `${BASE_URL}/recipes/${recipeId}`
    return AxiosHelper.axiosDelete(url)
  }

  static async modifyRecipeName (recipeId, recipeName) {
    const body = {
      'name': recipeName
    }
    const url = `${BASE_URL}/recipes/${recipeId}/name`
    return AxiosHelper.axiosPut(url, body)
  }

  static async modifyRecipeDirectives (recipeId, directives) {
    const body = {
      'directives': directives
    }
    const url = `${BASE_URL}/recipes/${recipeId}/directives`
    return AxiosHelper.axiosPut(url, body)
  }

  static async modifyRecipeIngredientQuantity (recipeId, ingredientId, totalQuantity) {
    const body = {
      'id_Ingredient': ingredientId,
      'totalQuantity': totalQuantity
    }
    const url = `${BASE_URL}/recipes/${recipeId}/ingredientQuantity`
    return AxiosHelper.axiosPut(url, body)
  }

  static async modifyFirstName (userId, firstName) {
    const body = {
      'firstName': firstName
    }
    const url = `${BASE_URL}/users/${userId}/firstName`
    return AxiosHelper.axiosPut(url, body)
  }

  static async modifyLastName (userId, lastName) {
    const body = {
      'lastName': lastName
    }
    const url = `${BASE_URL}/users/${userId}/lastName`
    return AxiosHelper.axiosPut(url, body)
  }

  static async modifyEmail (userId, email) {
    const body = {
      'email': email
    }
    const url = `${BASE_URL}/users/${userId}/email`
    return AxiosHelper.axiosPut(url, body)
  }

  static async modifyPassword (userId, password) {
    const body = {
      'password': password
    }
    const url = `${BASE_URL}/users/${userId}/password`
    return AxiosHelper.axiosPut(url, body)
  }

  static async modifyQuantityCartItems (cartId, ingredientId, multiplier) {
    const body = {
      'multiplier': multiplier
    }
    const url = `${BASE_URL}/cart/${cartId}/cartItems/${ingredientId}/ingredient`
    return AxiosHelper.axiosPut(url, body)
  }
}
