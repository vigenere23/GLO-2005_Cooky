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


    def getItemById(self, id):
        if not id:
            raise Exception("Id cannot be None")

        query = 'SELECT * FROM CartItem WHERE id = %(id)s'
        result = db.select(query, { 'id': id }, 1)
        if result:
            return self.mapper.from_tuple(result)
        else:
            raise NotFoundException(str.format("No cartItem found with id '%d'", id))

    def getItemByCart(self, id_Cart):
        query = 'SELECT * FROM CartItem WHERE id_Cart = %(id_Cart)s'
        results = db.select(query, {'id_Cart': id_Cart})
        return self.mapper.from_tuples(results)

    def deleteIngredient(self, id_Cart, id_Ingredient):
        query = 'DELETE FROM CartItem WHERE id_Cart = %(id_Cart)s AND id_Ingredient = %(id_Ingredient)s'
        db.delete(query, {"id_Cart": id_Cart, "id_Ingredient": id_Ingredient})
        
    def save(self, cartItemModel):
        if not isinstance(cartItemModel, CartItemModel):
            raise ValueError("cartItemModel should be of type CartItemModel")
        query = 'INSERT INTO CartItem (id, id_Ingredient, id_Cart, multiplier, subCost) VALUES (%s, %s, %s, %s, %s)'
        newItemId = db.insert(query, self.mapper.to_tuple(cartItemModel))
      
        if newItemId:
            return self.getItemById(newItemId)
        else:
            raise Exception("Could not save ingredient to cart")