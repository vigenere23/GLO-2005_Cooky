from app import db
from .model import IngredientTypeModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class IngredientTypeDao(BaseDao):

    def __init__(self):
        self.mapper = SQLMapper('IngredientType', IngredientTypeModel)

    def getAll(self):
        query = 'SELECT * FROM IngredientType'
        results = db.select(query)
        return self.mapper.from_tuples(results)
    
    def save(self, ingredientTypeModel):
        if not isinstance(ingredientTypeModel, IngredientTypeModel):
            raise ValueError("ingredientTypeModel should be of type IngredientTypeModel")
        pass