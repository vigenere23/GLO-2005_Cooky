from app import db
from .model import CartModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class CartDao(BaseDao):

    def __init__(self):
        self.mapper = SQLMapper('Cart', CartModel)

    def getAll(self):
        query = 'SELECT * FROM Cart'
        results = db.select(query)
        return self.mapper.from_tuples(results)

    def getCartByUser(self, id_User):
        query = 'SELECT * FROM Cart WHERE id_User = %(id_User)s'
        results = db.select(query, {'id_User': id_User})
        return self.mapper.from_tuples(results)
    
    def getById(self, id):
        if not id:
            raise Exception("Id cannot be None")

        query = 'SELECT * FROM Cart WHERE id = %(id)s'
        result = db.select(query, { 'id': id }, 1)
        if result:
            return self.mapper.from_tuple(result)
        else:
            raise NotFoundException(str.format("No cart found with id '%d'", id))
          

    def save(self, cartModel):
            if not isinstance(cartModel, CartModel):
                raise ValueError("cartModel should be of type cartModel")
            query = 'INSERT INTO Cart (id, id_User, totalCost) VALUES (%s, %s, %s)'
            cartId = db.insert(query, self.mapper.to_tuple(cartModel))
            
            if cartId:
                return self.getById(cartId)
            else:
                raise Exception("Could not save cart")