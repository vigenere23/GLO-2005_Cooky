from flask_jwt import JWT
from app import app
from .helpers import response
from .routes.users.dao import UserDao
from .routes.account.dao import AccountDao

def authenticate(username, password):
  userDao = UserDao()
  accountDao = AccountDao()
  try:
    user = userDao.getByUsername(username)
    account = accountDao.getAccountByUserId(user.id)
    if account.password == password:
      return user
  except:
    return None

def identity(payload):
  userDao = UserDao()
  user_id = payload['identity']
  try:
    return userDao.getById(user_id)
  except:
    return None

jwt = JWT(app, authenticate, identity)

@jwt.auth_response_handler
@response.handleExceptions
def jwt_response_handler(access_token, identity):
  return response.success({
    'token': access_token.decode('utf-8'),
    'id': identity.id,
    'username': identity.username
  })

@jwt.jwt_error_handler
@response.handleExceptions
def jwt_error_handler(error):
  return response.error(
    error.description,
    status=error.status_code
  )
