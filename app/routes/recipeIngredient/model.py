from app.helpers.BaseModel import BaseModel

class RecipeIngredientModel(BaseModel):
  def __init__(self, id=None, id_Recipe=None, id_Ingredient=None, id_QuantityUnit=None, totalQuantity=None):
    self.id = id
    self.id_Recipe = id_Recipe
    self.id_Ingredient = id_Ingredient
    self.id_Quantity = id_QuantityUnit
    self.totalQuantity = totalQuantity