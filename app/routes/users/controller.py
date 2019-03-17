from flask import Blueprint
from app.helpers import response, exceptions, queries
from . import dao

routes = Blueprint('user', __name__)

@routes.route('/')
@response.handleExceptions
def index():
  return response.success(dao.getAll())

@routes.route('/<int:id>')
@response.handleExceptions
def getOne(id):
  data = dao.getById(id)
  return response.success(data)
