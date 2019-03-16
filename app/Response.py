import flask

def __create(data, status):
  mimetype = 'text/plain'
  
  if not isinstance(data, str):
    data = flask.json.dumps(data)
    mimetype = 'application/json'

  return flask.Response(data, status=status, mimetype=mimetype)

def success(data, status=200):
  return __create(data, status)

def error(error, status=500):
  return __create({
    'error': error
  }, status)
