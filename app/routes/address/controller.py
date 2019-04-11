from flask import Blueprint, request
from app.helpers import response, exceptions, queries
from .dao import AddressDao
from .model import AddressModel

routes = Blueprint('address', __name__)
addressDao = AddressDao()

@routes.route('/', methods=['GET'])
@response.handleExceptions
def index():
  return response.success(addressDao.getAll())

@routes.route('/', methods=['POST'])
@response.handleExceptions
def addAddress():
  body = request.get_json(force=True)
  data = {
    "number": body['number'],
    "apartment": body['apartment'],
    "street": body['street'],
    "city": body['city'],
    "country": body['country']
  }
  addressModel = AddressModel(**data)
  result = addressDao.save(addressModel)
  return response.success(result)