from app import db
from .model import AddressModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class RecipeDao(BaseDao):

    def __init__(self):
        self.mapper = SQLMapper('Address', AddressModel)

    def getAll(self):
        query = 'SELECT * FROM Address'
        results = db.select(query)
        return self.mapper.from_tuples(results)
    
    def save(self, addressModel):
        if not isinstance(addressModel, AddressModel):
            raise ValueError("addressModel should be of type AddressModel")
        pass