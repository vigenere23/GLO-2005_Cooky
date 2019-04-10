from app.helpers.BaseModel import BaseModel

class UserModel(BaseModel):

  def __init__(self, id=None, username=None, bio=None, id_CurrentCart=None):
    self.id = id
    self.username = username
    self.bio = bio
    self.id_CurrentCart=None
