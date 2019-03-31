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

    def getRecipeById(self, id):
        if not id:
            raise Exception("Id cannot be None")
        query = 'SELECT * FROM Recipe WHERE id = %(id)s'
        result = db.select(query, { 'id': id }, 1)
        if result:
            return self.mapper.from_tuple(result)
        else:
            raise NotFoundException(str.format("No recipe found with id '%d'", id))


    def getAllRecipesByUser(self, id_User):
        query = 'SELECT * FROM Recipe WHERE id_User = %(id_User)s'
        results = db.select(query, {'id_User': id_User})
        return self.mapper.from_tuples(results)
    
    def save(self, recipeModel):
        if not isinstance(recipeModel, RecipeModel):
            raise ValueError("recipeModel should be of type RecipeModel")
        pass