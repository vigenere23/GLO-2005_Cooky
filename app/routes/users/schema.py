from app.helpers.BaseSchema import BaseSchema
from .model import UserModel

class UserSchema(BaseSchema):
  def __init__(self):
    super().__init__('User', UserModel)
