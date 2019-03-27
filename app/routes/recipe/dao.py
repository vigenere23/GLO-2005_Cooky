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

    def getAllRecipeByUser(self, id_User):
        query = 'SELECT * From Recipe WHERE id_User = %(id_User)s'
        #cant fetch them all only 1 is working
        #limit should be 0 but not working
        result = db.select(query, {'id_User': id_User}, 1)
        if result:
            return self.mapper.from_tuple(result)
        else:
            raise NotFoundException(str.format("No recipe found for user '%d'", id_User))
    
    def save(self, recipeModel):
        if not isinstance(recipeModel, RecipeModel):
            raise ValueError("recipeModel should be of type RecipeModel")
        pass