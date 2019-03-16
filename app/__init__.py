from flask import Flask
from .config import Config
from .helpers.DB import DB

app = Flask(__name__)
app.config.from_object(Config)

db = DB(Config.DATABASE)

from app import routes
