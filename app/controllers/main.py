from flask import Blueprint
from app import app, db

routes = Blueprint('main', __name__)

@routes.route('/')
def index():
  return "App is running correctly"

app.register_blueprint(routes, url_prefix='/')
