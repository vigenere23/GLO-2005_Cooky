from app import db
from .model import RecipeModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException
from ..recipeIngredient.model import RecipeIngredientModel
from ..recipeIngredient.dao import RecipeIngredientDao

recipeIngredientDao = RecipeIngredientDao()

class RecipeDao(BaseDao):

    def __init__(self):
        self.mapper = SQLMapper('Recipe', RecipeModel)

    def getAll(self):
        query = 'SELECT * FROM Recipe'
        results = db.select(query)
        return self.mapper.from_tuples(results)

    def getRecipeById(self, id):
        if not id:
            raise Exception("Id cannot be None")
        query = 'SELECT * FROM Recipe WHERE id = %(id)s'
        result = db.select(query, { 'id': id }, 1)
        if result:
            return self.mapper.from_tuple(result)
        else:
            raise NotFoundException(str.format("No recipe found with id '%d'", id))

    def getRecipeByName(self, name):
        query = 'SELECT * FROM Recipe WHERE name = %(name)s'
        results = db.select(query, {'name': name})
        return self.mapper.from_tuples(results)


    def getAllRecipesByUser(self, id_User):
        query = 'SELECT * FROM Recipe WHERE id_User = %(id_User)s'
        results = db.select(query, {'id_User': id_User})
        return self.mapper.from_tuples(results)
    
    def save(self, recipeModel, dataIngredient):
        if not isinstance(recipeModel, RecipeModel):
            raise ValueError("recipeModel should be of type RecipeModel")

        query = 'INSERT INTO Recipe (id, id_User, name, directives) VALUES (%s, %s, %s, %s)'
        newRecipeId = db.insert(query, self.mapper.to_tuple(recipeModel))
        if newRecipeId:
            for i in range(len(dataIngredient['id_Ingredient'])):
                data = { 
                    'id_Recipe': newRecipeId,
                    'id_Ingredient': dataIngredient['id_Ingredient'][i],
                    'id_QuantityUnit': dataIngredient['id_QuantityUnit'][i],
                    'totalQuantity': dataIngredient['totalQuantity'][i]
                }
                recipeIngredientModel = RecipeIngredientModel(**data)
                recipeIngredientDao.save(recipeIngredientModel)
            return self.getRecipeById(newRecipeId)
        else:
            raise Exception("Could not save recipe")