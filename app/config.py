import os
import platform

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'here-should-be-a-secret-key' # needed???
  DATABASE = {
    'user': 'root',
    'password': '',
    'host': '172.17.0.2' if platform.system() == 'Windows' else 'localhost',
    'port': '1337',
    'database': 'projet'
  }
