from app.helpers.BaseModel import BaseModel

class CommentModel(BaseModel):
  def __init__(self, id=None, id_Recipe=None, id_User=None, text=None):
    self.id = id
    self.id_Recipe = id_Recipe
    self.id_User = id_User
    self.text = text