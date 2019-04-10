from app import db
from .model import CartItemModel
from app.helpers.BaseDao import BaseDao

class CartItemDao(BaseDao):

    def __init__(self):
        super().__init__('CartItem', CartItemModel)

    def getItemByCart(self, id_Cart):
        query = 'SELECT * FROM CartItem WHERE id_Cart = %(id_Cart)s'
        results = db.select(query, {'id_Cart': id_Cart})
        return self._mapper.from_tuples(results)

    def deleteIngredient(self, id_Cart, id_Ingredient):
        query = 'DELETE FROM CartItem WHERE id_Cart = %(id_Cart)s AND id_Ingredient = %(id_Ingredient)s'
        db.delete(query, {"id_Cart": id_Cart, "id_Ingredient": id_Ingredient})
        
    def save(self, cartItemModel):
        if not isinstance(cartItemModel, CartItemModel):
            raise ValueError("cartItemModel should be of type CartItemModel")
        query = 'INSERT INTO CartItem (id, id_Ingredient, id_Cart, multiplier, subCost) VALUES (%s, %s, %s, %s, %s)'
        newItemId = db.insert(query, self._mapper.to_tuple(cartItemModel))
      
        if newItemId:
            return self.getById(newItemId)
        else:
            raise Exception("Could not save ingredient to cart")