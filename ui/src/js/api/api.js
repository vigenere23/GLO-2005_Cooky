import { AxiosHelper } from '@/js/helpers/axios'
const BASE_URL = ' http://127.0.0.1:5000'
getRecipe()

export class API {

  static async getUserById(id) {
    const url = '${BASE_URL}/users/${id}'
    return AxiosHelper.axiosGet(url)
  }

  static async getRecipeByUser(id) {
    const url = '${BASE_URL}/users/${id}/recipes'
    return AxiosHelper.axiosGet(url)
  }

  static async getLikedRecipes(id) {
    const url = '${BASE_URL}/users/${id}/likes'
    return AxiosHelper.axiosGet(url)
  }

  static async getProfile(id) {
    const url = '${BASE_URL}/users/${id}/profile'
    return AxiosHelper.axiosGet(url)
  }

  static async getAllCartFromUserId(id) {
    const url = '${BASE_URL}/users/${id}/cart'
    return AxiosHelper.axiosGet(url)
  }

  static async getRecipe() {
    const url = '${BASE_URL}/recipes'
    console.log("jsuis call")
    return AxiosHelper.axiosGet(url)
  }

  static async getRecipeById(id) {
    const url = '${BASE_URL}/recipes/${id}'
    return AxiosHelper.axiosGet(url)

  }

  static async getRecipeByName(name) {
    const url = '${BASE_URL}/recipes/name/{name}'
    return AxiosHelper.axiosGet(url)
  }

  static async getIngredientFromIdRecipe() {
    const url = '${BASE_URL}/recipes$/{id}/ingredients'
    return AxiosHelper.axiosGet(url)

  }

  static async getIngredients () {
    const url = `${BASE_URL}/ingredients`
    return AxiosHelper.axiosGet(url)
  }

  static async getIngredientByName () {

  }

  static async getCartItem () {

  }

  static async getCommandFromCart () {

  }

  static async addIngredientToCart () {

  }

  static async addRecipe () {

  }

  static async addComment () {

  }

  static async addLike () {

  }

  static async addRating () {

  }

  static async addNewCommand () {

  }

  static async addNewUser () {

  }
}
