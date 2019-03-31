from flask import Blueprint, request
from app.helpers import response, exceptions, queries
from .dao import UserDao

routes = Blueprint('users', __name__)
userDao = UserDao()

@routes.route('/', methods=['GET', 'POST'])
@response.handleExceptions
def index():
  if request.method == 'GET':
    return response.success(userDao.getAll())
  else:
    try:
      result = userDao.create()
      return response.success(result)
    except Exception as e:
      return response.error(e)

@routes.route('/<int:id>')
@response.handleExceptions
def getOne(id):
  data = userDao.getById(id)
  return response.success(data)
