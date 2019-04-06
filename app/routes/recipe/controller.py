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

routes = Blueprint('recipes', __name__) 
recipeDao = RecipeDao()
likeRecipeDao = LikeRecipeDao()
commentDao = CommentDao()
ratingDao = RatingDao()
recipeIngredientDao = RecipeIngredientDao()

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

@routes.route('/<int:recipe_id>')
@response.handleExceptions
def getRecipeById(recipe_id):
  data = recipeDao.getRecipeById(recipe_id)
  return response.success(data)

@routes.route('/name/<name>')
@response.handleExceptions
def getRecipeByName(name):
  data = recipeDao.getRecipeByName(name)
  return response.success(data)

@routes.route('/<int:recipe_id>/ingredients')
@response.handleExceptions
def getIngredientsByRecipe(recipe_id):
  data = recipeIngredientDao.getIngredientsByRecipe(recipe_id)
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



@routes.route('/<int:recipe_id>/rate', methods=['POST'])
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

