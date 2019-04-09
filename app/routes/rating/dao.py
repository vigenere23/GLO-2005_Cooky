from app import db
from .model import RatingModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class RatingDao(BaseDao):

    def __init__(self):
        self.mapper = SQLMapper('Rating', RatingModel)

    def getAll(self):
        query = 'SELECT * FROM Rating'
        results = db.select(query)
        return self.mapper.from_tuples(results)
    
    def getById(self, id):
        if not id:
            raise Exception("Id cannot be None")

        query = 'SELECT * FROM Rating WHERE id = %(id)s'
        result = db.select(query, { 'id': id }, 1)
        if result:
            return self.mapper.from_tuple(result)
        else:
            raise NotFoundException(str.format("No rating found with id '%d'", id))
          

    def save(self, ratingModel):
            if not isinstance(ratingModel, RatingModel):
                raise ValueError("ratingModel should be of type RatingModel")
            query = 'INSERT INTO Rating (id, id_Recipe, id_User, value) VALUES (%s, %s, %s, %s)'
            ratingId = db.insert(query, self.mapper.to_tuple(ratingModel))
            
            if ratingId:
                return self.getById(ratingId)
            else:
                raise Exception("Could not save rating")