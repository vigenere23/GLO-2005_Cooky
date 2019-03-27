from app.helpers.BaseModel import BaseModel

class RecipeModel(BaseModel):
  def __init__(self, id=None, id_User=None, name=None, directives=None):
    self.id = id
    self.id_User = id_User
    self.name = name
    self.directives = directives