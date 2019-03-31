from app import db
from .model import RecipeIngredientModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class RecipeIngredientDao(BaseDao):

    def __init__(self):
        self.mapper = SQLMapper('RecipeIngredient', RecipeIngredientModel)

    def getAll(self):
        query = 'SELECT * FROM RecipeIngredient'
        results = db.select(query)
        return self.mapper.from_tuples(results)

    def getIngredientsByRecipe(self, id_Recipe):
        querry = 'SELECT * FROM RecipeIngredient WHERE id_Recipe = %(id_Recipe)s'
        results = db.select(querry, {'id_Recipe': id_Recipe})
        return self.mapper.from_tuples(results)
    
    def save(self, recipeIngredientModel):
        if not isinstance(recipeIngredientModel, RecipeIngredientModel):
            raise ValueError("recipeIngredientModel should be of type RecipeIngredientModel")
        pass