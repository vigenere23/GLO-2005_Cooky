from app import db
from .model import User
from app.helpers.exceptions import NotFoundException

def getAll():
  data = []
  query = 'SELECT * FROM User'
  results = db.select(query)
  for result in results:
    data.append(User(result))
  return data

def getById(id):
  query = 'SELECT * FROM User WHERE id = %(id)s'
  result = db.select(query, { 'id': id }, 1)
  if result:
    return User(result)
  else:
    raise NotFoundException(str.format("No user found with id '%d'", id))
