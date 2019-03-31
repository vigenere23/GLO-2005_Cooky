from app import db
from .model import CartItemModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class CartItemDao(BaseDao):

    def __init__(self):
        self.mapper = SQLMapper('CartItem', CartItemModel)

    def getAll(self):
        query = 'SELECT * FROM CartItem'
        results = db.select(query)
        return self.mapper.from_tuples(results)

    def getItemByCart(self, id_Cart):
        query = 'SELECT * FROM CartItem WHERE id_Cart = %(id_Cart)s'
        results = db.select(query, {'id_Cart': id_Cart})
        return self.mapper.from_tuples(results)
    
    def save(self, cartItemModel):
        if not isinstance(cartItemModel, CartItemModel):
            raise ValueError("cartItemModel should be of type CartItemModel")
        pass