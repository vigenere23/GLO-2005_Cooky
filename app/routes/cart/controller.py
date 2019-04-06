from flask import Blueprint, request, json
from app.helpers import response, exceptions, queries
from ..cartItem.model import CartItemModel
from .dao import CartDao
from ..cartItem.dao import CartItemDao
from ..commands.dao import CommandsDao

routes = Blueprint('cart', __name__)
cartDao = CartDao()
cartItemDao = CartItemDao()
commandsDao = CommandsDao()

@routes.route('')
@response.handleExceptions
def index():
  return response.success(cartDao.getAll())

@routes.route('/<int:id>/cartItems', methods=['POST'])
@response.handleExceptions
def addItemToCart(id):
  body = request.get_json(force=True)
  data = {
      'id_Ingredient': body['id_Ingredient'],
      'id_Cart': str(id),
      'multiplier': '1',
      'subCost': body['subCost']
  }

  try:

    cartItemModel = CartItemModel(**data)
    result = cartItemDao.save(cartItemModel)
    return response.success(result)
  except Exception as e:
    return response.error(e)

@routes.route('/<int:id>/cartItems')
@response.handleExceptions
def getItemByCart(id):
  data = cartItemDao.getItemByCart(id)
  return response.success(data)

@routes.route('/<int:id>/command')
@response.handleExceptions
def getCommandsByCart(id):
  data = commandsDao.getCommandByCart(id)
  return response.success(data)
