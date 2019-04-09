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

  static async getProfile (id) {
    const url = `${BASE_URL}/users/${id}/profile`
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

  static async getIngredientByName (name) {
    const url = `${BASE_URL}/ingredients/${name}`
    return AxiosHelper.axiosGet(url)
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

  static async addRecipe (userId, recipeName, instruction, ingredientList, quantityUnitList, totalQuantityList) {
    const body = {
      'id_User': userId,
      'name': recipeName,
      'directives': instruction,
      'ingredients': {
        'id_Ingredient': ingredientList,
        'id_QuantityUnit': quantityUnitList,
        'totalQuantity': totalQuantityList
      }
    }
    const url = `${BASE_URL}/recipes`
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
}
