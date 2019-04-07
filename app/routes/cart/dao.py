from app import db
from .model import CartModel
from app.helpers.BaseDao import BaseDao

class CartDao(BaseDao):

    def __init__(self):
        super().__init__('Cart', CartModel)

    def getCartByUser(self, id_User):
        query = 'SELECT * FROM Cart WHERE id_User = %(id_User)s'
        results = db.select(query, {'id_User': id_User})
        return self._mapper.from_tuples(results)
    
    def save(self, cartModel):
        if not isinstance(cartModel, CartModel):
            raise ValueError("cartModel should be of type CartModel")
        pass