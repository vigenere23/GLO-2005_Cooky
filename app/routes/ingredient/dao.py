from app import db
from .model import IngredientModel
from app.helpers.BaseDao import BaseDao

class IngredientDao(BaseDao):

    def __init__(self):
        super().__init__('Ingredient', IngredientModel)
    
    def getIngredientsByName(self, name):
        query = 'SELECT * FROM Ingredient WHERE name = %(name)s'
        results = db.select(query, {'name': name})
        return self._mapper.from_tuples(results)
    
    def save(self, ingredientModel):
        if not isinstance(ingredientModel, IngredientModel):
            raise ValueError("ingredientModel should be of type IngredientModel")
        pass