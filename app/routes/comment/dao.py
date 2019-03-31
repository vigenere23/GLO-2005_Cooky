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
    
    def save(self, commentModel):
        if not isinstance(commentModel, CommentModel):
            raise ValueError("commentModel should be of type CommentModel")
        pass