from flask import Blueprint
from app.helpers import response, exceptions, queries
from .dao import UserDao

routes = Blueprint('user', __name__)
userDao = UserDao()

@routes.route('/')
@response.handleExceptions
def index():
  return response.success(userDao.getAll())

@routes.route('/<int:id>')
@response.handleExceptions
def getOne(id):
  data = userDao.getById(id)
  return response.success(data)
