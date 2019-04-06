from app import db
from .model import RecipeIngredientModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class RecipeIngredientDao(BaseDao):

    def __init__(self):
        self.mapper = SQLMapper('RecipeIngredient', RecipeIngredientModel)

    def getAll(self):
        query = 'SELECT * FROM RecipeIngredient'
        results = db.select(query)
        return self.mapper.from_tuples(results)

    def getById(self, id):
        if not id:
            raise Exception("Id cannot be None")

        query = 'SELECT * FROM RecipeIngredient WHERE id = %(id)s'
        result = db.select(query, { 'id': id }, 1)
        if result:
            return self.mapper.from_tuple(result)
        else:
            raise NotFoundException(str.format("No recipeIngredient found with id '%d'", id))

    def getIngredientsByRecipe(self, id_Recipe):
        querry = 'SELECT * FROM RecipeIngredient WHERE id_Recipe = %(id_Recipe)s'
        results = db.select(querry, {'id_Recipe': id_Recipe})
        return self.mapper.from_tuples(results)
    
    def save(self, recipeIngredientModel):
        if not isinstance(recipeIngredientModel, RecipeIngredientModel):
            raise ValueError("recipeIngredientModel should be of type RecipeIngredientModel")
        pass
        query = 'INSERT INTO RecipeIngredient (id, id_Recipe, id_Ingredient, id_QuantityUnit, totalQuantity) VALUES (%s, %s, %s, %s, %s)'
        newRecipeId = db.insert(query, self.mapper.to_tuple(recipeIngredientModel))
      
        if newRecipeId:
            return self.getById(newRecipeId)
        else:
            raise Exception("Could not save ingredient to cart")