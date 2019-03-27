from app.helpers.BaseModel import BaseModel

class ProfileModel(BaseModel):
  def __init__(self, id=None, id_User=None, bio=None, backgroundPicture=None):
    self.id = id
    self.id_User = id_User
    self.bio = bio
    self.backgroundPicture = backgroundPicture