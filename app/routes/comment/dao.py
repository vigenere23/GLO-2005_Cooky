from app import db
from .model import CommentModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class CommentDao(BaseDao):

    def __init__(self):
        self.mapper = SQLMapper('Comment', CommentModel)

    def getAll(self):
        query = 'SELECT * FROM Comment'
        results = db.select(query)
        return self.mapper.from_tuples(results)

    def getCommandById(self, id):
        if not id:
            raise Exception("Id cannot be None")

        query = 'SELECT * FROM Comment WHERE id = %(id)s'
        result = db.select(query, { 'id': id }, 1)
        if result:
            return self.mapper.from_tuple(result)
        else:
            raise NotFoundException(str.format("No comment found with id '%d'", id))
    
    def save(self, commentModel):
        if not isinstance(commentModel, CommentModel):
            raise ValueError("commentModel should be of type CommentModel")
        query = 'INSERT INTO Comment (id, id_Recipe, id_User, text) VALUES (%s, %s, %s, %s)'
        newCommandId = db.insert(query, self.mapper.to_tuple(commentModel))

        if newCommandId:
            return self.getCommandById(newCommandId)
        else:
            raise Exception("Could not save commend")