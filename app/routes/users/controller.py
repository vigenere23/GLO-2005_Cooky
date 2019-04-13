from flask import Blueprint, request
from app.helpers import response, exceptions, queries
from .dao import UserDao
from .model import UserModel
from ..recipe.dao import RecipeDao
from ..likeRecipe.dao import LikeRecipeDao
from ..carts.dao import CartDao
from ..commands.dao import CommandDao
from ..account.model import AccountModel
from ..account.dao import AccountDao
from ..address.dao import AddressDao
from ..address.model import AddressModel
from ..rating.dao import RatingDao

routes = Blueprint('users', __name__)
userDao = UserDao()
recipeDao = RecipeDao()
likeRecipeDao = LikeRecipeDao()
cartDao = CartDao()
commandDao = CommandDao()
accountDao = AccountDao()
addressDao = AddressDao()
ratingDao = RatingDao()

@routes.route('/', methods=['GET'])
@response.handleExceptions
def index():
  return response.success(userDao.getAll())

@routes.route('/', methods=['POST'])
@response.handleExceptions
def createUser():
  body = request.get_json(force=True)
  try:
    userDao.getByUsername(body['username'])
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

@routes.route('/<int:id>/country', methods=['PUT'])
@response.handleExceptions
def modifyCountry(id):
  userData = accountDao.getAccountByUserId(id)
  addressId = userData.id_Address
  body = request.get_json(force=True)
  data = addressDao.modifyCountry(body['country'], addressId)
  return response.success(data)

@routes.route('/<int:id>/city', methods=['PUT'])
@response.handleExceptions
def modifyCity(id):
  userData = accountDao.getAccountByUserId(id)
  addressId = userData.id_Address
  body = request.get_json(force=True)
  data = addressDao.modifyCity(body['city'], addressId)
  return response.success(data)

@routes.route('/<int:id>/street', methods=['PUT'])
@response.handleExceptions
def modifyStreet(id):
  userData = accountDao.getAccountByUserId(id)
  addressId = userData.id_Address
  body = request.get_json(force=True)
  data = addressDao.modifyStreet(body['street'], addressId)
  return response.success(data)

@routes.route('/<int:id>/apartment', methods=['PUT'])
@response.handleExceptions
def modifyApartment(id):
  userData = accountDao.getAccountByUserId(id)
  addressId = userData.id_Address
  body = request.get_json(force=True)
  data = addressDao.modifyApartment(body['apartment'], addressId)
  return response.success(data)

@routes.route('/<int:id>/doorNumber', methods=['PUT'])
@response.handleExceptions
def modifyDoorNumber(id):
  userData = accountDao.getAccountByUserId(id)
  addressId = userData.id_Address
  body = request.get_json(force=True)
  data = addressDao.modifyDoorNumber(body['number'], addressId)
  return response.success(data)

@routes.route('/<int:id>', methods=['GET'])
@response.handleExceptions
def getOne(id):
  data = userDao.getById(id)
  return response.success(data)


@routes.route('/<int:id>/recipes', methods=['GET'])
@response.handleExceptions
def getAllRecipesByUser(id):
  data = recipeDao.getAllRecipesByUser(id)
  return response.success(data)

@routes.route('/<int:id>/likes', methods=['GET'])
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

@routes.route('/<int:id>/ratings', methods=['GET'])
@response.handleExceptions
def getRatings(id):
  data = ratingDao.getRatingsByUser(id)
  return response.success(data)

@routes.route('/<int:id>/cart', methods=['GET'])
@response.handleExceptions
def getUserCart(id):
  data = cartDao.getCurrentUserCart(id)
  return response.success(data)

@routes.route('/<int:id>/commands', methods=['GET'])
@response.handleExceptions
def getUserCommands(id):
  commands = commandDao.getUserCommands(id)
  data = []
  for command in commands:
    cart = cartDao.getById(command.id_Cart)
    data.append({
      **command.serialize(),
      'totalCost': cart.totalCost
    })
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

