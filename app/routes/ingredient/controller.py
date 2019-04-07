from flask import Blueprint
from app.helpers import response, exceptions, queries
from .dao import IngredientDao
from ..quantityUnit.dao import QuantityUnitDao

routes = Blueprint('ingredients', __name__)
ingredientDao = IngredientDao()
quantityUnitDao = QuantityUnitDao()

@routes.route('')
@response.handleExceptions
def index():
  populated_ingredients = []
  ingredients = ingredientDao.getAll()
  for ingredient in ingredients:
    quantity_unit = quantityUnitDao.getById(ingredient.id_QuantityUnit)
    quantity = str.format('{} {}', int(ingredient.baseQuantity), quantity_unit.abbreviation)
    populated_ingredients.append({
      'id': ingredient.id,
      'name': ingredient.name,
      'quantity': quantity,
      'price': ingredient.baseCost
    })
  return response.success(populated_ingredients)

@routes.route('/<name>')
@response.handleExceptions
def getIngredientByName(name):
  data = ingredientDao.getIngredientByName(name)
  return response.success(data)
