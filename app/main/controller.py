from flask import Blueprint
from app import response

routes = Blueprint('main', __name__)

@routes.route('/')
def index():
  return response.success("App is running correctly")
