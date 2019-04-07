from app import db
from .model import RecipeModel
from app.helpers.BaseDao import BaseDao
from ..recipeIngredient.model import RecipeIngredientModel
from ..recipeIngredient.dao import RecipeIngredientDao

recipeIngredientDao = RecipeIngredientDao()

class RecipeDao(BaseDao):

    def __init__(self):
        super().__init__('Recipe', RecipeModel)

    def getRecipeByName(self, name):
        query = 'SELECT * FROM Recipe WHERE name = %(name)s'
        results = db.select(query, {'name': name})
        return self._mapper.from_tuples(results)


    def getAllRecipesByUser(self, id_User):
        query = 'SELECT * FROM Recipe WHERE id_User = %(id_User)s'
        results = db.select(query, {'id_User': id_User})
        return self._mapper.from_tuples(results)

    
    def deleteRecipe(self, id):
        query = 'DELETE FROM Recipe WHERE id = %(id)s'
        db.delete(query, {"id": id}) 
    
    def save(self, recipeModel, dataIngredient):
        if not isinstance(recipeModel, RecipeModel):
            raise ValueError("recipeModel should be of type RecipeModel")

        query = 'INSERT INTO Recipe (id, id_User, name, directives) VALUES (%s, %s, %s, %s)'
        newRecipeId = db.insert(query, self._mapper.to_tuple(recipeModel))
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
            return self.getById(newRecipeId)
        else:
            raise Exception("Could not save recipe")