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