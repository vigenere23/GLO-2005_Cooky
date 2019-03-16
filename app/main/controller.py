from flask import Blueprint

routes = Blueprint('main', __name__)

@routes.route('/')
def index():
  return "App is running correctly"
