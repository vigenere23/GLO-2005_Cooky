from flask import Blueprint
from app.helpers import response, exceptions, queries
from .dao import AddressDao

routes = Blueprint('address', __name__)
addressDao = AddressDao()

@routes.route('/')
@response.handleExceptions
def index():
  return response.success(addressDao.getAll())