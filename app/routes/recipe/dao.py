from app import db
from .model import RecipeModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class RecipeDao(BaseDao):

    def __init__(self):
        self.mapper = SQLMapper('Recipe', RecipeModel)

    def getAll(self):
        query = 'SELECT * FROM Recipe'
        results = db.select(query)
        return self.mapper.from_tuples(results)

    def getAllRecipesByUser(self, id_User):
        query = 'SELECT * From Recipe WHERE id_User = %(id_User)s'
        results = db.select(query, {'id_User': id_User})
        return self.mapper.from_tuples(results)
    
    def save(self, recipeModel):
        if not isinstance(recipeModel, RecipeModel):
            raise ValueError("recipeModel should be of type RecipeModel")
        pass