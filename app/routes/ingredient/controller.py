from flask import Blueprint
from app.helpers import response, exceptions, queries
from .dao import IngredientDao

routes = Blueprint('ingredients', __name__)
ingredientDao = IngredientDao()

@routes.route('')
@response.handleExceptions
def index():
  return response.success(ingredientDao.getAll())

@routes.route('/<name>')
@response.handleExceptions
def getAllRecipesByUser(name):
  data = ingredientDao.getIngredientByName(name)
  return response.success(data)
