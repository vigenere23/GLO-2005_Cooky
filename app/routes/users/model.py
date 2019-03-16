class User:
  def __init__(self, id, username, password, settings):
    self.__id = id
    self.username = username
    self.__password = password
    self.settings = settings

  def serialize(self):
    return {
      'id': self.__id,
      'username': self.username,
      'settings': self.settings
    }
