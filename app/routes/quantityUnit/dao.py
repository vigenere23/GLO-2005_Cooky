from app import db
from .model import QuantityUnitModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class QuantityUnitDao(BaseDao):

    def __init__(self):
        self.mapper = SQLMapper('QuantityUnit', QuantityUnitModel)

    def getAll(self):
        query = 'SELECT * FROM QuantityUnit'
        results = db.select(query)
        return self.mapper.from_tuples(results)
    
    def save(self, quantityUnitModel):
        if not isinstance(quantityUnitModel, QuantityUnitModel):
            raise ValueError("quantityUnitModel should be of type QuantityUnitModel")
        pass