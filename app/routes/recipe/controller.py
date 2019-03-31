from flask import Blueprint
from app.helpers import response, exceptions, queries
from .dao import RecipeDao

routes = Blueprint('recipes', __name__)
recipeDao = RecipeDao()

@routes.route('/')
@response.handleExceptions
def index():
  return response.success(recipeDao.getAll())
