from flask import Blueprint
from app.helpers import response, exceptions, queries
from .dao import RecipeDao
from ..recipeIngredient.dao import RecipeIngredientDao

routes = Blueprint('recipes', __name__)
recipeDao = RecipeDao()
recipeIngredientDao = RecipeIngredientDao()

@routes.route('/')
@response.handleExceptions
def index():
  return response.success(recipeDao.getAll())

@routes.route('/<int:recipe_id>')
@response.handleExceptions
def getRecipeById(recipe_id):
  data = recipeDao.getRecipeById(recipe_id)
  return response.success(data)

@routes.route('/<int:recipe_id>/ingredients')
@response.handleExceptions
def getIngredientsByRecipe(recipe_id):
  data = recipeIngredientDao.getIngredientsByRecipe(recipe_id)
  return response.success(data)
