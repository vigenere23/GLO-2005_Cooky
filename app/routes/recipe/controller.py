from flask import Blueprint, request
from app.helpers import response, exceptions, queries
from .dao import RecipeDao
from .model import RecipeModel
from ..recipeIngredient.dao import RecipeIngredientDao
from ..likeRecipe.model import LikeRecipeModel
from ..likeRecipe.dao import LikeRecipeDao
from ..comment.model import CommentModel
from ..comment.dao import CommentDao
from ..rating.model import RatingModel
from ..rating.dao import RatingDao
from ..ingredient.dao import IngredientDao
from ..quantityUnit.dao import QuantityUnitDao
from ..users.dao import UserDao

routes = Blueprint('recipes', __name__) 
recipeDao = RecipeDao()
likeRecipeDao = LikeRecipeDao()
commentDao = CommentDao()
ratingDao = RatingDao()
recipeIngredientDao = RecipeIngredientDao()
ingredientDao = IngredientDao()
quantityUnitDao = QuantityUnitDao()
userDao = UserDao()

@routes.route('', methods=['GET'])
@response.handleExceptions
def index():
  return response.success(recipeDao.getAll())

@routes.route('', methods=['POST'])
@response.handleExceptions
def addRecipe():
  body = request.get_json(force=True)
  data = {
      'id_User': body['id_User'],
      'name': body['name'],
      'directives': body['directives']
  }

  try:
    recipeModel = RecipeModel(**data)
    result = recipeDao.save(recipeModel,  body['ingredients'])
    return response.success(result)
  except Exception as e:
    return response.error(e)

@routes.route('/<int:recipe_id>', methods=['GET'])
@response.handleExceptions
def getRecipeById(recipe_id):
  recipe = recipeDao.getById(recipe_id)
  user = userDao.getById(recipe.id_User)
  data = {
    **recipe.serialize(),
    'user': {
      **user.serialize()
    }
  }
  return response.success(data)

@routes.route('/<int:recipe_id>', methods=['DELETE'])
@response.handleExceptions
def deleteRecipe(recipe_id):
  recipeDao.deleteRecipe(recipe_id) 
  return response.success('', status=204)

# should be a query param in getAll (?name="asdasd")
# should be like a search function, not absolute name
@routes.route('/name/<name>')
@response.handleExceptions
def getRecipeByName(name):
  data = recipeDao.getRecipeByName(name)
  return response.success(data)

@routes.route('/<int:recipe_id>/ingredients')
@response.handleExceptions
def getIngredientsByRecipe(recipe_id):
  data = []
  recipeIngredients = recipeIngredientDao.getIngredientsByRecipe(recipe_id)
  for recipeIngredient in recipeIngredients:
    ingredient = ingredientDao.getById(recipeIngredient.id_Ingredient)
    quantityUnit = quantityUnitDao.getById(recipeIngredient.id_QuantityUnit)
    quantity = str.format('{} {}', int(recipeIngredient.totalQuantity), quantityUnit.abbreviation)
    data.append({
      'id': ingredient.id,
      'name': ingredient.name,
      'quantity': quantity
    })

  return response.success(data)

@routes.route('/<int:recipe_id>/like', methods=['POST'])
@response.handleExceptions
def addLikeRecipe(recipe_id):
  body = request.get_json(force=True)
  data = {
      'id_Recipe': str(recipe_id),
      'id_User': body['id_User']
  }

  try:
    likeRecipeModel = LikeRecipeModel(**data)
    result = likeRecipeDao.save(likeRecipeModel)
    return response.success(result)
  except Exception as e:
    return response.error(e)



@routes.route('/<int:recipe_id>/rating', methods=['POST'])
@response.handleExceptions
def addRateRecipe(recipe_id):
  body = request.get_json(force=True)
  data = {
      'id_Recipe': str(recipe_id),
      'id_User': body['id_User'],
      'value': body['value']
  }

  try:
    ratingModel = RatingModel(**data)
    result = ratingDao.save(ratingModel)
    return response.success(result)
  except Exception as e:
    return response.error(e)

@routes.route('/<int:recipe_id>/comment', methods=['POST'])
@response.handleExceptions
def addCommentRecipe(recipe_id):
  body = request.get_json(force=True)
  data = {
    'id_Recipe': str(recipe_id),
    'id_User': body['id_User'],
    'text': body['text']
  }

  try:

    commentModel = CommentModel(**data)
    result = commentDao.save(commentModel)
    return response.success(result)
  except Exception as e:
    return response.error(e)

