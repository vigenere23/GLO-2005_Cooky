from flask import Blueprint
from app import Response
from . import dao

routes = Blueprint('user', __name__)

@routes.route('/')
def index():
  return Response.success(dao.getAll())
