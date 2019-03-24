from app import db
from .schema import UserSchema
from .model import UserModel
from app.helpers.BaseDao import BaseDao
from app.helpers.exceptions import NotFoundException

class UserDao(BaseDao):

  def __init__(self):
    self.schema = UserSchema()

  def getAll(self):
    query = 'SELECT * FROM User'
    results = db.select(query)
    return self.schema.from_tuples(results)

  def getById(self, id):
    query = 'SELECT * FROM User WHERE id = %(id)s'
    result = db.select(query, { 'id': id }, 1)
    if result:
      return self.schema.from_tuple(result)
    else:
      raise NotFoundException(str.format("No user found with id '%d'", id))

  def save(self, userModel):
    if not isinstance(userModel, UserModel):
      raise ValueError("userModel should be of type UserModel")
    pass
