from app import db
from .model import RatingModel
from app.helpers.BaseDao import BaseDao

class RatingDao(BaseDao):

    def __init__(self):
        super().__init__('Rating', RatingModel)
    
    def save(self, ratingModel):

        if not isinstance(ratingModel, RatingModel):
            raise ValueError("ratingModel should be of type RatingModel")

        query = 'INSERT INTO Rating (id, id_Recipe, id_User, value) VALUES (%s, %s, %s, %s)'
        newItemId = db.insert(query, self._mapper.to_tuple(ratingModel))
       
        if newItemId:
            return self.getById(newItemId)
        else:
            raise Exception("Could not save rate")
