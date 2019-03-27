from app import db
from .model import RatingModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class RecipeDao(BaseDao):

    def __init__(self):
        self.mapper = SQLMapper('Rating', RatingModel)

    def getAll(self):
        query = 'SELECT * FROM Rating'
        results = db.select(query)
        return self.mapper.from_tuples(results)
    
    def save(self, ratingModel):
        if not isinstance(ratingModel, RatingModel):
            raise ValueError("ratingModel should be of type RatingModel")
        pass