from flask import Blueprint
from flask_jwt import jwt_required, current_identity
from app.helpers import response

routes = Blueprint('authentication', __name__)

@routes.route('/protected')
@jwt_required()
@response.handleExceptions
def protected():
  return response.success(current_identity)
