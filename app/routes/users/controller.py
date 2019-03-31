from flask import Blueprint, request
from app.helpers import response, exceptions, queries
from .dao import UserDao
from .model import UserModel
from ..recipe.dao import RecipeDao

routes = Blueprint('users', __name__)
userDao = UserDao()
recipeDao = RecipeDao()

@routes.route('', methods=['GET'])
@response.handleExceptions
def index():
  return response.success(userDao.getAll())

@routes.route('', methods=['POST'])
@response.handleExceptions
def createUser():
  body = request.get_json(force=True)
  try:
    userDao.getByUsername(body['username'])
    return response.error("The username already exists")
  except:
    userModel = UserModel(**body)
    result = userDao.save(userModel)
    return response.success(result)

@routes.route('/<int:id>')
@response.handleExceptions
def getOne(id):
  data = userDao.getById(id)
  return response.success(data)

@routes.route('/<int:id>/recipes')
@response.handleExceptions
def getRecipes(id):
  data = recipeDao.getAllRecipesByUser(id)
  return response.success(data)