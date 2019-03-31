from app import db
from .model import ProfileModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class ProfileDao(BaseDao):

    def __init__(self):
        self.mapper = SQLMapper('Profile', ProfileModel)

    def getAll(self):
        query = 'SELECT * FROM Profile'
        results = db.select(query)
        return self.mapper.from_tuples(results)

    def getProfileByUser(self, id_User):
        query = 'SELECT * FROM Profile WHERE id_User = %(id_User)s'
        results = db.select(query, {'id_User': id_User})
        return self.mapper.from_tuples(results)
    
    def save(self, profileModel):
        if not isinstance(profileModel, ProfileModel):
            raise ValueError("profileModel should be of type ProfileModel")
        pass