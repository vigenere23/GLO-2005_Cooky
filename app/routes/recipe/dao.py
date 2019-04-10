from app import db
from .model import RecipeModel
from app.helpers.BaseDao import BaseDao
from ..recipeIngredient.model import RecipeIngredientModel
from ..recipeIngredient.dao import RecipeIngredientDao

recipeIngredientDao = RecipeIngredientDao()

class RecipeDao(BaseDao):

    def __init__(self):
        super().__init__('Recipe', RecipeModel)

    def getRecipesByName(self, name):
        query = 'SELECT * FROM Recipe WHERE LOWER(name) LIKE LOWER(%(name)s)'
        results = db.select(query, {'name': '%{}%'.format(name)})
        return self._mapper.from_tuples(results)


    def getAllRecipesByUser(self, id_User):
        query = 'SELECT * FROM Recipe WHERE id_User = %(id_User)s'
        results = db.select(query, {'id_User': id_User})
        return self._mapper.from_tuples(results)

    def modifyRecipeName(self, name, id):
        query = 'UPDATE Recipe SET name = \'{}\' WHERE id = {}'.format(name, id)
        db.modify(query, {'id': id, 'name': name})
        return {"id": id, "name": name}

    def modifyRecipeDirective(self, directives, id):
        query = 'UPDATE Recipe SET directives = \'{}\' WHERE id = {}'.format(directives, id)
        db.modify(query, {'directives': directives})
        return {"id": id, "directives": directives}

    
    def deleteRecipe(self, id):
        query = 'DELETE FROM Recipe WHERE id = %(id)s'
        db.delete(query, {"id": id})
    
    def save(self, recipeModel, ingredients):
        if not isinstance(recipeModel, RecipeModel):
            raise ValueError("recipeModel should be of type RecipeModel")

        query = 'INSERT INTO Recipe (id, id_User, name, directives) VALUES (%s, %s, %s, %s)'
        recipeId = db.insert(query, self._mapper.to_tuple(recipeModel))
        if recipeId:
            for ingredient in ingredients:
                data = {
                    'id_Recipe': recipeId,
                    'id_Ingredient': ingredient['id_Ingredient'],
                    'id_QuantityUnit': ingredient['id_QuantityUnit'],
                    'totalQuantity': ingredient['totalQuantity']
                }
                recipeIngredientModel = RecipeIngredientModel(**data)
                recipeIngredientDao.save(recipeIngredientModel)
            return self.getById(recipeId)
        else:
            raise Exception("Could not save recipe")