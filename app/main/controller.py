from flask import Blueprint
from app import Response

routes = Blueprint('main', __name__)

@routes.route('/')
def index():
  return Response.success("App is running correctly")
