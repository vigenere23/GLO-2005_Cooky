from flask import Blueprint
from app import app, db

routes = Blueprint('user', __name__)

@routes.route('/')
def index():
  text = 'Users: \n'
  query = 'SELECT * FROM Utilisateur'
  results = db.select(query)
  for result in results:
    text += str(result[1])
  return text

app.register_blueprint(routes, url_prefix='/user')
