from app import db
from .model import CartModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class RecipeDao(BaseDao):

    def __init__(self):
        self.mapper = SQLMapper('Cart', CartModel)

    def getAll(self):
        query = 'SELECT * FROM Cart'
        results = db.select(query)
        return self.mapper.from_tuples(results)
    
    def save(self, cartModel):
        if not isinstance(cartModel, CartModel):
            raise ValueError("cartModel should be of type CartModel")
        pass