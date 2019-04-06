from app import db
from .model import LikeRecipeModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class LikeRecipeDao(BaseDao):

    def __init__(self):
        self.mapper = SQLMapper('LikeRecipe', LikeRecipeModel)

    def getAll(self):
        query = 'SELECT * FROM LikeRecipe'
        results = db.select(query)
        return self.mapper.from_tuples(results)
    
    def getLikeRecipeById(self, id):
        if not id:
            raise Exception("Id cannot be None")
       
        query = 'SELECT * FROM LikeRecipe WHERE id = %(id)s'
        result = db.select(query, { 'id': id }, 1)
        if result:
            return self.mapper.from_tuple(result)
        else:
            raise NotFoundException(str.format("No likeRecipe found with id '%d'", id))


    def getLikeRecipeByUser(self, id_User):
        query = 'SELECT * FROM LikeRecipe WHERE id_User = %(id_User)s'
        results = db.select(query, {'id_User': id_User})
        return self.mapper.from_tuples(results)

    
    def save(self, likeRecipeModel):
        if not isinstance(likeRecipeModel, LikeRecipeModel):
            raise ValueError("likeRecipeModel should be of type LikeRecipeModel")
        query = 'INSERT INTO LikeRecipe (id, id_Recipe, id_User) VALUES (%s, %s, %s)'
        newLikeRecipe = db.insert(query, self.mapper.to_tuple(likeRecipeModel))

        if newLikeRecipe:
            return self.getLikeRecipeById(newLikeRecipe)
        else:
            raise Exception("Could not like this recipe")