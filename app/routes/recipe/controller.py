from flask import Blueprint
from app.helpers import response, exceptions, queries
from .dao import RecipeDao

routes = Blueprint('recipes', __name__)
recipeDao = RecipeDao()

@routes.route('/')
@response.handleExceptions
def index():
  return response.success(recipeDao.getAll())

@routes.route('/<int:id_User>')
@response.handleExceptions
def getAll(id_User):
  data = recipeDao.getAllRecipeByUser(id_User)
  return response.success(data)

