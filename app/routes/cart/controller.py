from flask import Blueprint, request, json
from app.helpers import response, exceptions, queries
from datetime import datetime
from ..cartItem.model import CartItemModel
from .dao import CartDao
from ..cartItem.dao import CartItemDao
from ..commands.dao import CommandsDao
from ..commands.model import CommandsModel

routes = Blueprint('cart', __name__)
cartDao = CartDao()
cartItemDao = CartItemDao()
commandsDao = CommandsDao()

@routes.route('/')
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

@routes.route('/<int:id>/cartItems', methods=['GET'])
@response.handleExceptions
def getItemByCart(id):
  data = cartItemDao.getItemByCart(id)
  return response.success(data)

@routes.route('/<int:id_Cart>/cartItems/<int:id_Ingredient>/ingredient', methods=['DELETE'])
@response.handleExceptions
def deleteItemFromCart(id_Cart, id_Ingredient):
  id_Ingredient =  str(id_Ingredient),
  id_Cart = str(id_Cart)
    
  cartItemDao.deleteIngredient(id_Cart, id_Ingredient) 
  return response.success("", status=204)

@routes.route('/<int:id_Cart>/cartItems/<int:id_Ingredient>/ingredient', methods=['PUT'])
@response.handleExceptions
def modifyRecipeName(id_Cart, id_Ingredient):
  body = request.get_json(force=True)
  result = cartItemDao.modifyQuantity(body['multiplier'], id_Cart, id_Ingredient)
  return response.success(result)


@routes.route('/<int:id>/command', methods=['GET'])
@response.handleExceptions
def getCommandsByCart(id):
  data = commandsDao.getCommandByCart(id)
  if (data):
    return response.success(data)
  else:
    return response.error("This cart is not in command")


@routes.route('/<int:id>/command', methods=['POST'])
@response.handleExceptions
def addCommandFromCart(id):
  data = {
    'id_Cart': str(id),
    'creationDate': datetime.today().strftime('%Y-%m-%d'),
    'arrivalDate': datetime.today().strftime('%Y-%m-%d')
  }
  commandsModel = CommandsModel(**data)
  data = commandsDao.save(commandsModel)
  return response.success(data)
