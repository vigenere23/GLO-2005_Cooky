from app import app
from .controller import routes

app.register_blueprint(routes, url_prefix='/recipes')