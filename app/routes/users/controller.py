from flask import Blueprint, request
from app.helpers import response, exceptions, queries
from .dao import UserDao
from .model import UserModel
from ..recipe.dao import RecipeDao
from ..likeRecipe.dao import LikeRecipeDao
from ..cart.dao import CartDao

routes = Blueprint('users', __name__)
userDao = UserDao()
recipeDao = RecipeDao()
likeRecipeDao = LikeRecipeDao()
cartDao = CartDao()

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
      'name': recipe.name
    })

  return response.success(recipes)


@routes.route('/<int:id>/cart')
def getCart(id):
  data = cartDao.getCartByUser(id)
  return response.success(data)