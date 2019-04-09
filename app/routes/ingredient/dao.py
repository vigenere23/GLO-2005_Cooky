from app import db
from .model import IngredientModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class IngredientDao(BaseDao):

    def __init__(self):
        self.mapper = SQLMapper('Ingredient', IngredientModel)

    def getById(self, id):
        if not id:
            raise Exception("Id cannot be None")

        query = 'SELECT * FROM Ingredient WHERE id = %(id)s'
        result = db.select(query, { 'id': id }, 1)
        if result:
            return self.mapper.from_tuple(result)
        else:
            raise NotFoundException(str.format("No ingredient found with id '%d'", id))
            
    def getAll(self):
        query = 'SELECT * FROM Ingredient'
        results = db.select(query)
        return self.mapper.from_tuples(results)
    
    def getIngredientByName(self, name):
        query = 'SELECT * FROM Ingredient WHERE name = %(name)s'
        results = db.select(query, {'name': name})
        return self.mapper.from_tuples(results)
    

    def save(self, ingredientModel):
        if not isinstance(ingredientModel, IngredientModel):
            raise ValueError("ingredientModel should be of type IngredientModel")
        query = 'INSERT INTO Ingredient (id, id_IngredientType, id_QuantityUnit, name, baseCost, baseQuantity) VALUES (%s, %s, %s, %s, %s, %s)'
        ingredientId = db.insert(query, self.mapper.to_tuple(ingredientModel))
        
        if ingredientId:
            return self.getById(ingredientId)
        else:
            raise Exception("Could not save ingredient")