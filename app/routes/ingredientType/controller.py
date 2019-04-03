from flask import Blueprint
from app.helpers import response, exceptions, queries
from .dao import IngredientTypeDao

routes = Blueprint('ingredientsType', __name__)
ingredientDao = IngredientTypeDao()

@routes.route('/')
@response.handleExceptions
def index():
  return response.success(ingredientDao.getAll())