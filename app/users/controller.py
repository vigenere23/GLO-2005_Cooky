from flask import Blueprint
from app.Response import Response
from . import dao

routes = Blueprint('user', __name__)

@routes.route('/')
def index():
  return Response.create(dao.getAll(), 200)
