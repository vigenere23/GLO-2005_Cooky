import os
import platform

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'here-should-be-a-secret-key' # needed???
  DATABASE = {
    'user': 'root',
    'password': os.environ.get('MYSQL_ROOT_PASSWORD', ''),
    'host': os.environ.get('DB_HOST', 'localhost'),
    'port': os.environ.get('DB_PORT', '3306'),
    'database': 'projet'
  }
  JWT_AUTH_URL_RULE = '/login/'
