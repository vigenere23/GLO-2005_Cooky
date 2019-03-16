from flask import Blueprint
from app import response, exceptions
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
