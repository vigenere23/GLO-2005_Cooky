from app import db
from .model import AddressModel
from app.helpers.BaseDao import BaseDao

class AddressDao(BaseDao):

    def __init__(self):
        super().__init__('Address', AddressModel)
    
    def save(self, addressModel):
        if not isinstance(addressModel, AddressModel):
            raise ValueError("addressModel should be of type AddressModel")
        
        query = 'INSERT INTO Address (`id`,`number`,`apartment`,`street`,`city`,`country`) VALUES (%s, %s, %s, %s, %s, %s)'
        newAddressId = db.insert(query, self._mapper.to_tuple(addressModel))

        if newAddressId:
            return self.getById(newAddressId)
        else:
            raise Exception("Could not save commend")