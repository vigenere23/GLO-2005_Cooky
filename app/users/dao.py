from app import db
from .model import User
from app.exceptions import NotFoundException

def getAll():
  data = []
  query = 'SELECT * FROM Utilisateur'
  results = db.select(query, None)
  for result in results:
    data.append(User(*result))
  return data

def getById(id):
  query = 'SELECT * FROM Utilisateur WHERE id = %(id)s'
  result = db.select(query, { 'id': id }, 1)
  if result:
    return User(*result)
  else:
    raise NotFoundException(str.format("No user found with id '%d'", id))
