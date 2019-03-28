from app import db
from .model import IngredientModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class RecipeDao(BaseDao):

    def __init__(self):
        self.mapper = SQLMapper('Ingredient', IngredientModel)

    def getAll(self):
        query = 'SELECT * FROM Ingredient'
        results = db.select(query)
        return self.mapper.from_tuples(results)
    
    def save(self, ingredientModel):
        if not isinstance(ingredientModel, IngredientModel):
            raise ValueError("ingredientModel should be of type IngredientModel")
        pass