import os
import platform

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'here-should-be-a-secret-key' # needed???
  DATABASE = {
    'user': 'root',
    'password': '',
    'host': '192.168.99.100' if platform.system() == 'Windows' else 'localhost',
    'port': '1337',
    'database': 'projet'
  }
  JWT_AUTH_URL_RULE = '/login/'
