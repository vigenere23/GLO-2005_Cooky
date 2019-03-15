import os
basedir = os.path.abspath(os.path.dirname(__file__ + '/../'))

class Config:
  SECRET_KEY = os.environ.get('SECRET_KEY') or 'here-should-be-a-secret-key' # needed???
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'mysql:///' + os.path.join(basedir, '/mysql/project')
