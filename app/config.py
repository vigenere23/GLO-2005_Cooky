import os

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'here-should-be-a-secret-key' # needed???
  DATABASE = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'port': '1337',
    'database': 'projet'
  }
