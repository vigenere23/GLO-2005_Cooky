from app import db
from .model import AddressModel
from app.helpers.BaseDao import BaseDao

class AddressDao(BaseDao):

    def __init__(self):
        super().__init__('Address', AddressModel)
    
    def save(self, addressModel):
        if not isinstance(addressModel, AddressModel):
            raise ValueError("addressModel should be of type AddressModel")
        pass