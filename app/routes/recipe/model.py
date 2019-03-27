from app.helpers.BaseModel import BaseModel

class RecipeModel(BaseModel):
  def __init__(self, id=None, other_attribute=None, **kwargs):
    self.id = id
    self.other_attribute = other_attribute