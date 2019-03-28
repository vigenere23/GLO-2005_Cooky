from app import db
from .model import LikeRecipeModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class RecipeDao(BaseDao):

    def __init__(self):
        self.mapper = SQLMapper('LikeRecipe', LikeRecipeModel)

    def getAll(self):
        query = 'SELECT * FROM LikeRecipe'
        results = db.select(query)
        return self.mapper.from_tuples(results)
    
    def save(self, likeRecipeModel):
        if not isinstance(likeRecipeModel, LikeRecipeModel):
            raise ValueError("likeRecipeModel should be of type LikeRecipeModel")
        pass