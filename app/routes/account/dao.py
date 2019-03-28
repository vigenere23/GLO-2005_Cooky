from app import db
from .model import AccountModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class RecipeDao(BaseDao):

    def __init__(self):
        self.mapper = SQLMapper('Account', AccountModel)

    def getAll(self):
        query = 'SELECT * FROM Account'
        results = db.select(query)
        return self.mapper.from_tuples(results)
    
    def save(self, accountModel):
        if not isinstance(accountModel, AccountModel):
            raise ValueError("accountModel should be of type AccountModel")
        pass