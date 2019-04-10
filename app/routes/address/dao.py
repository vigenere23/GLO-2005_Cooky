from app import db
from .model import AddressModel
from app.helpers.BaseDao import BaseDao

class AddressDao(BaseDao):

    def __init__(self):
        super().__init__('Address', AddressModel)

    def getAddress(self, id):
        query = 'SELECT * FROM Recipe WHERE id = %(id)s'
        results = db.select(query, {'id': id})
        return self._mapper.from_tuples(results)
    
    def save(self, addressModel):
        if not isinstance(addressModel, AddressModel):
            raise ValueError("addressModel should be of type AddressModel")
        pass