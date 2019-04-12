from flask import Blueprint, request
from app.helpers import response, exceptions, queries
from .dao import UserDao
from .model import UserModel
from ..recipe.dao import RecipeDao
from ..likeRecipe.dao import LikeRecipeDao
from ..carts.dao import CartDao
from ..account.model import AccountModel
from ..account.dao import AccountDao
from ..address.dao import AddressDao
from ..address.model import AddressModel

routes = Blueprint('users', __name__)
userDao = UserDao()
recipeDao = RecipeDao()
likeRecipeDao = LikeRecipeDao()
cartDao = CartDao()
accountDao = AccountDao()
addressDao = AddressDao()

@routes.route('/', methods=['GET'])
@response.handleExceptions
def index():
  return response.success(userDao.getAll())

@routes.route('/', methods=['POST'])
@response.handleExceptions
def createUser():
  body = request.get_json(force=True)
  try:
    userDao.getByUsername(body['username']).serialize()
    return response.error("The username already exists")
  except:
    try:
      userModel = UserModel(**body)
      result = userDao.save(userModel)
      return response.success(result)
    except Exception as e:
      return response.error(e)

@routes.route('/<int:id>/account', methods=['GET'])
@response.handleExceptions
def getAccount(id):
   return response.success(accountDao.getAccountByUserId(id))
  
@routes.route('/<int:id>/account/', methods=['POST'])
@response.handleExceptions
def addAccount(id):
  print("j'ai été call")
  body = request.get_json(force=True)
  data = {
    'id_User': str(id),
    'id_Address': body['id_Address'],
    'firstName': body['firstName'],
    'lastName': body['lastName'],
    'email': body['email'],
    'password': body['password']
  }

  accountModel = AccountModel(**data)
  result = accountDao.save(accountModel)
  return response.success(result)

@routes.route('/<int:id>/firstName/', methods=['PUT'])
@response.handleExceptions
def modifyFirstName(id):
  body = request.get_json(force=True)
  try:
    result = accountDao.modifyFirstName(body['firstName'], id)
    return response.success(result)
  except Exception as e:
    return response.error(e)

@routes.route('/<int:id>/lastName/', methods=['PUT'])
@response.handleExceptions
def modifyLastName(id):
  body = request.get_json(force=True)
  try:
    result = accountDao.modifyLastName(body['lastName'], id)
    return response.success(result)
  except Exception as e:
    return response.error(e)

@routes.route('/<int:id>/email/', methods=['PUT'])
@response.handleExceptions
def modifyEmail(id):
  body = request.get_json(force=True)
  try:
    result = accountDao.modifyEmail(body['email'], id) 
    return response.success(result)
  except Exception as e:
    return response.error(e)

@routes.route('/<int:id>/password', methods=['GET'])
@response.handleExceptions
def getUserPassword(id):
  data= accountDao.getAccountByUserId(id)
  return response.success({"password": data.password})

@routes.route('/<int:id>/password/', methods=['PUT'])
@response.handleExceptions
def modifyPassword(id):
  body = request.get_json(force=True)
  try:
    accountDao.modifyPassword(body['password'], id)
    return response.success('')
  except Exception as e:
    return response.error(e)

@routes.route('/<int:id>/', methods=['PUT'])
@response.handleExceptions
def modifyUser(id):
  body = request.get_json(force=True)
  data = userDao.modifyUser(id, body['username'])
  return response.success(data)

@routes.route('/<int:id>')
@response.handleExceptions
def getOne(id):
  data = userDao.getById(id)
  return response.success(data)


@routes.route('/<int:id>/recipes')
@response.handleExceptions
def getAllRecipesByUser(id):
  data = recipeDao.getAllRecipesByUser(id)
  return response.success(data)

@routes.route('/<int:id>/likes')
@response.handleExceptions
def getLikeRecipes(id):
  recipes = []
  likes = likeRecipeDao.getLikeRecipeByUser(id)
  for like in likes:
    recipe = recipeDao.getById(like.id_Recipe)
    recipes.append({
      'id': recipe.id,
      'name': recipe.name,
      'description': recipe.description
    })

  return response.success(recipes)


@routes.route('/<int:id>/cart', methods=['GET'])
@response.handleExceptions
def getUserCart(id):
  data = cartDao.getCurrentUserCart(id)
  return response.success(data)


@routes.route('/<int:id>/address', methods=['GET'])
@response.handleExceptions
def getAddress(id):
  userData = accountDao.getAccountByUserId(id)
  address = userData.id_Address
  return response.success(addressDao.getAddress(address))

@routes.route('/<name>', methods=['GET'])
@response.handleExceptions
def getUserByName(name):
  name = userDao.getByUsername(name)
  return response.success(name)

