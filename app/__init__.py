from flask import Flask
from .config import Config
from .DB import DB

app = Flask(__name__)
app.config.from_object(Config)

db = DB(Config.DATABASE)

from app import main, users
