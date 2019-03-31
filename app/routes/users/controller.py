from flask import Blueprint, request
from app.helpers import response, exceptions, queries
from .dao import UserDao
from .model import UserModel

routes = Blueprint('users', __name__)
userDao = UserDao()

@routes.route('', methods=['GET'])
@response.handleExceptions
def index():
  return response.success(userDao.getAll())

@routes.route('', methods=['POST'])
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
