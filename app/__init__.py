from flask import Flask
from flask_cors import CORS
from .config import Config
from .helpers.DB import DB

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)

db = DB(Config.DATABASE)

from . import auth, routes
