from flask import Blueprint
from app.helpers import response, exceptions, queries
from .dao import CartDao
from ..cartItem.dao import CartItemDao
from ..commands.dao import CommandsDao

routes = Blueprint('cart', __name__)
cartDao = CartDao()
cartItemDao = CartItemDao()
commandsDao = CommandsDao()

@routes.route('/')
@response.handleExceptions
def index():
  return response.success(cartDao.getAll())

##### 
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
