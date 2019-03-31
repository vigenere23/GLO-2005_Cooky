from app import db
from .model import QuantityTypeModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class QuantityTypeDao(BaseDao):

    def __init__(self):
        self.mapper = SQLMapper('QuantityType', QuantityTypeModel)

    def getAll(self):
        query = 'SELECT * FROM QuantityType'
        results = db.select(query)
        return self.mapper.from_tuples(results)
    
    def save(self, quantityTypeModel):
        if not isinstance(quantityTypeModel, QuantityTypeModel):
            raise ValueError("quantityTypeModel should be of type QuantityTypeModel")
        pass