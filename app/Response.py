import flask

class Response():

  @staticmethod
  def create(data, status):
    if (not isinstance(data, str)):
      data = flask.json.dumps(data)

    return flask.Response(data, status=status, mimetype='application/json')
