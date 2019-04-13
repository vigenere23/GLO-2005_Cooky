from app import db
from .model import UserModel
from app.helpers.BaseDao import BaseDao
from app.helpers.exceptions import NotFoundException

class UserDao(BaseDao):

  def __init__(self):
    super().__init__('User', UserModel)

  def getByUsername(self, username):
    query = 'SELECT * FROM User WHERE username = %(username)s'
    result = db.select(query, {'username': username}, 1)
    if result:
      return self._mapper.from_tuple(result)
    else:
      raise NotFoundException(str.format("No user found with username '%s'", username))

  def save(self, userModel):
    if not isinstance(userModel, UserModel):
      raise ValueError("userModel should be of type UserModel")
    query = 'INSERT INTO User (id, username, bio) VALUES (%s, %s, %s)'
    userId = db.insert(query, self._mapper.to_tuple(userModel))
      
    if userId:
      return self.getById(userId)
    else:
      raise Exception("Could not save user")
