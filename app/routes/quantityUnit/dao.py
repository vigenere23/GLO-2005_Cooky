from app import db
from .model import QuantityUnitModel
from app.helpers.BaseDao import BaseDao

class QuantityUnitDao(BaseDao):

    def __init__(self):
        super().__init__('QuantityUnit', QuantityUnitModel)

    def save(self, quantityUnitModel):
        if not isinstance(quantityUnitModel, QuantityUnitModel):
            raise ValueError("quantityUnitModel should be of type QuantityUnitModel")
        pass

    def getAllQuantityUnitsOfSameType(self, quantityUnitModel):
        if not isinstance(quantityUnitModel, QuantityUnitModel):
            raise ValueError("quantityUnitModel should be of type QuantityUnitModel")
        
        query = 'SELECT * FROM QuantityUnit WHERE id_QuantityType = %(quantity_type_id)s'
        data = { 'quantity_type_id': quantityUnitModel.id_QuantityType }
        results = db.select(query, data)
        return self._mapper.from_tuples(results)